# Divide And Conquer

## Quick Revision

- **When to use it:** split into independent subproblems and combine.
- **Core idea:** solve halves recursively.
- **Complexity:** often O(n log n).
- **Template:** `merge_sort`.
- **Common trap:** bad base case or expensive combine step.

## Mental Model

Divide and conquer is useful when each part can be solved without knowing the
other part, then merged into a full answer.

## How It Works

1. Base case for small input.
2. Split input.
3. Recurse on each part.
4. Combine results.

## Python Template

```python
if len(nums) <= 1:
    return nums
mid = len(nums) // 2
left = solve(nums[:mid])
right = solve(nums[mid:])
return combine(left, right)
```

See `merge_sort` in `../03_template_bank.py`.

## Walkthrough

Merge sort splits the array until single elements, then merges sorted halves.

## Edge Cases

- Empty input.
- One item.
- Odd length split.
- Combine step preserving stability.

## Common Mistakes

- No progress toward base case.
- Excessive slicing in performance-sensitive code.
- Combining in O(n^2) accidentally.

## Practice

- **Anchor problems:** Sort an Array, Merge K Sorted Lists.
- **Extra problems:** Kth Largest Element, Maximum Subarray divide-and-conquer.
- **Interview prompt:** "Can the halves be solved independently?"

## Related Concepts

- `../algorithms/01_sorting.md`
- `../foundations/02_recursion.md`
