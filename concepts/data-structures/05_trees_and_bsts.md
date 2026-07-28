# Trees And BSTs

## Quick Revision

- **When to use it:** hierarchy, depth, path, subtree, sorted BST property.
- **Core idea:** solve left and right subtrees, then combine.
- **Complexity:** O(n) time, O(h) recursion stack.
- **Template:** DFS, BFS, BST min/max bounds.
- **Common trap:** validating BST only against direct children.

## Mental Model

Every tree node is the root of a smaller tree. Decide what information a subtree
should return to its parent.

## How It Works

Tree DFS:

- base case for empty node;
- compute left answer;
- compute right answer;
- combine with current node.

BST:

- left subtree values must be within lower and current bounds;
- right subtree values must be within current and upper bounds.

## Python Template

```python
def valid_bst(node, low, high):
    if not node:
        return True
    if not (low < node.val < high):
        return False
    return valid_bst(node.left, low, node.val) and valid_bst(node.right, node.val, high)
```

See `max_depth`, `inorder`, and `level_order` in `../03_template_bank.py`.

## Walkthrough

Inorder traversal of a BST visits values in sorted order. That is useful for kth
smallest and validation, but bounds are safer for full BST validation.

## Edge Cases

- Empty tree.
- Duplicate values.
- Skewed tree.
- Negative or extreme values.

## Common Mistakes

- Confusing depth and height.
- Mixing preorder/inorder/postorder use cases.
- Assuming balanced height.

## Practice

- **Anchor problems:** Maximum Depth, Validate BST.
- **Extra problems:** Invert Binary Tree, LCA of BST, Kth Smallest.
- **Interview prompt:** "What should each subtree return?"

## Related Concepts

- `../algorithms/03_tree_traversals.md`
