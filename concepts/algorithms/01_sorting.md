# Sorting

## Quick Revision

- **When to use it:** order simplifies comparisons, grouping, intervals, greedy.
- **Core idea:** pay O(n log n) once to make local relationships obvious.
- **Complexity:** Python sort is O(n log n) time, O(n) worst-case auxiliary.
- **Template:** `sorted(items, key=...)`.
- **Common trap:** sorting when hashing gives O(n).

## Mental Model

Sorting is a transformation. It changes "compare everything" into "compare
neighbors" or "scan in a useful order."

## How It Works

Sort by the field that makes the decision local:

- interval merge: start time;
- non-overlap greedy: end time;
- frequency tie: count then value;
- strings for anagrams: sorted characters as a key.

## Python Template

```python
items.sort(key=lambda x: (x[0], x[1]))
```

See `merge_sort` in `../03_template_bank.py` for a from-scratch template.

## Walkthrough

Meeting Rooms sorts meetings by start time. After that, only adjacent meetings
can create a conflict.

## Edge Cases

- Ties.
- Stable sort behavior.
- Custom tuple keys.
- Sorting mutates lists in place.

## Common Mistakes

- Sorting by start when greedy needs earliest end.
- Forgetting O(n log n) may exceed target.
- Sorting strings repeatedly inside loops.

## Practice

- **Anchor problems:** Meeting Rooms, Merge Intervals.
- **Extra problems:** Sort Colors, K Closest Points.
- **Interview prompt:** "What does sorting make adjacent?"

## Related Concepts

- `../data-structures/10_intervals.md`
- `../techniques/06_divide_and_conquer.md`
