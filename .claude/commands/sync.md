Sync the local repo with `origin` and clean up stale branches. Run this at the start of a session, or any time to check whether local and remote have drifted.

## Step 1 — Check for uncommitted work

Run `git status`. If there's anything uncommitted, stop and tell the user rather than proceeding — don't stash or discard anything automatically.

## Step 2 — Fetch and compare

```
git fetch --prune origin
git log --oneline HEAD..origin/main   # commits on remote main we don't have
git log --oneline origin/main..HEAD   # commits we have that remote main doesn't
```

- **Behind only:** `git pull --ff-only origin main`. Report what came down (commit summary is enough, no need to dump full diffs unless something looks like it touched a file the user's mid-session on).
- **Ahead only:** don't push automatically — report what's unpushed and ask whether to push now.
- **Diverged (both ahead and behind):** report both sides and ask how to proceed rather than picking rebase vs. merge unilaterally.
- **Neither:** say so plainly, nothing to do.

## Step 3 — Check every other branch

```
git branch -r | grep -v 'HEAD ->' | grep -v 'origin/main$'
```

For each, check whether it's fully merged into (the now-synced) `origin/main`:

```
git merge-base origin/main origin/<branch>
git rev-parse origin/<branch>
# fully merged if these two hashes match
```

- **Fully merged, no unique commits:** safe to delete. List these together.
- **Has unique commits not on main:** never delete without asking. Show what the branch actually contains (`git log -p` on the unique commits, or at least the commit messages and file list) so the user can judge whether it's still-wanted work-in-progress or something to merge or discard.

## Step 4 — Report and act

Give a short summary: what got pulled, what's still unpushed (if anything), which branches are safe to delete, and which have real unmerged work with a one-line description of each.

Ask before deleting the merged branches (a single confirmation for the whole batch is fine — no need to ask once per branch). For any branch with unique commits, ask what the user wants to do with it (merge, leave it, or discard) rather than assuming.
