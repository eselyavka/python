# Python Workspace

This repository is now organized into a few clear areas:

- `src/`: active Python 3 modules with repo-level tests
- `tests/`: unit tests for `src/`
- `projects/`: self-contained subprojects
- `practice/`: algorithm and interview-style exercises
- `archive/`: archived scripts and reference files kept for reference

## Active Modules

The actively maintained root modules live under `src/`:

- `src/decorator_examples.py`
- `src/is_word_palindrome.py`
- `src/lcs.py`
- `src/mymod.py`
- `src/rabin_karp.py`
- `src/rps_sliding_window.py`
- `src/sparse_vector.py`

## Technical Assessments

- `technical_assessments/`: standalone assessment/problem files

## Projects

- `projects/reporter/`: server health aggregation tool, updated for Python 3 packaging and tests

## Practice

- `practice/algorithms/`: standalone coding exercises
- `practice/leetcode/`: LeetCode solutions archive

## Archive

- `archive/`: archived scripts and reference files kept outside the active code paths
- `archive/legacy_ops/`: older infra-specific scripts preserved for historical context

`archive/legacy_ops` remains importable for reference and manual use, but it is not part of the actively tested surface of the repository.

## Development

Run the repo-level tests:

```bash
python3 -m pytest
```

Git commits use the tracked hook in `.githooks/pre-commit`.
It runs `pytest` for the full repo and `pylint` for newly added staged Python files.
By default the hook uses `~/.venv/py3_11/bin/python`; override with `PYTHON_BIN=/path/to/python` if needed.
Enable it in a fresh clone with:

```bash
git config core.hooksPath .githooks
```

If you want to run the reporter project against real HTTP endpoints, install `requests` first.

## AVRO Script

To run `archive/legacy_ops/integration/test_avro.py`, install the AVRO extra:

```bash
python3 -m pip install .[avro]
python3 archive/legacy_ops/integration/test_avro.py
```

If you also want `--send`, install the Flume logger dependency too:

```bash
python3 -m pip install .[avro,avro-send]
python3 archive/legacy_ops/integration/test_avro.py --send
```

`--send` expects a Flume endpoint on `localhost:6666`. The script reads `log.avsc` and `part-00000.avro` from its own directory.
