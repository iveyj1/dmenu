# dmenu: changes and cloc since the fork

Committed history through `c4df2fc0ede081af8aa48757a9d62a4f34a25cb2`; cloc **2.10**.

## Provenance and method

- Upstream: https://git.suckless.org/dmenu.
- Original fork baseline: `7175c4880bac3d2a2d4a6262b59193f0a38e2fdb`.
- Upstream HEAD verified during this review: `61e0072c3e6adfc67bafbc84e376cf26bc3680c0`.
- Baseline verified as the upstream/local merge-base. -ob/-of outline colors were inherited upstream, not added by this fork.
- Main tables follow first-parent history, oldest first; dates are author dates. Merge rows include their complete first-parent delta, including conflict resolutions. Side commits are detailed separately, not added again to totals.
- C = runtime .c/.h files; one effective configuration header (tracked config.h/blocks.h, otherwise its .def.h template). Support C = test/diagnostic C sources. Runtime scripts are counted separately from build/test/update scripts.
- cloc code lines exclude blanks/comments. Deltas are signed net changes vs the preceding row, not diff insertion/deletion counts. Zero does not imply no behavior change. Embedded shell strings in C count as C; shell help heredocs follow cloc classification.
- Build = Makefile/config.mk. Docs, terminfo, binaries, images, generated buildinfo.h, unused configuration templates, and reporting files under scripts/ are excluded. --skip-uniqueness prevents duplicate-file suppression.
- Historical counts use Git blobs. WORKTREE, when present, includes staged/unstaged changes and nonignored untracked regular files; delta is vs HEAD, never folded into committed history. Report-only edits do not create a WORKTREE row.
- Requires Python 3.9+, Git and cloc. Regenerate: `python3 scripts/update_cloc_by_commit.py`. Validate freshness: `python3 scripts/update_cloc_by_commit.py --check`.
- Regeneration is offline: upstream provenance records the review-time verification, not a fresh network check.
- Add reviewed descriptions to scripts/cloc-history.json when a commit subject is unclear. Otherwise new commits automatically use their subjects. Keep baseline fixed; do not move it to a later upstream merge-base.

## Runtime changes

| Commit | Date | C code | Δ C | Script code | Δ scripts | Change |
|---|---|---:|---:|---:|---:|---|
| `7175c48` | 2026-01-28 | 1307 | — | 12 | — | Upstream dmenu 5.4 plus upstream fixes; fork baseline. |
| `50644ca` | 2026-06-22 | 1307 | 0 | 12 | 0 | Default launcher to 10 vertical rows; track config.h with font size 14; add build-artifact ignores. |
| `5d2dc6c` | 2026-07-19 | 1321 | +14 | 12 | 0 | Add -c centered placement (900px width cap, Xinerama and fallback); font 14 → 24. |
| `afcf736` | 2026-08-10 | 1321 | 0 | 12 | 0 | Font 24 → 16; synchronize config.def.h; add b build/optional-install script. |
| `6437bf6` | 2026-08-31 | 1322 | +1 | 12 | 0 | Document local build/options; correct CLI usage for -c and existing -ob/-of options. |
| `88bd9e7` | 2026-09-04 | 1322 | 0 | 12 | 0 | Reduce font 16 → 13 in both configuration headers. |
| `02cad08` | 2026-09-13 | 1322 | 0 | 12 | 0 | Document Mint/Void build dependencies; no executable changes. |
| `821c86b` | 2026-09-13 | 1322 | 0 | 24 | +12 | Add dmenu-font Xresources wrapper and launcher fallback; font 13 → 11; install wrapper, add font tests and make check. |
| `c4df2fc` | 2026-09-22 | 1331 | +9 | 24 | 0 | Add -s smart-case search; document option. |
| `WORKTREE` | uncommitted | 1335 | +4 | 24 | 0 | Pending changes vs HEAD: AGENTS.md, README, dmenu.c, scripts/cloc-history.json, scripts/test_cloc_history.py, scripts/update_cloc_by_commit.py |

## Supporting code and build files

| Commit | Support C | Δ C | Support scripts | Δ scripts | Build | Δ build | Combined code | Δ combined |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `7175c48` | 0 | — | 0 | — | 58 | — | 1377 | — |
| `50644ca` | 0 | 0 | 0 | 0 | 58 | 0 | 1377 | 0 |
| `5d2dc6c` | 0 | 0 | 0 | 0 | 58 | 0 | 1391 | +14 |
| `afcf736` | 0 | 0 | 7 | +7 | 58 | 0 | 1398 | +7 |
| `6437bf6` | 0 | 0 | 7 | 0 | 58 | 0 | 1399 | +1 |
| `88bd9e7` | 0 | 0 | 7 | 0 | 58 | 0 | 1399 | 0 |
| `02cad08` | 0 | 0 | 7 | 0 | 58 | 0 | 1399 | 0 |
| `821c86b` | 0 | 0 | 48 | +41 | 64 | +6 | 1458 | +59 |
| `c4df2fc` | 0 | 0 | 48 | 0 | 64 | 0 | 1467 | +9 |
| `WORKTREE` | 0 | 0 | 48 | 0 | 64 | 0 | 1471 | +4 |

Combined includes all five counted categories; excluded files remain excluded.

## Baseline → committed HEAD totals

| Category | Code baseline → HEAD (net) | Blank baseline → HEAD | Comment baseline → HEAD |
|---|---:|---:|---:|
| C | 1307 → 1331 (+24) | 172 → 172 | 78 → 78 |
| Runtime scripts | 12 → 24 (+12) | 3 → 3 | 0 → 2 |
| Support C | 0 → 0 (0) | 0 → 0 | 0 → 0 |
| Support scripts | 0 → 48 (+48) | 0 → 11 | 0 → 1 |
| Build | 58 → 64 (+6) | 20 → 21 | 12 → 12 |

## Commits integrated by merges

Counts below are each side commit’s snapshot and delta vs its own first parent. These are **not additive** with the main tables.

No post-fork merges.

## Files counted at committed HEAD

- **C:** `arg.h`, `config.h`, `dmenu.c`, `drw.c`, `drw.h`, `stest.c`, `util.c`, `util.h`.
- **Runtime scripts:** `dmenu-font`, `dmenu_path`, `dmenu_run`.
- **Support C:** (none).
- **Support scripts:** `b`, `tests/font.py`.
- **Build:** `Makefile`, `config.mk`.

## Latest change

WORKTREE — Pending changes vs HEAD: AGENTS.md, README, dmenu.c, scripts/cloc-history.json, scripts/test_cloc_history.py, scripts/update_cloc_by_commit.py
C: 1335 (+4); Runtime scripts: 24 (0); Support C: 0 (0); Support scripts: 48 (0); Build: 64 (0)

Maintenance: regenerate after each modification and again after committing (or switching branches); include the latest code/script totals and net deltas in the change summary. Reporting-only changes legitimately have zero measured delta.
