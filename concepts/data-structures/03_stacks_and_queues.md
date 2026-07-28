# Stacks And Queues

## Quick Revision

- **When to use it:** nesting, undo, next greater, BFS, level order.
- **Core idea:** stack is LIFO; queue is FIFO.
- **Complexity:** O(1) push/pop with list stack or deque queue.
- **Template:** stack append/pop, deque append/popleft.
- **Common trap:** using `list.pop(0)` for queues.

## Mental Model

Stack keeps the most recent unresolved item. Queue processes work in the order it
was discovered.

## How It Works

Use a stack for:

- parentheses;
- monotonic next greater/smaller;
- iterative DFS.

Use a queue for:

- BFS;
- tree levels;
- shortest unweighted distance.

## Python Template

```python
stack = []
stack.append(x)
x = stack.pop()

q = deque([start])
node = q.popleft()
```

See `daily_temperatures` and `graph_bfs` in `../03_template_bank.py`.

## Walkthrough

Valid Parentheses pushes opening brackets. A closing bracket must match the most
recent unresolved opening bracket, so stack order is exactly the rule.

## Edge Cases

- Empty stack before pop.
- Leftover stack at the end.
- Queue level size changing during BFS.

## Common Mistakes

- Not checking empty stack.
- Mixing DFS and BFS accidentally.
- Storing values when indices are needed.

## Practice

- **Anchor problems:** Valid Parentheses, Binary Tree Level Order Traversal.
- **Extra problems:** Min Stack, Evaluate RPN, Daily Temperatures.
- **Interview prompt:** "Is the next item determined by recency or arrival order?"

## Related Concepts

- `../techniques/04_monotonic_stack_queue.md`
- `../algorithms/04_graph_traversals.md`
