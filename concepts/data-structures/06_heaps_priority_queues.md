# Heaps Priority Queues

## Quick Revision

- **When to use it:** top K, kth, streaming median, merge K, repeated min/max.
- **Core idea:** keep fast access to one extreme.
- **Complexity:** push/pop O(log n), peek O(1).
- **Template:** `top_k_frequent`, `MedianFinder`.
- **Common trap:** Python `heapq` is a min-heap.

## Mental Model

A heap is for "I only need the next best item," not full sorted order. If you need
all items sorted, sort. If you repeatedly need the smallest or largest, heap.

## How It Works

For top K largest, keep a min-heap of size K. The heap root is the weakest kept
candidate. When size exceeds K, pop it.

For median stream, keep lower half in a max-heap via negatives and upper half in
a min-heap.

## Python Template

```python
heap = []
heappush(heap, item)
smallest = heappop(heap)
```

See `top_k_frequent` and `MedianFinder` in `../03_template_bank.py`.

## Walkthrough

Top K Frequent counts values, then keeps only K best `(count, value)` pairs in a
heap. This avoids sorting every unique item when K is small.

## Edge Cases

- Tied priorities.
- K equals number of unique items.
- Empty stream.
- Max-heap needed in Python.

## Common Mistakes

- Negating inconsistently.
- Letting a size-k heap grow without popping.
- Forgetting tuple tie behavior.

## Practice

- **Anchor problems:** Top K Frequent Elements, Find Median from Data Stream.
- **Extra problems:** K Closest Points, Merge K Sorted Lists, Task Scheduler.
- **Interview prompt:** "Do I need full order or just the next extreme?"

## Related Concepts

- `../foundations/05_python_dsa_toolkit.md`
- `../algorithms/06_shortest_paths.md`
