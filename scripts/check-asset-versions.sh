#!/usr/bin/env bash
# Fails if docs/js/scripts.js or docs/css/styles.css changed more recently
# than the matching ?v= cache-bust string was last bumped in docs/index.html.
# See the "Site code" section of CLAUDE.md for why this exists — it has
# already shipped silently-stale assets twice.
set -euo pipefail

check() {
  local asset_path="$1"
  local grep_pattern="$2"
  local name="$3"

  local asset_commit asset_time bump_commit bump_time
  asset_commit=$(git log -1 --format='%H' -- "$asset_path")
  asset_time=$(git log -1 --format='%ct' -- "$asset_path")
  bump_commit=$(git log -G"$grep_pattern" -1 --format='%H' -- docs/index.html || true)
  bump_time=$(git log -G"$grep_pattern" -1 --format='%ct' -- docs/index.html || true)

  if [ -z "$asset_commit" ]; then
    echo "SKIP: $asset_path has no history yet."
    return 0
  fi

  if [ -z "$bump_commit" ]; then
    echo "::error::No commit found bumping ${name}'s ?v= string in docs/index.html, but $asset_path has history. Add a version query string and bump it."
    exit 1
  fi

  if [ "$asset_time" -gt "$bump_time" ]; then
    echo "::error::$asset_path changed in $asset_commit (after commit $bump_commit last bumped its ?v= in docs/index.html). Bump the ${name}?v= number in the same commit as the change."
    exit 1
  fi

  echo "OK: $name in sync (asset last changed $asset_commit, version last bumped $bump_commit)"
}

check docs/js/scripts.js 'scripts\.js\?v=' 'scripts.js'
check docs/css/styles.css 'styles\.css\?v=' 'styles.css'
