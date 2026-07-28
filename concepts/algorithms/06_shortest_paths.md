# Shortest Paths

## Quick Revision

- **When to use it:** minimum steps or minimum cost in a graph.
- **Core idea:** choose algorithm by edge weights.
- **Complexity:** BFS O(V + E), Dijkstra O((V + E) log V).
- **Template:** `graph_bfs`, `dijkstra`.
- **Common trap:** using Dijkstra with negative weights.

## Mental Model

Shortest path is not one algorithm. Unweighted graphs use BFS because each layer
adds one step. Non-negative weighted graphs use Dijkstra because the smallest
known distance can be finalized safely.

## How It Works

BFS tracks distance by levels. Dijkstra uses a min-heap of `(distance, node)` and
relaxes outgoing edges when a better distance is found.

## Python Template

```python
dist = {source: 0}
heap = [(0, source)]
while heap:
    cost, node = heappop(heap)
    if cost != dist[node]:
        continue
```

See `dijkstra` in `../03_template_bank.py`.

## Walkthrough

Network Delay Time runs Dijkstra from the source and takes the maximum final
distance. If any node is missing, not all nodes are reachable.

## Edge Cases

- Unreachable nodes.
- Multiple edges between same nodes.
- Zero-weight edges.
- Negative weights need another algorithm.

## Common Mistakes

- Treating weighted graph like unweighted BFS.
- Not skipping stale heap entries.
- Forgetting directed edge direction.

## Practice

- **Anchor problems:** Network Delay Time, Word Ladder.
- **Extra problems:** Cheapest Flights, Rotting Oranges.
- **Interview prompt:** "Are edges weighted, and can weights be negative?"

## Related Concepts

- `04_graph_traversals.md`
- `../data-structures/06_heaps_priority_queues.md`
