# Tree Traversals

## Quick Revision

- **When to use it:** visit tree nodes in structural order.
- **Core idea:** traversal order controls when root is processed.
- **Complexity:** O(n) time, O(h) DFS stack or O(w) BFS queue.
- **Template:** `inorder`, `level_order`.
- **Common trap:** using inorder on a non-BST expecting sorted values.

## Mental Model

Traversal is not the solution by itself; it is the order in which the solution
collects or combines information.

## How It Works

- Preorder: root before children, useful for serialization/copy.
- Inorder: left, root, right; sorted for BST.
- Postorder: children before root, useful for delete/bottom-up DP.
- Level order: breadth-first by depth.

## Python Template

```python
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```

See `inorder` and `level_order` in `../03_template_bank.py`.

## Walkthrough

For Binary Tree Level Order Traversal, freeze `len(q)` before processing a level.
That prevents children from mixing into the current level.

## Edge Cases

- Empty tree.
- Skewed tree.
- Duplicate values.
- Wide level that increases queue size.

## Common Mistakes

- Mixing level sizes in BFS.
- Confusing preorder and postorder.
- Recursion depth on skewed trees.

## Practice

- **Anchor problems:** Level Order Traversal, Kth Smallest in BST.
- **Extra problems:** Right Side View, Serialize and Deserialize Binary Tree.
- **Interview prompt:** "When should the root be processed?"

## Related Concepts

- `../data-structures/05_trees_and_bsts.md`
