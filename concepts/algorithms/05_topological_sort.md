# Topological Sort

## Quick Revision

- **When to use it:** prerequisites, dependency order, directed cycle detection.
- **Core idea:** process nodes only after prerequisites are processed.
- **Complexity:** O(V + E).
- **Template:** `topo_sort`.
- **Common trap:** reversing edge direction.

## Mental Model

Topological order is a valid build order. A node becomes available when its
indegree reaches zero.

## How It Works

Kahn's algorithm:

1. Build adjacency list and indegree count.
2. Queue all nodes with indegree 0.
3. Pop nodes and reduce neighbors' indegree.
4. If all nodes are processed, no cycle blocks the order.

## Python Template

```python
q = deque(i for i, deg in enumerate(indeg) if deg == 0)
while q:
    node = q.popleft()
    for nei in adj[node]:
        indeg[nei] -= 1
        if indeg[nei] == 0:
            q.append(nei)
```

See `topo_sort` in `../03_template_bank.py`.

## Walkthrough

For Course Schedule, edge `prereq -> course` means taking the prerequisite unlocks
the course by reducing its indegree.

## Edge Cases

- Cycle.
- Multiple valid orders.
- Isolated nodes.
- Duplicate prerequisite pairs.

## Common Mistakes

- Edge direction reversed.
- Returning order without checking processed count.
- Not adding isolated nodes.

## Practice

- **Anchor problems:** Course Schedule, Alien Dictionary.
- **Extra problems:** Course Schedule II, Minimum Height Trees.
- **Interview prompt:** "What must happen before this node?"

## Related Concepts

- `../data-structures/07_graphs.md`
