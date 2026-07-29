# Repository Guidelines

## Project Structure & Module Organization

This is a Python workspace organized around active modules, practice code, and archived scripts. Core reusable modules live in `src/` and have repo-level tests in `tests/`. `practice/algorithms/` contains standalone exercises, while `practice/leetcode/` stores LeetCode solutions in hundred-bucket packages such as `solutions_00000/solution_00001.py`. `technical_assessments/` holds interview and assessment problems. `projects/reporter/` is a self-contained server health reporter with its own package, test, README, and `run.sh`. `archive/` is historical reference code and is excluded from normal test runs.

## Build, Test, and Development Commands

- `python -m pip install -e .[dev]`: install the workspace plus development tools.
- `python -m pytest`: run the configured test suite from `pyproject.toml`.
- `python -m pytest tests/test_lcs.py`: run one focused test file.
- `python -m pip install -e .[reporter]`: install the `requests` dependency needed by the reporter project.
- `git config core.hooksPath .githooks`: enable the tracked pre-commit hook, which runs tests and pylint checks on newly staged Python files.

## Coding Style & Naming Conventions

Use Python 3.10+ syntax and follow the existing straightforward module style. Indent with four spaces, prefer clear function names, and keep algorithm solutions self-contained. Name tests `test_*.py`. Name LeetCode files `solution_<five_digit_problem_id>.py`, grouped under the matching `practice/leetcode/solutions_<hundred_bucket>/` package. Avoid introducing dependencies unless they belong in `pyproject.toml` optional extras.

## Testing Guidelines

The project uses `pytest`, with discovery configured for `tests/`, `projects/reporter/test_status_reporter.py`, `practice/algorithms`, `technical_assessments`, and `practice/leetcode`. Add or update tests with behavior changes. For LeetCode additions, include a small `unittest` case in the same solution file, matching the repository's existing pattern. Keep `archive/` out of active test expectations.

## Commit & Pull Request Guidelines

Recent commits use short imperative titles such as `Add optimized diagonal traverse solution`, `Refactor binary tree right side view`, and `Handle zero-capacity LRU cache`, often followed by a PR number. Keep commits focused and describe the changed behavior, not the implementation mechanics. Pull requests should include a concise summary, test results such as `python -m pytest`, linked issues when applicable, and screenshots only for UI-facing changes.

## Security & Configuration Tips

Do not commit local virtual environments, generated `__pycache__/` files, credentials, or real endpoint lists. Reporter runs that target real services should keep environment-specific configuration outside committed source files.
