# Selection Sort — How it Works & How to Visualize It

## Plain-English Explanation

1. You divide the array into two parts:
   - Left side = sorted portion (starts empty).
   - Right side = unsorted portion.

2. For each index `i` from `0` to `n-1`:
   - Assume the minimum element is at `minIndex = i`.
   - Scan the rest of the array (`j = i+1 .. n-1`) to find the real minimum.
   - Each time you compare `arr[j]` with `arr[minIndex]`, update `minIndex` if smaller is found.
   - After scanning, **swap** `arr[i]` and `arr[minIndex]`.
   - Now the prefix `[0..i]` is sorted.

---

## Pseudocode

```text
selection_sort(A):
    for i from 0 to n-1:
        minIndex = i
        for j from i+1 to n-1:
            if A[j] < A[minIndex]:
                minIndex = j
        swap A[i] and A[minIndex]
```

---

## Visual Mapping (Colors)

- **current** (Purple `#7209B7`): the current outer loop index `i` (where the next min will be placed).
- **comparing** (Pink `#A23B72`): the element `arr[j]` currently being compared to the current minimum.
- **swapping** (Orange `#F18F01`): when you swap `arr[i]` with `arr[minIndex]`.
- **sorted** (Red `#C73E1D`): after finishing index `i`, mark it as sorted.
- **default** (Blue `#2E86AB`): everything else.
- **background** (Light gray `#F8F9FA`).

---

## Walkthrough (Example Array: `[7, 3, 5, 2]`)

**Start:** `[7, 3, 5, 2]`

### Pass i = 0
- Mark index `0` (`7`) as `current` (purple).
- Compare with `j=1` (`3`) → `comparing`. `3 < 7`, update `minIndex=1`.
- Compare with `j=2` (`5`) → `comparing`. `5 > 3`, no update.
- Compare with `j=3` (`2`) → `comparing`. `2 < 3`, update `minIndex=3`.
- Swap `arr[0]` and `arr[3]` (orange highlight on `0` and `3`).
- Array becomes `[2, 3, 5, 7]`.
- Mark index `0` as `sorted` (red).

### Pass i = 1
- `current` at index `1` (`3`).
- Compare with `j=2` (`5`): `comparing`. `5 > 3`, no update.
- Compare with `j=3` (`7`): `comparing`. `7 > 3`, no update.
- No swap needed.
- Mark index `1` as `sorted`.

### Pass i = 2
- `current` at index `2` (`5`).
- Compare with `j=3` (`7`): `comparing`. `7 > 5`, no update.
- No swap needed.
- Mark index `2` as `sorted`.

### Pass i = 3
- `current` at index `3` (`7`).
- Nothing left to compare.
- Mark index `3` as `sorted`.

**Final array:** `[2, 3, 5, 7]` — all red.

---

## High-Level Visual Timeline

For each outer loop `i`:

1. Highlight `i` as **current**.
2. For each `j = i+1..n-1`:
   - Highlight `j` as **comparing**.
   - If `arr[j] < arr[minIndex]`, update `minIndex`.
3. After inner loop:
   - Highlight `i` and `minIndex` as **swapping**.
   - Swap their values.
4. Mark index `i` as **sorted**.
5. Continue until done.
