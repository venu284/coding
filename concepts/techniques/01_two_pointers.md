# Two Pointers

## Quick Revision

- **When to use it:** sorted pairs/triples, palindrome, in-place array work.
- **Core idea:** two indices eliminate impossible candidates.
- **Complexity:** O(n), or O(n log n) if sorting first.
- **Template:** `two_sum_sorted`.
- **Common trap:** duplicate handling in tuple problems.

## Mental Model

Two pointers work when moving one pointer has a predictable effect. In sorted
arrays, moving left right increases the sum; moving right left decreases it.

## How It Works

Start pointers at meaningful boundaries. Compare current state, then move the
pointer that can make progress toward the target.

## Python Template

```python
left, right = 0, len(nums) - 1
while left < right:
    total = nums[left] + nums[right]
```

See `two_sum_sorted` in `../03_template_bank.py`.

## Walkthrough

For Two Sum II, if the sum is too small, only increasing `left` can help. If it
is too large, only decreasing `right` can help.

## Edge Cases

- Duplicates.
- Negative values.
- Empty or one-item input.
- Need original indices after sorting.

## Common Mistakes

- Sorting when original indices are required.
- Not skipping duplicate triples in 3Sum.
- Moving both pointers blindly.

## Practice

- **Anchor problems:** 3Sum, Valid Palindrome.
- **Extra problems:** Container With Most Water, Two Sum II.
- **Interview prompt:** "Which pointer movement eliminates candidates safely?"

## Related Concepts

- `../data-structures/01_arrays_and_strings.md`
- `../algorithms/01_sorting.md`
