# Quick Revision Cards

Use these cards when you need fast recall. Each card gives the interview trigger,
the core idea, the normal complexity, the template to remember, an anchor problem,
and the trap that usually fails hidden tests.

## Foundations

### Big-O
- **Trigger:** constraints decide whether brute force survives.
- **Core idea:** count how work grows as input grows.
- **Complexity:** know O(1), O(log n), O(n), O(n log n), O(n^2), O(2^n), O(n!).
- **Template:** estimate before coding.
- **Anchor:** compare Two Sum brute force vs hash map.
- **Trap:** ignoring constraints like n = 1e5.

### Recursion
- **Trigger:** tree, graph DFS, backtracking, divide and conquer.
- **Core idea:** solve a smaller same-shaped problem, then combine.
- **Complexity:** calls times work per call; stack is depth.
- **Template:** base case -> recursive calls -> combine.
- **Anchor:** Maximum Depth of Binary Tree.
- **Trap:** missing base case or mutating shared state.

### Invariants
- **Trigger:** loops with pointers, binary search, sliding window.
- **Core idea:** keep one statement true before and after every iteration.
- **Complexity:** usually same as the loop count.
- **Template:** initialize -> maintain -> terminate.
- **Anchor:** Binary Search.
- **Trap:** changing `left` or `right` without preserving meaning.

### Math For DSA
- **Trigger:** modulo, gcd, combinatorics, coordinates, overflow, parity.
- **Core idea:** reduce the problem using arithmetic properties.
- **Complexity:** often O(log n) for gcd or exponentiation.
- **Template:** gcd, mod counting, integer bounds.
- **Anchor:** Missing Number.
- **Trap:** negative modulo and integer division edge cases.

### Python Toolkit
- **Trigger:** Python-specific implementation speed.
- **Core idea:** know the standard library that changes complexity.
- **Complexity:** dict/set O(1) average, heap O(log n), deque popleft O(1).
- **Template:** `Counter`, `defaultdict`, `deque`, `heapq`, `bisect`.
- **Anchor:** Top K Frequent Elements.
- **Trap:** using `list.pop(0)` for queues.

### Testing Edge Cases
- **Trigger:** before submitting every solution.
- **Core idea:** test shape, boundary, duplicates, empty/min input, and tricky values.
- **Complexity:** O(1) planning time that saves failed submissions.
- **Template:** happy -> edge -> boundary -> tricky.
- **Anchor:** Valid Anagram.
- **Trap:** only testing the sample.

## Data Structures

### Arrays And Strings
- **Trigger:** indexed sequence, contiguous ranges, in-place updates.
- **Core idea:** O(1) random access, O(n) insert/delete in the middle.
- **Complexity:** scans O(n), sorting O(n log n).
- **Template:** scan, two pointers, prefix sums.
- **Anchor:** Product of Array Except Self.
- **Trap:** off-by-one and string immutability.

### Hash Maps And Sets
- **Trigger:** find, count, group, duplicate, seen-before.
- **Core idea:** trade memory for O(1) average lookup.
- **Complexity:** O(n) time and O(n) space for one pass.
- **Template:** seen map, frequency map, grouping map.
- **Anchor:** Two Sum.
- **Trap:** storing the item before checking for its pair.

### Stacks And Queues
- **Trigger:** LIFO nesting or FIFO level order.
- **Core idea:** stack resolves recent items; queue processes in arrival order.
- **Complexity:** O(n) time, O(n) space.
- **Template:** append/pop for stack, deque for queue.
- **Anchor:** Valid Parentheses.
- **Trap:** using a queue when unresolved state needs LIFO.

### Linked Lists
- **Trigger:** node pointers, reverse, cycle, merge, remove nth.
- **Core idea:** pointer rewiring; dummy nodes reduce edge cases.
- **Complexity:** O(n) time, O(1) extra space for most pointer tasks.
- **Template:** dummy head, prev/curr/next, fast/slow.
- **Anchor:** Reverse Linked List.
- **Trap:** losing `next` before rewiring.

### Trees And BSTs
- **Trigger:** hierarchy, subtree, depth, paths, sorted BST property.
- **Core idea:** recurse left and right, combine local answer.
- **Complexity:** O(n) time, O(h) stack.
- **Template:** DFS, BFS, BST bounds.
- **Anchor:** Maximum Depth of Binary Tree.
- **Trap:** validating BST by only comparing parent and child.

### Heaps
- **Trigger:** top K, kth, smallest/largest next, streaming median.
- **Core idea:** heap gives fast access to one extreme.
- **Complexity:** push/pop O(log n), top O(1).
- **Template:** size-k heap, two heaps.
- **Anchor:** Top K Frequent Elements.
- **Trap:** Python `heapq` is a min-heap.

### Graphs
- **Trigger:** nodes, edges, grid reachability, connected components.
- **Core idea:** represent neighbors, visit each node once.
- **Complexity:** O(V + E).
- **Template:** adjacency list, BFS, DFS, visited set.
- **Anchor:** Number of Islands.
- **Trap:** marking visited too late.

### Tries
- **Trigger:** prefix, word dictionary, autocomplete, wildcard search.
- **Core idea:** share prefixes across words.
- **Complexity:** O(L) per insert/search where L is word length.
- **Template:** nested dict nodes with end marker.
- **Anchor:** Implement Trie.
- **Trap:** forgetting word-end marker.

### Union-Find
- **Trigger:** connectivity, components, redundant edge, undirected cycle.
- **Core idea:** merge sets with parent pointers.
- **Complexity:** near O(1) per operation with compression and rank.
- **Template:** `find`, `union`.
- **Anchor:** Redundant Connection.
- **Trap:** union raw nodes instead of roots.

### Intervals
- **Trigger:** ranges, meetings, overlaps, merge, insert.
- **Core idea:** sort so related ranges become adjacent.
- **Complexity:** O(n log n) from sorting.
- **Template:** sort and sweep.
- **Anchor:** Merge Intervals.
- **Trap:** wrong overlap condition.

## Algorithms And Techniques

### Sorting
- **Trigger:** need order, grouping, intervals, kth alternatives.
- **Core idea:** sort once to simplify comparisons.
- **Complexity:** O(n log n).
- **Template:** key function, custom tuple sort.
- **Anchor:** Meeting Rooms.
- **Trap:** sorting when O(n) hash solution exists.

### Binary Search
- **Trigger:** sorted input, monotonic answer, O(log n).
- **Core idea:** discard half the search space each step.
- **Complexity:** O(log n).
- **Template:** half-open `lo < hi`.
- **Anchor:** Search in Rotated Sorted Array.
- **Trap:** inconsistent bounds.

### Tree Traversals
- **Trigger:** visit all tree nodes in a specific order.
- **Core idea:** preorder, inorder, postorder, level order.
- **Complexity:** O(n).
- **Template:** recursive DFS or deque BFS.
- **Anchor:** Binary Tree Level Order Traversal.
- **Trap:** mixing levels in BFS.

### Graph Traversals
- **Trigger:** reachability, components, shortest unweighted path.
- **Core idea:** DFS explores; BFS gives shortest unweighted distance.
- **Complexity:** O(V + E).
- **Template:** stack/recursion or deque.
- **Anchor:** Clone Graph.
- **Trap:** no visited set.

### Topological Sort
- **Trigger:** prerequisites, dependency order, directed cycle.
- **Core idea:** repeatedly remove nodes with indegree zero.
- **Complexity:** O(V + E).
- **Template:** Kahn's algorithm.
- **Anchor:** Course Schedule.
- **Trap:** reversing edge direction.

### Shortest Paths
- **Trigger:** minimum cost or steps in graph.
- **Core idea:** BFS for unweighted, Dijkstra for non-negative weights.
- **Complexity:** BFS O(V + E), Dijkstra O((V + E) log V).
- **Template:** queue or min-heap distances.
- **Anchor:** Network Delay Time.
- **Trap:** using Dijkstra with negative weights.

### Minimum Spanning Tree
- **Trigger:** connect all nodes with minimum total edge cost.
- **Core idea:** choose safe edges without cycles.
- **Complexity:** Kruskal O(E log E).
- **Template:** sort edges + union-find.
- **Anchor:** Min Cost to Connect All Points.
- **Trap:** stopping before n - 1 edges.

### Dynamic Programming
- **Trigger:** optimal/count ways over overlapping choices.
- **Core idea:** define subproblem, recurrence, base cases, order.
- **Complexity:** number of states times transition cost.
- **Template:** memo DFS or bottom-up table.
- **Anchor:** House Robber.
- **Trap:** coding before defining `dp[i]`.

### Greedy
- **Trigger:** local choice seems sufficient, min jumps, reachability, intervals.
- **Core idea:** prove the local best never blocks the global best.
- **Complexity:** often O(n) or O(n log n).
- **Template:** maintain current best/reach.
- **Anchor:** Jump Game.
- **Trap:** using greedy when future choices can invalidate it.

### Bit Manipulation
- **Trigger:** XOR, masks, count bits, single number, no extra space.
- **Core idea:** use binary identities directly.
- **Complexity:** O(n) or O(number of bits).
- **Template:** XOR fold, bit count loop.
- **Anchor:** Single Number.
- **Trap:** not knowing `n & (n - 1)`.

### Two Pointers
- **Trigger:** sorted pair/triple, palindrome, in-place, opposite ends.
- **Core idea:** move the pointer that can improve the answer.
- **Complexity:** O(n) after sorting if needed.
- **Template:** `left`, `right`, while left < right.
- **Anchor:** 3Sum.
- **Trap:** duplicate skipping.

### Sliding Window
- **Trigger:** contiguous substring/subarray with condition.
- **Core idea:** expand right, shrink left when invalid.
- **Complexity:** O(n).
- **Template:** variable window with frequency map.
- **Anchor:** Longest Substring Without Repeating Characters.
- **Trap:** wrong shrink condition.

### Prefix Sums
- **Trigger:** many range sums or subarray sum equals k.
- **Core idea:** convert range sum to difference of prefixes.
- **Complexity:** O(n) build, O(1) query.
- **Template:** prefix array or prefix count map.
- **Anchor:** Subarray Sum Equals K.
- **Trap:** forgetting initial prefix zero.

### Monotonic Stack And Queue
- **Trigger:** next greater/smaller, sliding window max, histogram.
- **Core idea:** keep only candidates that can still win.
- **Complexity:** O(n).
- **Template:** stack/deque of indices.
- **Anchor:** Daily Temperatures.
- **Trap:** push values when indices are needed.

### Backtracking
- **Trigger:** all subsets, permutations, combinations, boards.
- **Core idea:** choose, explore, unchoose.
- **Complexity:** exponential.
- **Template:** DFS with path.
- **Anchor:** Subsets.
- **Trap:** appending the live path instead of a copy.

### Divide And Conquer
- **Trigger:** split input, solve halves, combine.
- **Core idea:** reduce a problem to independent subproblems.
- **Complexity:** often O(n log n).
- **Template:** merge sort shape.
- **Anchor:** Sort an Array.
- **Trap:** bad base case causing infinite recursion.

### Sweep Line
- **Trigger:** events over time/position, max overlap, active intervals.
- **Core idea:** sort events and maintain active state.
- **Complexity:** O(n log n).
- **Template:** events `(point, delta)`.
- **Anchor:** Meeting Rooms II.
- **Trap:** tie ordering at start/end.

### Fast/Slow Pointers
- **Trigger:** cycle, middle, kth from end in linked list.
- **Core idea:** pointers moving at different speeds reveal structure.
- **Complexity:** O(n), O(1).
- **Template:** slow one step, fast two steps.
- **Anchor:** Linked List Cycle.
- **Trap:** not checking `fast and fast.next`.

### Search On Answer
- **Trigger:** minimize maximum, maximize minimum, monotonic feasibility.
- **Core idea:** binary search values, not indices.
- **Complexity:** O(log range * check cost).
- **Template:** `can(x)` predicate.
- **Anchor:** Koko Eating Bananas.
- **Trap:** predicate not monotonic.

## Advanced

### Segment Tree
- **Trigger:** range query plus point/range updates.
- **Core idea:** tree stores aggregate for intervals.
- **Complexity:** build O(n), query/update O(log n).
- **Template:** iterative segment tree.
- **Anchor:** Range Sum Query Mutable.
- **Trap:** off-by-one in query bounds.

### Fenwick Tree
- **Trigger:** prefix sums with updates.
- **Core idea:** store partial sums using lowest set bit.
- **Complexity:** update/query O(log n).
- **Template:** 1-indexed BIT.
- **Anchor:** Count of Smaller Numbers After Self.
- **Trap:** forgetting 1-indexing.

### Advanced Graphs
- **Trigger:** SCC, bridges, articulation, max flow, negative weights.
- **Core idea:** choose graph algorithm by edge type and ask.
- **Complexity:** varies by algorithm.
- **Template:** Tarjan, Bellman-Ford, Floyd-Warshall.
- **Anchor:** Critical Connections in a Network.
- **Trap:** using the basic BFS/DFS template for weighted or directed nuance.

### Advanced DP
- **Trigger:** bitmask state, interval state, tree state, digit constraints.
- **Core idea:** encode the missing decision dimensions.
- **Complexity:** state count times transition cost.
- **Template:** memo with tuple state.
- **Anchor:** Partition to K Equal Sum Subsets.
- **Trap:** state explosion without pruning.

### String Algorithms
- **Trigger:** substring search, palindromes, repeated patterns.
- **Core idea:** avoid comparing the same characters repeatedly.
- **Complexity:** KMP O(n + m), rolling hash average O(n).
- **Template:** prefix function, rolling hash.
- **Anchor:** Longest Palindromic Substring.
- **Trap:** hash collision assumptions.

### System Design DSA
- **Trigger:** design cache, rate limiter, leaderboard, autocomplete.
- **Core idea:** combine data structures to meet operation constraints.
- **Complexity:** state each operation's time and space.
- **Template:** map + linked list, heap + lazy delete, trie + heap.
- **Anchor:** LRU Cache.
- **Trap:** optimizing one operation while breaking another.
