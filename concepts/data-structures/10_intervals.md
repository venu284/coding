# Intervals

## Quick Revision

- **When to use it:** ranges, meetings, overlaps, insert, merge.
- **Core idea:** sort intervals so conflicts become adjacent.
- **Complexity:** O(n log n) from sorting.
- **Template:** sort and sweep.
- **Common trap:** wrong overlap rule.

## Mental Model

Intervals become simple after sorting. Once starts are in order, you only need to
compare the next interval with the current merged interval or active set.

## How It Works

For merge intervals:

1. Sort by start.
2. Keep current merged interval.
3. If next start <= current end, merge.
4. Otherwise, push current and start a new one.

## Python Template

```python
intervals.sort()
merged = []
for start, end in intervals:
    if not merged or start > merged[-1][1]:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)
```

## Walkthrough

`[1,3]` and `[2,6]` overlap because `2 <= 3`, so they merge into `[1,6]`.

## Edge Cases

- Touching endpoints.
- Nested intervals.
- Empty interval list.
- Sort by start vs sort by end.

## Common Mistakes

- Using `<` when the problem treats touching endpoints as overlap.
- Sorting by wrong key for erase-overlap problems.
- Forgetting to append the final interval.

## Practice

- **Anchor problems:** Merge Intervals, Insert Interval.
- **Extra problems:** Non-overlapping Intervals, Meeting Rooms II.
- **Interview prompt:** "After sorting, what must be compared?"

## Related Concepts

- `../techniques/07_sweep_line.md`
- `../algorithms/09_greedy.md`
