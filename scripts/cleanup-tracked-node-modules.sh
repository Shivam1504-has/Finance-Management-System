#!/usr/bin/env bash
# Day-2 task: stop tracking firebase/node_modules (199MB / ~15k files).
# .gitignore already ignores it for the future; this removes it from git's index.
# Safe: your local files on disk are NOT deleted (--cached only).
set -euo pipefail

cd "$(dirname "$0")/.."

echo "==> Untracking firebase/node_modules (keeps files on disk)..."
git rm -r --cached firebase/node_modules

echo "==> Verifying nothing else unexpected is staged..."
git status --short | head -n 20

echo ""
echo "Next steps:"
echo "  1. Review: git status"
echo "  2. Commit: git commit -m 'chore: untrack firebase/node_modules, rely on npm ci'"
echo "  3. Push + open PR, then merge to main."
echo ""
echo "Note: old history still contains those files (clone stays big until"
echo "history is rewritten with filter-repo/BFG — optional, ask Arena for help)."
