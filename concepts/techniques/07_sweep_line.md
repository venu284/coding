# Sweep Line

## Quick Revision

- **When to use it:** events over time/position, overlap counts, active intervals.
- **Core idea:** sort events and update active state while sweeping left to right.
- **Complexity:** O(n log n).
- **Template:** `max_overlap`.
- **Common trap:** tie ordering for start and end events.

## Mental Model

Convert ranges into point events. The active count or active set tells you what is
true at the current sweep position.

## How It Works

For maximum overlap:

1. Add `(start, +1)`.
2. Add `(end, -1)`.
3. Sort events.
4. Accumulate active count and track best.

## Python Template

```python
events = []
for start, end in intervals:
    events.append((start, 1))
    events.append((end, -1))
```

See `max_overlap` in `../03_template_bank.py`.

## Walkthrough

Meeting Rooms II counts how many meetings are active at once. The maximum active
count is the number of rooms required.

## Edge Cases

- Meeting ending when another starts.
- Identical start times.
- Zero-length intervals if allowed.
- Need active objects, not just count.

## Common Mistakes

- Wrong tie order at equal time.
- Forgetting to sort events.
- Using merge intervals when maximum overlap is needed.

## Practice

- **Anchor problems:** Meeting Rooms II, Car Pooling.
- **Extra problems:** Employee Free Time, My Calendar.
- **Interview prompt:** "Can intervals become start/end events?"

## Related Concepts

- `../data-structures/10_intervals.md`
- `04_monotonic_stack_queue.md`
