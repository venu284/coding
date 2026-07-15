# Pattern Cards — the 19 shapes behind Blind 75

One card per pattern. This is the spine of the whole system. Read the **Trigger**
and **Template** lines until they're reflex. Every Blind 75 problem is one of these
wearing a costume.

Card format:
- **Trigger** — words/shape in the problem that scream this pattern
- **Why** — the one-sentence reason it works
- **Template** — function name in `01_template_bank.py` to type from memory
- **Complexity** — time / space you say out loud in the interview
- **Anchors** — the 2 problems you master cold (see `02_anchor_problems.md`)
- **Trap** — the mistake that fails the hidden test case

---

## 1. Hashing (lookup / frequency / group)
- **Trigger:** "find a pair", "count", "seen before", "group by", "duplicate". Any O(n²) nested-loop brute force.
- **Why:** dict/set give O(1) membership; trade space for time.
- **Template:** `two_sum`, `group_anagrams`
- **Complexity:** O(n) time, O(n) space
- **Anchors:** Two Sum, Group Anagrams
- **Trap:** store the value BEFORE you need to look it up; watch index-vs-value keys.

## 2. Two Pointers (sorted, opposite ends)
- **Trigger:** "sorted array" + "find pair/triple", "palindrome", "in-place", "remove duplicates".
- **Why:** sorted order lets one comparison eliminate a whole side.
- **Template:** `two_sum_sorted`
- **Complexity:** O(n) time (O(n log n) if you sort first), O(1) space
- **Anchors:** Valid Palindrome, 3Sum
- **Trap:** skip duplicates when the problem wants unique tuples (3Sum).

## 3. Sliding Window (contiguous run under a constraint)
- **Trigger:** "contiguous subarray/substring", "longest/shortest ... such that", "at most K".
- **Why:** expand right to grow, shrink left when the window breaks the rule — each index enters/leaves once.
- **Template:** `longest_unique_substring`
- **Complexity:** O(n) time, O(k) space
- **Anchors:** Best Time to Buy/Sell Stock, Longest Substring Without Repeating Characters
- **Trap:** decide fixed-size vs variable-size first; know your shrink condition exactly.

## 4. Binary Search (sorted space OR search-on-answer)
- **Trigger:** "sorted", "rotated sorted", O(log n) required, "minimize the max / maximize the min".
- **Why:** each step halves the search space.
- **Template:** `binary_search`, `lower_bound`
- **Complexity:** O(log n) time, O(1) space
- **Anchors:** Search in Rotated Sorted Array, Koko Eating Bananas (search on answer)
- **Trap:** pick ONE invariant ([lo,hi] inclusive vs [lo,hi) half-open) and keep mid/update consistent.

## 5. Stack + Monotonic Stack
- **Trigger:** "matching/nesting brackets", "next greater/smaller element", "previous ...", histogram.
- **Why:** stack remembers unresolved items in LIFO order; monotonic keeps only useful candidates.
- **Template:** `valid_parentheses`, `daily_temperatures`
- **Complexity:** O(n) time, O(n) space
- **Anchors:** Valid Parentheses, Daily Temperatures
- **Trap:** monotonic — decide increasing vs decreasing, and push index vs value.

## 6. Linked List (dummy / reverse / fast-slow)
- **Trigger:** "reverse", "middle", "cycle", "merge sorted lists", "remove Nth from end".
- **Why:** dummy head kills edge cases; fast/slow finds middle & cycles; prev/curr/next reverses.
- **Template:** `reverse_list`, `has_cycle`
- **Complexity:** O(n) time, O(1) space
- **Anchors:** Reverse Linked List, Linked List Cycle
- **Trap:** save `next` before rewiring or you lose the rest of the list.

## 7. Tree DFS (bottom-up recursion)
- **Trigger:** "depth", "path sum", "diameter", "same/subtree", "validate BST".
- **Why:** ask "what do I need from left and right subtree?" then combine.
- **Template:** `max_depth`
- **Complexity:** O(n) time, O(h) space (recursion stack)
- **Anchors:** Maximum Depth of Binary Tree, Invert Binary Tree
- **Trap:** base case `if not root`; for BST-validity pass down (min,max) bounds, don't just compare children.

## 8. Tree BFS (level-order)
- **Trigger:** "level by level", "level order", "right side view", "shortest steps in a tree".
- **Why:** a deque processes one full level at a time via `for _ in range(len(q))`.
- **Template:** `level_order`
- **Complexity:** O(n) time, O(n) space
- **Anchors:** Binary Tree Level Order Traversal, Binary Tree Right Side View
- **Trap:** freeze the level size before the inner loop, or you mix levels.

## 9. Trie (prefix tree)
- **Trigger:** "prefix", "starts with", "dictionary of words", "autocomplete", word search on a board.
- **Why:** shared prefixes share nodes → prefix queries are O(len), not O(#words · len).
- **Template:** `Trie`
- **Complexity:** O(L) per op, O(total chars) space
- **Anchors:** Implement Trie, Design Add and Search Words (`.` wildcard)
- **Trap:** mark word-end explicitly ("$"); "app" is a prefix but not a word unless inserted.

## 10. Heap (top-K / streaming / two-heap)
- **Trigger:** "top/K-th largest/smallest", "K closest", "merge K", "median of a stream", "schedule by frequency".
- **Why:** heap gives O(log n) push/pop of the extreme; size-K heap keeps only what matters.
- **Template:** `top_k_frequent`
- **Complexity:** O(n log k) time, O(k) space
- **Anchors:** Top K Frequent Elements, Find Median from Data Stream (two heaps)
- **Trap:** Python heapq is a MIN-heap; negate values for a max-heap. Size-K "largest" uses a MIN-heap.

## 11. Backtracking (choose / explore / unchoose)
- **Trigger:** "all subsets/permutations/combinations", "generate all", "N-Queens", "partition".
- **Why:** DFS over a decision tree; undo the choice on the way back up.
- **Template:** `subsets`, `permutations`
- **Complexity:** exponential (O(2^n), O(n!)) — expected, say it out loud
- **Anchors:** Subsets, Combination Sum
- **Trap:** append a COPY `path[:]`; sort + skip duplicates for "no duplicate combos".

## 12. Graph BFS/DFS (grid & adjacency)
- **Trigger:** "grid of regions/islands", "connected", "reachable", "shortest path unweighted", "clone graph".
- **Why:** visit every node once, mark visited to avoid loops; BFS = shortest unweighted, DFS = explore.
- **Template:** `num_islands`
- **Complexity:** O(V+E) time, O(V) space
- **Anchors:** Number of Islands, Clone Graph
- **Trap:** mark visited when you ENQUEUE (BFS), not when you dequeue, or nodes double-enter.

## 13. Topological Sort (dependencies / ordering)
- **Trigger:** "prerequisites", "build order", "course schedule", "is there a valid ordering / a cycle?".
- **Why:** repeatedly take nodes with in-degree 0; if you can't take all, there's a cycle.
- **Template:** `can_finish`
- **Complexity:** O(V+E) time, O(V+E) space
- **Anchors:** Course Schedule, Alien Dictionary
- **Trap:** direction of edges (prereq → course); count processed nodes to detect the cycle.

## 14. Union-Find (connectivity / undirected cycle)
- **Trigger:** "connected components", "redundant connection", "accounts merge", "is it one group?".
- **Why:** near-O(1) union/find with path compression + rank; union returning False = cycle.
- **Template:** `UnionFind`
- **Complexity:** ~O(α(n)) per op (near constant)
- **Anchors:** Number of Connected Components, Redundant Connection
- **Trap:** always union ROOTS, not raw nodes; add path compression or it degrades.

## 15. DP 1D (rolling state)
- **Trigger:** "how many ways", "min/max to reach", "can you reach", 1 changing index, "rob/steps/decode".
- **Why:** answer at i depends on a few earlier answers → keep them in rolling variables.
- **Template:** `climb_stairs`, `rob`
- **Complexity:** O(n) time, O(1) space (rolled) — else O(n) space
- **Anchors:** Climbing Stairs, House Robber
- **Trap:** define dp[i] in one English sentence FIRST; nail base cases dp[0], dp[1].

## 16. DP 2D (grid / two sequences)
- **Trigger:** "two strings/arrays compared", "edit distance", "grid paths", "subsequence", "knapsack".
- **Why:** dp[i][j] answers the subproblem on prefixes i and j; fill the table by recurrence.
- **Template:** `longest_common_subsequence`
- **Complexity:** O(m·n) time, O(m·n) space (often O(n) rollable)
- **Anchors:** Longest Common Subsequence, Unique Paths
- **Trap:** off-by-one — size the table (m+1)×(n+1) and index the string with i-1.

## 17. Intervals (sort then sweep)
- **Trigger:** "intervals", "meeting rooms", "merge overlapping", "insert interval", "non-overlapping".
- **Why:** sort by start (or end) so overlaps become adjacent and a single pass resolves them.
- **Template:** `merge_intervals`
- **Complexity:** O(n log n) time, O(n) space
- **Anchors:** Merge Intervals, Insert Interval
- **Trap:** decide sort key (start vs end); overlap test is `start <= prev_end`.

## 18. Greedy (local best → global best)
- **Trigger:** "minimum number of", "can you reach", "maximum ... one pass", "jump", "gas station".
- **Why:** a provable local choice never needs revisiting — track a running best/reach.
- **Template:** `can_jump`
- **Complexity:** O(n) time, O(1) space
- **Anchors:** Jump Game, Merge Intervals (greedy sweep)
- **Trap:** greedy is only correct when the local-choice property holds — if unsure, it's probably DP.

## 19. Bit Manipulation (XOR / masks)
- **Trigger:** "single number", "count bits", "without extra space", "subsets via bitmask", "missing number".
- **Why:** XOR cancels pairs; `n & (n-1)` clears the lowest set bit.
- **Template:** `single_number`, `count_bits`
- **Complexity:** O(n) time, O(1) space
- **Anchors:** Single Number, Number of 1 Bits
- **Trap:** know the identities cold: `x^x=0`, `x^0=x`, `n&(n-1)` drops a bit.

---

### Coverage note
These 19 cards cover every Blind 75 topic. `02_anchor_problems.md` maps each card to
its anchor problems and confirms no Blind 75 problem falls outside a card.
