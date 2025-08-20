# Sorting Algorithms Testing Project

A minimal framework to choose, run, and validate sorting algorithms.

## Project Structure
```
sorting/
├── sorting_algorithms/
│   ├── __init__.py          # ALGORITHMS mapping
│   ├── bubble_sort.py       # def bubble_sort(arr: list) -> list: pass
│   ├── merge_sort.py        # def merge_sort(arr: list) -> list: pass
│   └── quick_sort.py        # def quick_sort(arr: list) -> list: pass
├── tests/
│   └── test_sorting.py      # pytest parametrized tests
├── main.py                  # CLI with exact contract
├── requirements.txt         # pytest
└── README.md               # usage + Definition of Done
```

## Usage

### Non-interactive mode (preferred)

**Flags**
- `--algo {bubble,merge,quick}` (required)
- Exactly one of:
  - `--input "3,1,4,1,5"` (comma-separated integers; spaces optional)
  - `--dataset {sorted,reverse,duplicates,empty,random,single,negatives}`
- Optional: `--validate` (compare algorithm output vs `sorted()` and print status)

**Examples**
```bash
# Test bubble sort with explicit input
python main.py --algo bubble --input "3,1,4,1,5" --validate

# Test quick sort with predefined dataset
python main.py --algo quick --dataset duplicates --validate

# Test merge sort without validation
python main.py --algo merge --dataset random
```

### Interactive mode (fallback if no flags passed)
```bash
python main.py
```
- Choose algorithm: 1) Bubble 2) Merge 3) Quick
- Enter either comma-separated list or dataset name

## Datasets
- `sorted`: `[1, 2, 3, 4, 5]`
- `reverse`: `[5, 4, 3, 2, 1]`
- `duplicates`: `[2, 3, 2, 1, 3, 1]` → expected sort: `[1, 1, 2, 2, 3, 3]`
- `empty`: `[]`
- `random`: `[7, 1, 4, 9, 2]` (fixed for determinism)
- `single`: `[42]`
- `negatives`: `[0, -1, 5, -3, 2]`

## File-by-File Tasks

### `sorting_algorithms/__init__.py`
- Imports the three functions and exposes:
  ```python
  ALGORITHMS = {
      "bubble": bubble_sort,
      "merge": merge_sort,
      "quick": quick_sort,
  }
  ```

### `bubble_sort.py`, `merge_sort.py`, `quick_sort.py`
- Each file defines exactly one function with signature:
  ```python
  def bubble_sort(arr: list) -> list: ...
  def merge_sort(arr: list) -> list: ...
  def quick_sort(arr: list) -> list: ...
  ```
- Leave bodies empty initially (e.g., `pass`) and include a brief docstring.

### `main.py`
- Uses `argparse` for flags.
- Implements dataset resolution & `--input` parsing (integers only).
- Looks up callable from `ALGORITHMS`; calls it with a **copy** of the list.
- Prints `ALGO`, `INPUT`, `OUTPUT`, `EXPECTED` exactly as labeled above.
- Handles `--validate` and exit codes as specified.
- If no flags → runs the interactive flow.

### `requirements.txt`
- Includes `pytest` only.

### `tests/test_sorting.py`
- Uses `pytest` parametrization across algorithms and datasets.
- Compares algorithm output to `sorted()` for each dataset.
- Tests will naturally FAIL until you implement algorithms (expected for Stage A).

## Definition of Done (Acceptance Tests)

### Stage A (wiring only) — with stubs unimplemented:
The following commands must produce the exact print pattern and exit codes (validation FAIL is expected).

1) Non-interactive with explicit input
```bash
python main.py --algo bubble --input "3,1,4,1,5" --validate
# Expected lines (order exact):
# ALGO: bubble
# INPUT: [3, 1, 4, 1, 5]
# OUTPUT: None
# EXPECTED: [1, 1, 3, 4, 5]
# VALIDATION: FAIL
# Exit code: 1
```

2) Non-interactive with dataset
```bash
python main.py --algo quick --dataset duplicates --validate
# Expected:
# ALGO: quick
# INPUT: [2, 3, 2, 1, 3, 1]
# OUTPUT: None
# EXPECTED: [1, 1, 2, 2, 3, 3]
# VALIDATION: FAIL
# Exit code: 1
```

3) Interactive (manual simulation)
- Run `python main.py` → choose Quick → enter `5,3,9,0`
- Expected lines:
  ```
  ALGO: quick
  INPUT: [5, 3, 9, 0]
  OUTPUT: None
  EXPECTED: [0, 3, 5, 9]
  VALIDATION: FAIL
  ```
- Exit code: 1

4) Pytest discovery
```bash
pytest -q
# Expected: tests are collected successfully (failures are OK in Stage A)
```

### Stage B (after implementing algorithms) — the same commands should then produce:
- `OUTPUT` equal to `EXPECTED`
- `VALIDATION: OK`
- Exit code: 0

## Testing
```bash
# Run all tests
pytest tests/ -v

# Quick test discovery
pytest -q

# Run specific test file
pytest tests/test_sorting.py -v
```

## Dependencies
- pytest (see requirements.txt)

## Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Verify installation
pytest --version
```

## Goals
- Provide a minimal framework to **choose**, **run**, and **validate** sorting algorithms.
- Each algorithm lives in its own module as an **empty stub** to start.
- `main.py` MUST execute the selected algorithm on provided input and report correctness against Python's built-in `sorted()`.

## Non-Goals
- No GUIs.
- No dependencies beyond `pytest`.
- No benchmarking in this iteration. 