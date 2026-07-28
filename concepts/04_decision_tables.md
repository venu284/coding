# Decision Tables

Use these tables in the first two minutes of a problem. Extract the input type,
constraints, ask, and trigger words, then choose the simplest tool that fits.

## Constraint To Complexity

| Input size | Usually acceptable | Common tools |
|---|---|---|
| n <= 10 | O(n!) | permutations, exhaustive backtracking |
| n <= 20 | O(2^n) | subsets, bitmask DP |
| n <= 500 | O(n^3) | dense DP, Floyd-Warshall |
| n <= 5,000 | O(n^2) | 2D DP, pair loops |
| n <= 100,000 | O(n log n) or O(n) | sort, heap, binary search, hash, window |
| value range large | O(log answer) | search on answer |

## Input Shape To Tool

| Input shape | First tools to consider |
|---|---|
| Array/string | hashing, two pointers, sliding window, prefix sums, sorting |
| Sorted array | binary search, two pointers |
| Linked list | dummy node, reverse, fast/slow |
| Binary tree | DFS recursion, BFS levels, BST bounds |
| Graph/grid | BFS, DFS, union-find, topological sort |
| Intervals | sort and sweep, heap for active meetings |
| Prefix dictionary | trie |
| Stream | heap, deque, hash map |

## Ask To Tool

| Ask | Likely tool |
|---|---|
| Find/count/group | hash map or set |
| Longest/shortest contiguous range | sliding window |
| Range sum query | prefix sums, Fenwick tree, segment tree |
| Top K or kth | heap or quickselect |
| All combinations/permutations | backtracking |
| Minimum steps in unweighted graph | BFS |
| Dependency order | topological sort |
| Connectivity/components | union-find or DFS |
| Min/max over choices | DP or greedy |
| Minimize max / maximize min | search on answer |

## Data Structure Selection

| Need | Use | Why |
|---|---|---|
| Fast membership | set | O(1) average lookup |
| Count frequencies | dict or Counter | O(1) average update |
| Preserve unresolved recent items | stack | LIFO |
| Process by arrival order | deque queue | O(1) popleft |
| Repeated min/max extraction | heap | O(log n) updates |
| Prefix lookup | trie | O(word length) |
| Dynamic connectivity | union-find | near O(1) union/find |
| Dynamic prefix sums | Fenwick tree | O(log n) update/query |
| Dynamic range min/sum/max | segment tree | O(log n) update/query |

## Algorithm Selection

| Trigger | Algorithm |
|---|---|
| Sorted or monotonic | binary search |
| Need order before scan | sorting |
| Tree all nodes | DFS or BFS traversal |
| Unweighted shortest path | BFS |
| Non-negative weighted shortest path | Dijkstra |
| Negative weighted path | Bellman-Ford |
| All-pairs shortest path, small n | Floyd-Warshall |
| Connect all nodes minimum cost | Kruskal or Prim |
| Directed dependency order | topological sort |
| Overlapping subproblems | dynamic programming |
| Provable local best | greedy |

## DP Or Greedy

| Question | If yes |
|---|---|
| Does a choice affect future options in multiple ways? | DP is safer |
| Can you define `dp[i]` or `dp[i][j]` clearly? | DP |
| Does the locally best choice never need revisiting? | Greedy |
| Can you prove an exchange argument? | Greedy |
| Unsure between them? | Start with DP, then see if it simplifies to greedy |

## Common First-Two-Minute Script

1. What is the input shape?
2. What are the constraints?
3. What is the ask: count, min/max, existence, all solutions, exact item?
4. Is there sorted order or monotonic behavior?
5. Is there repeated work or overlapping subproblems?
6. Which template gives the target complexity?
