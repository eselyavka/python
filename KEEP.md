# Keep

This file is a historical refactor note.
It captures the modules that still have clear educational or practical value after the Python 3 cleanup and repo reorganization.

## Active Code

- `src/decorator_examples.py`
- `src/is_word_palindrome.py`
- `src/lcs.py`
- `src/mymod.py`
- `src/rabin_karp.py`
- `src/rps_sliding_window.py`
- `src/sparse_vector.py`

Reason:
- These are part of the current active module set.
- They are exercised by repo-level tests.
- They are small, understandable reference implementations.

## Project Code

- `projects/reporter/`

Reason:
- It is a cohesive subproject with its own tests and README.

## Practice Material Worth Keeping

- `practice/algorithms/extract_sum_nums_from_string.py`
- `practice/algorithms/fact.py`
- `practice/algorithms/largest_digit_substring_product.py`
- `practice/algorithms/normalize_string.py`
- `practice/algorithms/permutation_string.py`
- `practice/algorithms/same_sum_array.py`
- `practice/algorithms/second_largest_element_in_array.py`
- `practice/algorithms/simple_queue.py`
- `practice/algorithms/split_array_equal_sum.py`
- `practice/algorithms/sum_of_tree_levels.py`
- `practice/algorithms/validate_numbers_in_string.py`
- `practice/algorithms/bst.py`

Reason:
- They are concise algorithm/data-structure exercises.
- Most now run under Python 3 and have embedded tests.
- Even the weaker ones still have educational value as interview practice.

## Technical Assessments

- `technical_assessments/akamai.py`
- `technical_assessments/carta.py`
- `technical_assessments/facebook.py`
- `technical_assessments/geotab.py`
- `technical_assessments/valid_number.py`

Reason:
- These are clearly scoped assessment/reference files.
- Several have embedded tests.
- `geotab.py` is one of the more substantial standalone problem files in the repo.

## Borderline But Reasonable To Keep

- `technical_assessments/tt.py`
- `technical_assessments/yandex.py`
- `practice/algorithms/bst.py`
- `practice/algorithms/permutation_string.py`
- `practice/algorithms/fact.py`

Reason:
- These still have some educational value.
- They are weaker than the files above because they are either untested, loosely scoped, or mostly demo material.
- Keep them unless the goal is to trim the repository aggressively.

## Already Removed

These paths are listed for historical context only. They are no longer present in the repository.

- `archive/skeleton.py`
- `archive/python_threading.py`
- `archive/lre.py`
- `archive/db_decorator.py`
- `archive/learning_python.py`
- `archive/part5.py`
- `archive/legacy_ops/hadoop/hbase_migrate_legacy.py`

Reason:
- These were reviewed and deleted in the first cleanup pass.

## Practice Archive

- `practice/leetcode/`

Reason:
- Large solution archive.
- Useful if the goal is to preserve practice history.
- Not part of active package code, but still valid as a reference set.

## Legacy Ops Worth Keeping Only If Historical Context Matters

- `archive/legacy_ops/postgres/database.py`
- `archive/legacy_ops/postgres/extract_file.py`
- `archive/legacy_ops/postgres/file_operations.py`
- `archive/legacy_ops/postgres/options.py`
- `archive/legacy_ops/postgres/prepare_database.py`
- `archive/legacy_ops/postgres/process_config.py`
- `archive/legacy_ops/hadoop/hbase_migrate.py`
- `archive/legacy_ops/integration/ib_data_generator.py`

Reason:
- These are the few archived files that still form a partial toolchain or have some standalone utility value.
- Keep them only if preserving old operational history is intentional.
