# Sorting Algorithms Testing Project (Authoritative Spec)

> Follow this spec exactly. Do not add features or re-plan beyond what is written.
> This spec has two stages of acceptance:
> - **Stage A (wiring only)**: algorithm stubs are empty; all validations should FAIL as expected, but the harness and reporting must work.
> - **Stage B (after implementations)**: same commands should then PASS with exit code 0.

---

## Goals
- Provide a minimal framework to **run** and **validate** sorting algorithms against a fixed suite of datasets.
- Algorithms live in separate modules as **stubs** initially (empty bodies).
- `main.py` MUST select an algorithm (or all), run the test harness over predefined datasets, and report PASS/FAIL **without printing the arrays themselves**.

---

## Non-Goals
- No arbitrary user-provided arrays or interactive data entry.
- No GUIs.
- No dependencies beyond `pytest` for unit tests.
- No benchmarking in this iteration.

---

## Project Structure
```
sorting/
├── sorting_algorithms/
│   ├── __init__.py
│   ├── bubble_sort.py        # def bubble_sort(arr: list) -> list: pass
│   ├── merge_sort.py         # def merge_sort(arr: list) -> list: pass
│   └── quick_sort.py         # def quick_sort(arr: list) -> list: pass
├── tests/
│   └── test_sorting.py       # correctness tests over datasets (will FAIL until algos implemented)
├── main.py                   # CLI harness: selects algo(s), runs datasets, reports PASS/FAIL
├── requirements.txt          # pytest
└── README.md                 # usage + examples (from this spec)
```

---

## Datasets (exact values; not to be printed by the CLI)
- `sorted`: `[1, 2, 3, 4, 5]`
- `reverse`: `[5, 4, 3, 2, 1]`
- `duplicates`: `[2, 3, 2, 1, 3, 1]` → expected sort: `[1, 1, 2, 2, 3, 3]`
- `empty`: `[]`
- `random`: `[7, 1, 4, 9, 2]` (fixed for determinism)
- `single`: `[42]`
- `negatives`: `[0, -1, 5, -3, 2]`

> Optional extended datasets for pytest (recommended, not required by CLI output):
> - `all_equal`: `[7, 7, 7, 7, 7]`
> - `near_sorted`: `[1, 2, 3, 5, 4, 6, 7]`
> - `mixed_small`: `[-10, 0, 7, -1, 7, 3, -10]`
> - `alternating`: `[1, 100, 2, 99, 3, 98, 4, 97]`
> - `zeros_negs`: `[0, 0, 0, -1, -1, -2, 0, -3]`
> - `gapped`: `[1000, -1000, 500, -500, 0, 250, -250]`
> - `random10_fixed`: `[12, -3, 7, 7, 0, -11, 25, 4, 4, -3]`

---

## CLI Requirements (main.py)

### Overview
`python main.py` MUST run a **non-interactive** harness that executes one chosen algorithm or **all** algorithms over the fixed datasets and reports results **without printing the actual arrays**.

### Flags
- `--algo {bubble,merge,quick,all}` (required)
- `--report {text,json}` (optional; default `text`)
- `--failfast` (optional; stop on first failure; exit immediately with non-zero)

### Behavior
- Resolve the selected algorithm(s) from `ALGORITHMS` (see below).
- For each selected algorithm and each dataset in the order listed above:
  - Call the algorithm with a copy of the dataset.
  - Compare the output to Python’s `sorted(dataset)`.
  - Record PASS/FAIL (boolean), **do not print the arrays**.
- Reporting:
  - `text` report: one line per dataset in the format  
    `ALGO=<name> DATASET=<name> RESULT=<PASS|FAIL>`
  - After all runs, print a summary line per algorithm:  
    `SUMMARY ALGO=<name> PASSED=<n_pass> TOTAL=<n_total>`
- Exit codes:
  - Exit **0** only if **all** checked datasets PASS for all selected algorithms.
  - Exit **1** otherwise (or earlier if `--failfast` triggers).

> No interactive prompts. No input lists. The harness is deterministic.

---

## File-by-File Tasks (do not skip)

### `sorting_algorithms/__init__.py`
- Import the three functions and expose:
  ```python
  from .bubble_sort import bubble_sort
  from .merge_sort import merge_sort
  from .quick_sort import quick_sort

  ALGORITHMS = {
      "bubble": bubble_sort,
      "merge": merge_sort,
      "quick": quick_sort,
  }
  ```

### `bubble_sort.py`, `merge_sort.py`, `quick_sort.py`
- Each file defines exactly one function with signature:
  ```python
  def bubble_sort(arr: list) -> list:
      """Return a new list sorted in non-decreasing order. Stub for now."""
      pass
  ```
  (same pattern for `merge_sort` and `quick_sort`)
- Bodies remain empty in Stage A.

### `main.py`
- Parse flags with `argparse`.
- Build the dataset dictionary internally (per the **Datasets** section).
- Resolve one algorithm or iterate all (if `--algo all`).
- Execute the harness, accumulate results, and print lines as specified under **Behavior**.
- Implement `--report json` to print a single JSON object with keys:
  - `algorithms` → list of objects `{name, results: [{dataset, passed}], summary: {passed, total}}`
  - `status` → `"OK"` or `"FAIL"`
- Set exit codes exactly as specified.

### `requirements.txt`
- Include `pytest` only.

### `tests/test_sorting.py`
- Use `pytest` parametrization across algorithms and datasets.
- Compare algorithm output to `sorted()` for each dataset.
- Tests will FAIL in Stage A until algorithms are implemented.

### `README.md`
- Include CLI examples and the **Definition of Done** commands.

---

## Definition of Done (Acceptance Tests)

> **Stage A (wiring only)** — with algorithm stubs unimplemented:
> The following must run and produce the required lines, with non-zero exit codes.

1) Run one algorithm in text mode
```bash
python main.py --algo bubble --report text
# Expected output (exact format; order of datasets as listed):
# ALGO=bubble DATASET=sorted RESULT=FAIL
# ALGO=bubble DATASET=reverse RESULT=FAIL
# ALGO=bubble DATASET=duplicates RESULT=FAIL
# ALGO=bubble DATASET=empty RESULT=FAIL
# ALGO=bubble DATASET=random RESULT=FAIL
# ALGO=bubble DATASET=single RESULT=FAIL
# ALGO=bubble DATASET=negatives RESULT=FAIL
# SUMMARY ALGO=bubble PASSED=0 TOTAL=7
# Exit code: 1
```

2) Run all algorithms, fail fast
```bash
python main.py --algo all --failfast
# Expected: Print at least the first failure line for the first dataset attempted, then exit code 1.
```

3) JSON report
```bash
python main.py --algo quick --report json
# Expected: Single-line JSON with fields: algorithms, status.
# Exit code: 1
```

4) Pytest collection
```bash
pytest -q
# Expected: tests are collected successfully (failures are OK in Stage A).
```

> **Stage B (after algorithms implemented)** — running the same commands should produce `RESULT=PASS` on every dataset and `Exit code: 0`. The JSON `status` must be `OK`.

---
