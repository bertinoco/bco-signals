#!/usr/bin/env python3
"""Validate docs/data/jobs.json's structure.

Catches the class of mistake a manual edit can introduce silently: invalid
JSON, a cluster/signal key on an entry that doesn't exist in the taxonomy
(scripts.js only console.warns on an unknown signal key and doesn't check
cluster keys at all), a duplicate entry id, or meta.totalEntries drifting
from the actual entry count (CLAUDE.md's Step 6 keeps these in sync by hand).
"""
import json
import sys

PATH = "docs/data/jobs.json"
errors = []


def error(msg):
    errors.append(msg)
    print(f"::error::{msg}")


try:
    with open(PATH, encoding="utf-8") as f:
        raw = f.read()
    data = json.loads(raw)
except json.JSONDecodeError as e:
    print(f"::error::{PATH} is not valid JSON: {e}")
    sys.exit(1)

for key in ("meta", "entries", "clusters", "signals"):
    if key not in data:
        error(f"Missing top-level key: {key!r}")

if errors:
    sys.exit(1)

entries = data["entries"]
clusters = data["clusters"]
signals = data["signals"]

if not isinstance(entries, list):
    error("'entries' is not a list")
if not isinstance(clusters, dict):
    error("'clusters' is not an object")
if not isinstance(signals, dict):
    error("'signals' is not an object")

if errors:
    sys.exit(1)

for group_name, group in (("clusters", clusters), ("signals", signals)):
    for key, val in group.items():
        if not isinstance(val, dict) or not val.get("label") or not val.get("description"):
            error(f"{group_name}.{key} is missing a non-empty 'label' or 'description'")

total_entries = data.get("meta", {}).get("totalEntries")
if total_entries != len(entries):
    error(
        f"meta.totalEntries ({total_entries!r}) does not match the actual "
        f"entry count ({len(entries)}) — update meta.totalEntries"
    )

seen_ids = {}
for i, entry in enumerate(entries):
    label = entry.get("id") or f"entries[{i}]"

    for field in ("id", "company", "title", "clusters", "signals"):
        if field not in entry:
            error(f"{label}: missing required field {field!r}")

    entry_id = entry.get("id")
    if entry_id:
        if entry_id in seen_ids:
            error(f"Duplicate entry id {entry_id!r} (also at index {seen_ids[entry_id]})")
        else:
            seen_ids[entry_id] = i

    for key in entry.get("clusters") or []:
        if key not in clusters:
            error(f"{label}: references unknown cluster key {key!r}")
    for key in entry.get("signals") or []:
        if key not in signals:
            error(f"{label}: references unknown signal key {key!r}")

if errors:
    print(f"\n{len(errors)} problem(s) found in {PATH}.")
    sys.exit(1)

print(
    f"OK: {PATH} valid — {len(entries)} entries, {len(clusters)} clusters, "
    f"{len(signals)} signals, all references resolve."
)
