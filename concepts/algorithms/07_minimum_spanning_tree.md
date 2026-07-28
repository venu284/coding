# Minimum Spanning Tree

## Quick Revision

- **When to use it:** connect all nodes with minimum total undirected edge cost.
- **Core idea:** add safe edges that do not create cycles.
- **Complexity:** Kruskal is O(E log E).
- **Template:** sort edges plus `UnionFind`.
- **Common trap:** not stopping after n - 1 edges.

## Mental Model

MST is about connecting everything cheaply, not shortest path between two nodes.
Kruskal sorts edges by cost and accepts an edge only if it connects two different
components.

## How It Works

1. Convert choices to weighted edges.
2. Sort by weight.
3. Use union-find to reject cycle edges.
4. Stop when n - 1 edges are accepted.

## Python Template

```python
cost = 0
for w, a, b in sorted(edges):
    if uf.union(a, b):
        cost += w
```

See `UnionFind` in `../03_template_bank.py`.

## Walkthrough

Min Cost to Connect All Points creates Manhattan-distance edges, sorts them, and
uses Kruskal to join components with the cheapest safe edges.

## Edge Cases

- Already connected graph.
- Disconnected graph.
- Equal edge weights.
- Complete graph with many edges.

## Common Mistakes

- Solving with Dijkstra instead of MST.
- Counting accepted edges incorrectly.
- Forgetting undirected cycle checks.

## Practice

- **Anchor problems:** Min Cost to Connect All Points.
- **Extra problems:** Connecting Cities With Minimum Cost.
- **Interview prompt:** "Am I connecting all nodes or finding a path?"

## Related Concepts

- `../data-structures/09_union_find.md`
- `06_shortest_paths.md`
