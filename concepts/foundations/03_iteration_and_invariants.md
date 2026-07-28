# Iteration And Invariants

## Quick Revision

- **When to use it:** binary search, two pointers, sliding window, greedy scans.
- **Core idea:** keep a statement true through every loop iteration.
- **Complexity:** normally O(number of iterations).
- **Template:** initialize invariant -> maintain invariant -> use termination.
- **Common trap:** moving a pointer without knowing what the pointer means.

## Mental Model

An invariant is the reason a loop is correct. For binary search, it might be:
"the answer is always inside `[lo, hi)`." Every update must preserve that sentence.

## How It Works

Before coding a loop, define:

1. What each variable means.
2. What remains true before and after each iteration.
3. Why the loop must terminate.
4. What the final variable means.

## Python Template

```python
def lower_bound(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

See `binary_search_left` in `../03_template_bank.py`.

## Walkthrough

In lower bound, all indices before `lo` are known to be too small. All indices at
or after `hi` are candidates or beyond the array. When the loop ends, `lo == hi`,
so that position is the first valid candidate.

## Edge Cases

- Empty array.
- Target smaller than all values.
- Target larger than all values.
- Duplicate values.

## Common Mistakes

- Mixing inclusive and half-open bounds.
- Using `while lo <= hi` with half-open updates.
- Not proving the loop shrinks.

## Practice

- **Anchor problems:** Binary Search, Search Insert Position.
- **Extra problems:** Search in Rotated Sorted Array, Koko Eating Bananas.
- **Interview prompt:** "What invariant does your loop maintain?"

## Related Concepts

- `../algorithms/02_binary_search.md`
- `../techniques/01_two_pointers.md`
- `../techniques/02_sliding_window.md`
