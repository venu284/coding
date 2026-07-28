# Binary Search

## Quick Revision

- **When to use it:** sorted data, monotonic answer, O(log n) requirement.
- **Core idea:** each comparison discards half the search space.
- **Complexity:** O(log n), or O(log range * check cost) for answer search.
- **Template:** `binary_search_left`, `search_on_answer`.
- **Common trap:** mixing inclusive and half-open bounds.

## Mental Model

Binary search is about monotonic truth. Find the first position where a predicate
becomes true, or the exact target in sorted space.

## How It Works

For lower bound, maintain `[lo, hi)` as the candidate region. If mid is too small,
the answer is right of mid. Otherwise mid remains a candidate.

## Python Template

```python
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

For Search Insert Position, lower bound returns the first index whose value is at
least target. That is also where target should be inserted.

## Edge Cases

- Empty array.
- Target before first or after last.
- Duplicate values.
- Rotated sorted arrays need side detection.

## Common Mistakes

- Infinite loop from not moving bounds.
- Returning mid after loop without proving it.
- Predicate not monotonic in answer search.

## Practice

- **Anchor problems:** Search in Rotated Sorted Array, Koko Eating Bananas.
- **Extra problems:** Find Minimum in Rotated Sorted Array, Search a 2D Matrix.
- **Interview prompt:** "What is monotonic?"

## Related Concepts

- `../foundations/03_iteration_and_invariants.md`
- `../techniques/09_search_on_answer.md`
