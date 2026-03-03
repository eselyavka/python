# Remove Candidates

This file is a historical cleanup note.
It lists optional deletion candidates that remain archived, plus the files already removed in the first cleanup pass.

## Removed In First Cleanup Pass

These paths are listed for historical context only. They are no longer present in the repository.

- `archive/skeleton.py`
- `archive/python_threading.py`
- `archive/lre.py`
- `archive/db_decorator.py`
- `archive/learning_python.py`
- `archive/part5.py`
- `archive/legacy_ops/hadoop/hbase_migrate_legacy.py`

Reason:
- These were the strongest deletion candidates.
- They had little practical or educational value, or were direct duplicates.

## Remove If You Do Not Intend To Preserve Legacy Ops History

- `archive/legacy_ops/hadoop/compaction.py`
- `archive/legacy_ops/hadoop/get_data.py`
- `archive/legacy_ops/hadoop/get_job_json.py`
- `archive/legacy_ops/hadoop/mapper.py`
- `archive/legacy_ops/hadoop/reducer.py`

Reason:
- Old Hadoop/HBase scripts tied to a specific environment.
- No tests and no current repo integration.

- `archive/legacy_ops/integration/log4j_parser.py`
- `archive/legacy_ops/integration/log_cleaner.py`
- `archive/legacy_ops/integration/read_keys.py`
- `archive/legacy_ops/integration/send_sms.py`
- `archive/legacy_ops/integration/soap_send.py`
- `archive/legacy_ops/integration/test_avro.py`

Reason:
- Environment-specific integration scripts.
- Retained only as historical artifacts.

- `archive/legacy_ops/postgres/calculate_trx.py`
- `archive/legacy_ops/postgres/check_backup.py`
- `archive/legacy_ops/postgres/check_idx_bloat.py`

Reason:
- Large operational scripts with heavy environment assumptions.
- No evidence they are still part of a maintained workflow here.

## Borderline Candidates

- `technical_assessments/tt.py`
  Reason: interactive tic-tac-toe script, no tests, low assessment/reference value.

- `technical_assessments/yandex.py`
  Reason: mixed task snippets rather than a cohesive, tested solution file.

- `practice/algorithms/bst.py`
  Reason: educational, but minimal and untested.

- `practice/algorithms/permutation_string.py`
  Reason: educational CLI exercise, limited reuse.

- `practice/algorithms/fact.py`
  Reason: mostly benchmarking/demo material, but still reasonable to keep as a language exercise.

These are not strong deletion candidates. Remove them only if the goal is to aggressively trim the repository.

## Not Recommended For Removal

Do not remove these in the first cleanup pass:

- `src/`
- `tests/`
- `projects/reporter/`
- `technical_assessments/`
- `practice/algorithms/` files with passing embedded tests
- `practice/leetcode/` unless you explicitly want to drop the large practice archive
