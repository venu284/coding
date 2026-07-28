# Prefix Sums

## Quick Revision

- **When to use it:** range sums, subarray sums, repeated sum queries.
- **Core idea:** range sum is difference of two prefixes.
- **Complexity:** build O(n), query O(1); hash-prefix variants O(n).
- **Template:** `prefix_sums`, `range_sum`.
- **Common trap:** forgetting the initial prefix 0.

## Mental Model

Prefix sums turn many repeated range computations into subtraction. For subarray
sum equals k, store how many previous prefixes would complete the target.

## How It Works

If `prefix[i]` is sum before index i, then sum from left to right inclusive is
`prefix[right + 1] - prefix[left]`.

## Python Template

```python
pref = [0]
for x in nums:
    pref.append(pref[-1] + x)
```

See `prefix_sums` and `range_sum` in `../03_template_bank.py`.

## Walkthrough

For Subarray Sum Equals K, current prefix is `p`. Any previous prefix `p - k`
marks a subarray ending here with sum k.

## Edge Cases

- Negative numbers.
- Zero target.
- Empty prefix before first item.
- Multiple same prefix values.

## Common Mistakes

- Sliding window on arrays with negatives.
- Missing `counts[0] = 1`.
- Off-by-one range query.

## Practice

- **Anchor problems:** Subarray Sum Equals K, Range Sum Query.
- **Extra problems:** Pivot Index, Product Except Self.
- **Interview prompt:** "Can a range be represented by two accumulated values?"

## Related Concepts

- `../data-structures/01_arrays_and_strings.md`
- `../data-structures/02_hash_maps_and_sets.md`
