# Arrays And Strings

## Quick Revision

- **When to use it:** ordered data, indexed access, contiguous ranges.
- **Core idea:** arrays give O(1) index access; strings are immutable sequences.
- **Complexity:** scan O(n), sort O(n log n), middle insert/delete O(n).
- **Template:** scan, two pointers, prefix sums.
- **Common trap:** slicing copies and can turn O(n) into O(n^2).

## Mental Model

Arrays and strings are the default interview input. Their power is position:
neighbors, ranges, sorted order, and indices usually carry the signal.

## How It Works

Ask whether the problem cares about:

- individual values -> hash map or scan;
- contiguous ranges -> sliding window or prefix sums;
- sorted order -> binary search or two pointers;
- in-place mutation -> two pointers.

## Python Template

```python
for i, value in enumerate(nums):
    pass
```

See `prefix_sums`, `two_sum_sorted`, and `longest_unique_substring` in
`../03_template_bank.py`.

## Walkthrough

Product of Array Except Self uses two passes. The left pass stores product before
each index; the right pass multiplies by product after each index.

## Edge Cases

- Empty or one-element arrays.
- Duplicates.
- Negative numbers and zero.
- Unicode or case sensitivity in strings.

## Common Mistakes

- Modifying a list while iterating.
- Using string concatenation in a loop instead of list join.
- Forgetting that slicing allocates.

## Practice

- **Anchor problems:** Product of Array Except Self, Valid Palindrome.
- **Extra problems:** Valid Sudoku, Encode and Decode Strings.
- **Interview prompt:** "Does position, order, or contiguity matter?"

## Related Concepts

- `../techniques/01_two_pointers.md`
- `../techniques/02_sliding_window.md`
- `../techniques/03_prefix_sums.md`
