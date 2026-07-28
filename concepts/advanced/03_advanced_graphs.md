# Advanced Graphs

## Quick Revision

- **When to use it:** SCCs, bridges, articulation points, negative weights, max flow.
- **Core idea:** graph details decide the specialized algorithm.
- **Complexity:** Tarjan O(V + E), Bellman-Ford O(VE), Floyd-Warshall O(n^3).
- **Template:** choose by graph property.
- **Common trap:** forcing basic BFS/DFS onto weighted or directed nuance.

## Mental Model

Advanced graph problems usually add one constraint: directed cycles, negative
weights, critical edges, all-pairs paths, or capacity. Name that constraint first.

## How It Works

Common tools:

- Tarjan for strongly connected components, bridges, articulation points.
- Bellman-Ford for negative weights and negative-cycle detection.
- Floyd-Warshall for all-pairs shortest paths on small dense graphs.
- Max flow for capacity through a network.

## Python Template

```python
# Tarjan-style DFS shape
disc[node] = low[node] = time
for nei in adj[node]:
    if nei not in disc:
        dfs(nei)
        low[node] = min(low[node], low[nei])
```

## Walkthrough

Critical Connections uses discovery time and low-link values. If a neighbor cannot
reach an ancestor of the current node, the edge to that neighbor is a bridge.

## Edge Cases

- Disconnected graph.
- Parallel edges.
- Directed vs undirected low-link rules.
- Negative cycles.

## Common Mistakes

- Reusing undirected bridge logic for directed SCCs.
- Forgetting parent edge in bridge DFS.
- Running Dijkstra on negative weights.

## Practice

- **Anchor problems:** Critical Connections in a Network.
- **Extra problems:** Network Delay Time variants, Cheapest Flights, SCC drills.
- **Interview prompt:** "What graph feature makes the basic traversal insufficient?"

## Related Concepts

- `../data-structures/07_graphs.md`
- `../algorithms/06_shortest_paths.md`
