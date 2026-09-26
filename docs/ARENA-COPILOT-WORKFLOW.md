# 🤖 Arena + Copilot co-working playbook

How to use **Muse** (in your IDE) and **Arena Agent Mode** (here)
together to grow fast without burning out.

## Who does what

| Task | Copilot | Arena |
|------|---------|-------|
| Autocomplete lines / functions while you type | ✅ | — |
| Explain / refactor a highlighted block | ✅ | — |
| Multi-file feature across the repo | — | ✅ |
| Create README, CI, templates, docs | — | ✅ |
| Run `flutter analyze`, `pytest`, fix failures | — | ✅ |
| Open branches, PRs, issues | — | ✅ |
| Daily mini-project scaffolds with tests | — | ✅ |
| Final review, merge, release | 👤 you | 👤 you |

**Golden rule:** Copilot helps you *type*, Arena helps you *ship*,
you *decide and merge*.

## The daily 15-minute loop (freelance edition)

1. **Pick** one micro-task from [`ROADMAP.md`](../ROADMAP.md) (1 min).
   Keep it shippable in one PR — clients trust steady progress.
2. **Prompt Arena**, e.g. (1 min):
   - *"Day 9: add a monthly budget progress bar to the regular dashboard
     with a widget test. Follow CONTRIBUTING.md."*
   - *"Day 16: scaffold projects/day-02-budget-calculator (Dart CLI)
     with README + tests + CI wired."*
3. **Review the diff** in your IDE with Copilot Chat asking
   *"explain this diff / find bugs"* (8 min).
4. **Merge the PR** → commit lands on `main` under your name → green square,
   and only for *real* work (4 min).
5. **Log it** in `ROADMAP.md` daily log (1 min).

## Prompts that work well

- *"Fix CI failure in flutter analyze; show the error and the fix."*
- *"Add feature X with tests; keep the PR under ~200 lines."*
- *"Refactor file Y for readability; no behavior change."*
- *"Write docs for Z as if for a first-time contributor."*

## How contributions actually count

- Commits on your session branch are authored as you
  (`user.name = Shivam1504-has`), but they only appear on your graph
  **after the PR is merged to `main`** (the default branch).
- Also counted: merged PRs, opened issues/PRs, code reviews.
- Bot-authored commits (e.g. `arena-ai-coding-agent[bot]`, GitHub Actions
  `github-actions[bot]`) do **not** raise *your* graph — that's why **you**
  merge, and why we keep automation to CI rather than fake daily commits.

## ⛔ Don'ts

- Don't mass-create empty repos (10 polished > 50 empty).
- Don't commit `node_modules/`, build output, or secrets.
- Don't game the graph with meaningless commits — maintainers and
  recruiters spot it instantly, and it can violate ToS if automated abusively.
- Don't let CI stay red. Fix it the same day.
