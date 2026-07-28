# Recursion

## Quick Revision

- **When to use it:** trees, DFS, backtracking, divide and conquer.
- **Core idea:** solve a smaller version of the same problem.
- **Complexity:** number of calls times work per call; space is recursion depth.
- **Template:** base case -> recurse -> combine result.
- **Common trap:** missing the base case or sharing mutable state incorrectly.

## Mental Model

A recursive function is a contract. Assume it correctly solves a smaller input,
then write how the current call uses that answer. You do not mentally expand the
entire call tree in an interview; you define the contract and trust it.

## How It Works

Every recursive solution needs:

1. A base case that stops.
2. Progress toward the base case.
3. A return value or side effect that combines useful information.

## Python Template

```python
def dfs(node):
    if not node:
        return 0
    left = dfs(node.left)
    right = dfs(node.right)
    return 1 + max(left, right)
```

See `max_depth` in `../03_template_bank.py`.

## Walkthrough

For maximum depth, an empty tree has depth 0. A real node has depth 1 plus the
deeper of its left and right subtrees. That sentence is the whole recurrence.

## Edge Cases

- Empty tree or empty list.
- One-node input.
- Very deep recursion in Python may need iterative DFS or recursion-limit care.

## Common Mistakes

- Returning nothing from one branch.
- Mutating a shared list and forgetting to undo it.
- Recomputing the same state without memoization.

## Practice

- **Anchor problems:** Maximum Depth of Binary Tree, Subsets.
- **Extra problems:** Invert Binary Tree, Combination Sum, Same Tree.
- **Interview prompt:** "What does this recursive call promise to return?"

## Related Concepts

- `../algorithms/03_tree_traversals.md`
- `../techniques/05_backtracking.md`
- `../techniques/06_divide_and_conquer.md`
