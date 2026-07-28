# Graphs

## Quick Revision

- **When to use it:** nodes/edges, grids, reachability, components, paths.
- **Core idea:** represent neighbors and avoid revisiting nodes.
- **Complexity:** O(V + E) for BFS/DFS.
- **Template:** adjacency list, visited set, queue or recursion.
- **Common trap:** marking visited too late.

## Mental Model

A graph problem is about relationships. For grids, each cell is a node and valid
neighbor moves are edges.

## How It Works

Choose representation:

- adjacency list for sparse graphs;
- matrix/grid for direct coordinate access;
- edge list for union-find or MST.

Then choose traversal or algorithm by ask.

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

See `graph_bfs`, `graph_dfs`, and `dijkstra` in `../03_template_bank.py`.

## Walkthrough

Number of Islands scans a grid. When land is found, DFS/BFS marks the entire
connected region, then the island count increases once.

## Edge Cases

- Disconnected graph.
- Cycle.
- Empty grid.
- Directed vs undirected edges.

## Common Mistakes

- No visited set.
- Treating directed edges as undirected.
- Reusing a visited set across independent runs incorrectly.

## Practice

- **Anchor problems:** Number of Islands, Clone Graph.
- **Extra problems:** Rotting Oranges, Pacific Atlantic, Network Delay Time.
- **Interview prompt:** "What are nodes, edges, and visited state?"

## Related Concepts

- `../algorithms/04_graph_traversals.md`
- `../algorithms/06_shortest_paths.md`
- `09_union_find.md`
