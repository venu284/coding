# Interview Revision

This is the compressed review path when an interview or OA is close.

## Last Week

Daily:

1. Review 8-10 cards from `00_quick_revision_cards.md`.
2. Type 3 templates from `03_template_bank.py` without looking.
3. Solve 1 medium problem with no topic label.
4. Log: problem -> concept -> trigger -> missed edge case.

Rotate by day:

| Day | Focus |
|---|---|
| 1 | Hashing, arrays, strings, prefix sums |
| 2 | Two pointers, sliding window, binary search |
| 3 | Stack, monotonic stack, linked lists |
| 4 | Trees, BSTs, tree traversal |
| 5 | Graphs, BFS/DFS, topological sort, union-find |
| 6 | Heap, intervals, greedy |
| 7 | DP, backtracking, bit manipulation |

## Day Before

Do:

- Review every quick card headline and trap.
- Run `python3 concepts/03_template_bank.py`.
- Re-solve 2 weak anchors.
- Prepare a 30-second explanation for DP, graph BFS, binary search, and hashing.

Do not:

- Start a brand-new advanced topic.
- Grind until tired.
- Memorize code without understanding the trigger.

## Same Day

Use this five-minute warmup:

1. Hashing: "Can I trade space for time?"
2. Binary search: "Is the input or answer monotonic?"
3. Sliding window: "Is it contiguous?"
4. Graph: "What are nodes, edges, visited?"
5. DP: "What is the subproblem in one sentence?"

## Problem Attack Checklist

1. Restate the problem.
2. Extract input shape and constraints.
3. Name the brute force and its complexity.
4. Pick the concept from `04_decision_tables.md`.
5. State the invariant, recurrence, or data-structure operation.
6. Code the simplest correct template.
7. Test happy, edge, boundary, and tricky cases.
8. State final time and space complexity.

## High-Yield Traps

- Hashing: check before storing when looking for pairs.
- Sliding window: know exactly when to shrink.
- Binary search: keep one bounds convention.
- Tree DFS: return useful information from children.
- Graph BFS: mark visited when enqueuing.
- Topological sort: get edge direction right.
- DP: define the state before writing recurrence.
- Backtracking: append copies, not live paths.
- Heap: Python heap is a min-heap.
- Union-find: union roots, not raw nodes.

## Emergency Review Order

If you only have one hour:

1. `00_quick_revision_cards.md`
2. `04_decision_tables.md`
3. `03_template_bank.py`
4. Weakest 2 anchors from `05_practice_map.md`
