# Union-Find

## Quick Revision

- **When to use it:** connectivity, components, undirected cycle, merging accounts.
- **Core idea:** each set has a representative root.
- **Complexity:** near O(1) per operation with path compression and rank.
- **Template:** `UnionFind`.
- **Common trap:** unioning raw nodes instead of roots.

## Mental Model

Union-find answers "are these in the same group?" quickly while groups are being
merged over time.

## How It Works

`find(x)` returns the root of x's set. Path compression points nodes directly to
the root. `union(a, b)` merges roots and returns false if they were already in
the same set.

## Python Template

```python
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
```

See `UnionFind` in `../03_template_bank.py`.

## Walkthrough

In Redundant Connection, each edge tries to union two nodes. If union returns
false, that edge connects nodes already connected, so it creates the cycle.

## Edge Cases

- 0-indexed vs 1-indexed nodes.
- Disconnected graph.
- Duplicate edges.
- Components count updates.

## Common Mistakes

- Forgetting path compression.
- Not using rank/size.
- Counting components incorrectly after failed union.

## Practice

- **Anchor problems:** Redundant Connection, Number of Connected Components.
- **Extra problems:** Graph Valid Tree, Accounts Merge.
- **Interview prompt:** "Is this dynamic connectivity rather than traversal?"

## Related Concepts

- `07_graphs.md`
- `../algorithms/07_minimum_spanning_tree.md`
