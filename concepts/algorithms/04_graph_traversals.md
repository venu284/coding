# Graph Traversals

## Quick Revision

- **When to use it:** reachability, components, islands, unweighted shortest path.
- **Core idea:** visit nodes without repeating them.
- **Complexity:** O(V + E).
- **Template:** `graph_bfs`, `graph_dfs`.
- **Common trap:** no visited set.

## Mental Model

BFS spreads in layers. DFS follows one path deeply before backtracking. Use BFS
when distance in unweighted steps matters; use DFS when exploring a component is
enough.

## How It Works

Traversal needs:

1. A neighbor function.
2. A visited set.
3. A worklist: queue for BFS, stack/recursion for DFS.

## Python Template

```python
seen = {start}
q = deque([start])
while q:
    node = q.popleft()
    for nei in adj[node]:
        if nei not in seen:
            seen.add(nei)
            q.append(nei)
```

See `graph_bfs` and `graph_dfs` in `../03_template_bank.py`.

## Walkthrough

Clone Graph uses DFS/BFS to visit each original node once and build a map from
original node to cloned node.

## Edge Cases

- Disconnected graph.
- Self-loop.
- Directed edges.
- Empty graph.

## Common Mistakes

- Marking visited only after dequeue.
- Forgetting to start traversal from every component.
- Recursive DFS exceeding stack depth.

## Practice

- **Anchor problems:** Clone Graph, Number of Islands.
- **Extra problems:** Pacific Atlantic, Rotting Oranges.
- **Interview prompt:** "Does BFS distance matter, or is reachability enough?"

## Related Concepts

- `../data-structures/07_graphs.md`
- `06_shortest_paths.md`
