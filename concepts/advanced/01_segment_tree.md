# Segment Tree

## Quick Revision

- **When to use it:** range queries with updates.
- **Core idea:** store aggregates over intervals in a binary tree.
- **Complexity:** build O(n), query/update O(log n).
- **Template:** `SegmentTree`.
- **Common trap:** off-by-one in query bounds.

## Mental Model

A segment tree precomputes answers for chunks. A range query is answered by
combining O(log n) chunks that exactly cover the requested range.

## How It Works

The iterative version stores leaves in the second half of an array and parents in
the first half. Updating a leaf recomputes ancestors. Query moves left and right
boundaries upward while collecting complete chunks.

## Python Template

```python
seg = SegmentTree(nums)
seg.update(index, value)
total = seg.query(left, right)
```

See `SegmentTree` in `../03_template_bank.py`.

## Walkthrough

For Range Sum Query Mutable, each update changes one value. Recomputing the whole
prefix array is O(n), but a segment tree updates only O(log n) ancestors.

## Edge Cases

- One element.
- Query entire range.
- Repeated updates to same index.
- Inclusive vs half-open query API.

## Common Mistakes

- Mixing 0-indexed input with internal positions.
- Returning wrong identity value for min/max variants.
- Forgetting to update parent nodes.

## Practice

- **Anchor problems:** Range Sum Query Mutable.
- **Extra problems:** My Calendar III, Count of Smaller Numbers After Self.
- **Interview prompt:** "Do both range queries and updates need to be fast?"

## Related Concepts

- `02_fenwick_tree.md`
- `../techniques/03_prefix_sums.md`
