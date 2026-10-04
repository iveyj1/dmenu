# dmenu maintenance

Keep tracked `config.h` and `config.def.h` synchronized for configuration changes.

## Change-size history (required)

After every modification run `python3 scripts/update_cloc_by_commit.py`.
`scripts/cloc_by_commit.md` is generated locally and gitignored; never stage it. Regenerate after committing or changing
branches to replace WORKTREE with the actual commit row. Do not create commits
without the user's request just to refresh the report.

Check freshness with `python3 scripts/update_cloc_by_commit.py --check`. Test
reporting changes with `python3 scripts/test_cloc_history.py`.

In the final response report latest runtime C and runtime-script totals and net
deltas; include support C/scripts/build deltas when nonzero. Explicitly report zero
measured change for documentation/reporting-only changes.

Maintain the fixed fork baseline and scope in `scripts/cloc-history.json`.
Add reviewed descriptions for unclear commit subjects; new commits otherwise use
their subjects. Keep runtime/support categories and the single effective config
header policy consistent. WORKTREE counts staged/unstaged and nonignored new
files; never attribute those changes to an existing commit.
