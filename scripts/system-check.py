#!/usr/bin/env python3
"""The mechanical half of /system-check: every check here has a right answer.
The judgment half -- what to simplify, what's drifted, what to recommend --
is the skill in .claude/commands/system-check.md, which runs this first.

Read-only: nothing is left changed. (refresh.py writes files, so it's run,
compared, and its outputs restored.)

    python3 scripts/system-check.py

Exit 1 if anything under FAIL; WARN and INFO never fail the run.
"""

import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
LARGE_IMAGE_BYTES = 200_000

results = {"FAIL": [], "WARN": [], "INFO": [], "OK": []}


def add(level, msg):
    results[level].append(msg)


def run(cmd):
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip()


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8", errors="replace") as fh:
        return fh.read()


def tracked_files():
    code, out = run(["git", "ls-files"])
    return out.splitlines() if code == 0 else []


# ── Builds and validators ───────────────────────────────────

def check_commands():
    checks = [
        ("Findings pages match findings/*.md", [sys.executable, "scripts/build-findings.py", "--check"]),
        ("Home page sections match jobs.json", [sys.executable, "scripts/build-home.py", "--check"]),
        ("jobs.json structure", [sys.executable, "scripts/check-jobs-json.py"]),
        ("Asset cache-bust versions", ["bash", "scripts/check-asset-versions.sh"]),
    ]
    for label, cmd in checks:
        code, out = run(cmd)
        if code == 0:
            add("OK", label)
        else:
            add("FAIL", f"{label}: {out.splitlines()[-1] if out else 'failed'}  (run: {' '.join(cmd[1:] if cmd[0] == sys.executable else cmd)})")


def check_syntax():
    bad = []
    for f in tracked_files():
        if f.endswith(".py"):
            code, out = run([sys.executable, "-m", "py_compile", f])
            if code:
                bad.append(f"{f}: {out.splitlines()[-1]}")
    if shutil.which("node"):
        for f in tracked_files():
            if f.startswith("docs/") and f.endswith(".js"):
                code, out = run(["node", "--check", f])
                if code:
                    bad.append(f"{f}: {out.splitlines()[0]}")
    else:
        add("INFO", "node not installed here, so JavaScript syntax wasn't checked")
    if bad:
        for b in bad:
            add("FAIL", f"Syntax error in {b}")
    else:
        add("OK", "Python and JavaScript syntax")


def check_insights():
    """refresh.py regenerates stats.md and quotes.md. Run it, see whether
    they'd change, then put them back so this check stays read-only."""
    paths = ["jd-insights/stats.md", "jd-insights/quotes.md"]
    before = {p: read(p) for p in paths if os.path.exists(os.path.join(ROOT, p))}
    code, out = run([sys.executable, "jd-insights/refresh.py"])
    changed = [p for p in before if read(p) != before[p]]
    for p, text in before.items():
        with open(os.path.join(ROOT, p), "w", encoding="utf-8") as fh:
            fh.write(text)
    if code:
        add("FAIL", f"jd-insights/refresh.py errored: {out.splitlines()[-1] if out else ''}")
        return
    if changed:
        add("WARN", f"Generated insights are stale: {', '.join(changed)} (run: python3 jd-insights/refresh.py)")
    else:
        add("OK", "jd-insights stats.md and quotes.md current")
    stale = [l for l in out.splitlines() if "STALE" in l or "couldn't find" in l]
    for line in stale:
        add("WARN", f"findings.md: {line.strip()}")


# ── Security ────────────────────────────────────────────────

SECRET_PATTERNS = [
    ("AWS access key", r"AKIA[0-9A-Z]{16}"),
    ("private key", r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    ("GitHub token", r"\bgh[pousr]_[A-Za-z0-9]{36,}"),
    ("Anthropic/OpenAI-style key", r"\bsk-[A-Za-z0-9_-]{20,}"),
    ("Slack token", r"\bxox[baprs]-[A-Za-z0-9-]{10,}"),
    ("hard-coded API key", r"api[_-]?key\s*[:=]\s*['\"][A-Za-z0-9_\-]{16,}['\"]"),
]


def check_secrets():
    hits = []
    for f in tracked_files():
        full = os.path.join(ROOT, f)
        if not os.path.isfile(full) or os.path.getsize(full) > 1_000_000:
            continue
        if f.endswith((".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf")):
            continue
        text = read(f)
        for label, pat in SECRET_PATTERNS:
            if re.search(pat, text):
                hits.append(f"{f} (looks like a {label})")
    if hits:
        for h in hits:
            add("FAIL", f"Possible secret committed: {h}")
    else:
        add("OK", "No secrets found in tracked files")


def check_third_party():
    for f in tracked_files():
        if not (f.startswith("docs/") and f.endswith(".html")):
            continue
        for tag in re.findall(r"<script\b[^>]*\bsrc=\"https?://[^\"]+\"[^>]*>", read(f)):
            if "integrity=" not in tag:
                src = re.search(r'src="([^"]+)"', tag).group(1)
                add("INFO", f"Third-party script without an integrity hash: {src} (in {f})")
    for f in tracked_files():
        if f.startswith(".github/workflows/"):
            for use in re.findall(r"uses:\s*(\S+)", read(f)):
                if not re.search(r"@[0-9a-f]{40}$", use):
                    add("INFO", f"GitHub Action pinned to a tag, not a commit: {use} (in {f})")


# ── Dead weight ─────────────────────────────────────────────

def source_text():
    """Everything that could use a CSS class or reference an image."""
    parts = []
    for f in tracked_files():
        if (f.startswith("docs/") and f.endswith((".html", ".js", ".css", ".xml", ".txt", ".json"))) \
                or (f.startswith("scripts/") and f.endswith(".py")) or f in ("README.md",):
            parts.append(read(f))
    return "\n".join(parts)


def check_unused_css(sources):
    css = re.sub(r"/\*.*?\*/", "", read("docs/css/styles.css"), flags=re.S)
    classes = set()
    for selector in re.findall(r"([^{}]+)\{", css):
        if selector.strip().startswith("@"):
            continue
        classes.update(re.findall(r"\.([a-zA-Z_][\w-]*)", selector))
    # Classes built from a template (state--${variant}, state--{kind}) count
    # as used when their prefix is.
    prefixes = set(re.findall(r"([\w-]+)(?:\$\{|\{)", sources))
    used_text = sources.replace(read("docs/css/styles.css"), "")
    unused = sorted(c for c in classes
                    if not re.search(rf"(?<![\w-]){re.escape(c)}(?![\w-])", used_text)
                    and not any(c.startswith(p) and p.endswith("-") for p in prefixes))
    if unused:
        add("WARN", f"CSS classes nothing uses ({len(unused)}): {', '.join(unused)}")
    else:
        add("OK", "Every CSS class is used")


def check_images(sources):
    img_dir = os.path.join(DOCS, "images")
    tracked = set(tracked_files())
    for name in sorted(os.listdir(img_dir)):
        if name.startswith("."):  # .DS_Store and friends; .gitignore covers them
            continue
        rel = f"docs/images/{name}"
        size = os.path.getsize(os.path.join(img_dir, name))
        if name not in sources:
            state = "tracked" if rel in tracked else "untracked, not even committed"
            add("WARN", f"Image nothing references: {rel} ({size // 1024} KB, {state})")
        elif size > LARGE_IMAGE_BYTES:
            add("WARN", f"Large image: {rel} is {size // 1024} KB — check it against the size it's displayed at")


def check_untracked():
    code, out = run(["git", "status", "--porcelain", "--untracked-files=all"])
    untracked = [l[3:] for l in out.splitlines() if l.startswith("??")]
    for f in untracked:
        add("INFO", f"Untracked file (won't deploy): {f}")


def check_doc_drift():
    """Class names that docs describe in backticks (`.foo`) but the
    stylesheet no longer has — the kind of drift that makes instructions
    describe a site that isn't there anymore."""
    css = read("docs/css/styles.css")
    docs = ["CLAUDE.md", "findings/README.md"] + [
        f for f in tracked_files() if f.startswith(".claude/commands/") and f.endswith(".md")]
    for f in docs:
        for name in sorted(set(re.findall(r"`\.([a-z][\w-]*)", read(f)))):
            if not re.search(rf"\.{re.escape(name)}(?![\w-])", css):
                add("WARN", f"{f} mentions `.{name}`, which isn't in styles.css anymore")


def check_weight():
    files = ["docs/index.html", "docs/css/styles.css", "docs/js/scripts.js", "docs/js/menu.js",
             "docs/data/jobs.json"]
    parts = [f"{os.path.basename(f)} {os.path.getsize(os.path.join(ROOT, f)) // 1024} KB" for f in files]
    add("INFO", "Page weight: " + ", ".join(parts))


def main():
    os.chdir(ROOT)
    check_commands()
    check_syntax()
    check_insights()
    check_secrets()
    sources = source_text()
    check_unused_css(sources)
    check_images(sources)
    check_doc_drift()
    check_untracked()
    check_third_party()
    check_weight()

    marks = {"FAIL": "✗", "WARN": "⚠", "INFO": "·", "OK": "✓"}
    for level in ("FAIL", "WARN", "INFO", "OK"):
        if results[level]:
            print(f"\n{level} ({len(results[level])})")
            for msg in results[level]:
                print(f"  {marks[level]} {msg}")
    print(f"\nsystem-check: {len(results['FAIL'])} failing, {len(results['WARN'])} warnings, "
          f"{len(results['INFO'])} notes")
    sys.exit(1 if results["FAIL"] else 0)


if __name__ == "__main__":
    main()
