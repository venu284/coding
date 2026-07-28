# Fenwick Tree

## Quick Revision

- **When to use it:** prefix sums with point updates.
- **Core idea:** use lowest set bit to jump across stored ranges.
- **Complexity:** update/query O(log n), space O(n).
- **Template:** `FenwickTree`.
- **Common trap:** forgetting 1-indexing internally.

## Mental Model

Fenwick tree is a compact prefix-sum structure. Each index stores the sum of a
range whose size is determined by the lowest set bit.

## How It Works

To update, add delta to index and climb to larger ranges using `i += i & -i`.
To query prefix sum, accumulate and move to smaller ranges using `i -= i & -i`.

## Python Template

```python
bit = FenwickTree(n)
bit.add(index, delta)
prefix = bit.prefix_sum(index)
```

See `FenwickTree` in `../03_template_bank.py`.

## Walkthrough

For Count of Smaller Numbers After Self, process values from right to left. Query
how many smaller values have been seen, then add the current value.

## Edge Cases

- Coordinate compression for large values.
- Duplicate values.
- Index 0 handling.
- Query before any update.

## Common Mistakes

- Using raw values as indices without compression.
- Off-by-one with internal 1-indexing.
- Confusing prefix query with range query.

## Practice

- **Anchor problems:** Count of Smaller Numbers After Self.
- **Extra problems:** Range Sum Query Mutable, Reverse Pairs.
- **Interview prompt:** "Do I only need prefix/range sums, not arbitrary range min?"

## Related Concepts

- `01_segment_tree.md`
- `../algorithms/10_bit_manipulation.md`
