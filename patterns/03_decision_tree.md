# Decision Tree — problem → pattern in under 2 minutes

This is what you run in the first 2 minutes of every interview. Read the problem,
walk these questions top to bottom, stop at the first YES. This is the skill that
separates "I've seen this" from "I can solve anything."

## Step 0 — Extract the signal
Before matching, note: input type (array / string / tree / graph / linked list),
whether it's **sorted**, the **constraints** (n ≤ 20 → exponential OK; n up to 1e5 →
need O(n log n) or better), and the **ask** (count / min-max / all-solutions / yes-no / exact-item).

## Step 1 — Walk the questions

```
Is the input a GRAPH or GRID?
├─ dependencies / ordering / prerequisites?      → Topological Sort (13)
├─ "are these connected" / components / cycle?   → Union-Find (14)
├─ shortest path, unweighted?                    → Graph BFS (12)
└─ explore regions / islands / reachability?     → Graph DFS/BFS flood fill (12)

Is it a TREE?
├─ level-by-level / right view / min depth?      → Tree BFS (8)
└─ depth / path / validate / compare subtrees?   → Tree DFS bottom-up (7)

Is it a LINKED LIST?                              → Linked List: dummy/reverse/fast-slow (6)

Is it about PREFIXES / dictionary of words?       → Trie (9)

Does it ask for ALL subsets/permutations/combos
or n is tiny (≤ ~20)?                              → Backtracking (11)

Does it ask "how many ways" / "min/max cost to
reach" / "can you reach" over choices?
├─ two sequences / grid / 2 indices?             → DP 2D (16)
└─ one moving index?                             → DP 1D (15)
    (if a simple local choice is provably optimal → Greedy (18) instead)

Is the array SORTED (or answer is monotonic,
"minimize the max")?                              → Binary Search (4)

INTERVALS / meetings / overlaps?                  → Intervals: sort + sweep (17)

Top-K / K-th / median-of-stream / merge-K?        → Heap (10)

Contiguous subarray/substring with a constraint?  → Sliding Window (3)

Sorted array + find pair/triple, or palindrome,
or in-place two-end work?                          → Two Pointers (2)

"Matching/nesting" or "next greater/smaller"?     → Stack / Monotonic (5)

Bitwise / "single number" / "without extra space"
/ count bits?                                      → Bit Manipulation (19)

DEFAULT / "find / count / seen-before / group"     → Hashing (1)
```

## Step 2 — Constraint sanity check (says your complexity out loud)
| n (input size) | Target complexity | Patterns that fit |
|---|---|---|
| ≤ 12 | O(n!) | Backtracking permutations |
| ≤ 20 | O(2^n) | Backtracking subsets, bitmask DP |
| ≤ 500 | O(n³) | 2D/3D DP |
| ≤ 5,000 | O(n²) | DP, some two-pointer |
| ≤ 1e5–1e6 | O(n log n) / O(n) | sort, heap, sliding window, hashing, binary search |
| ≥ 1e9 (value, not array) | O(log n) | binary search on the answer |

If your first idea's complexity exceeds the target above, it's the wrong pattern — re-walk Step 1.

## Step 3 — Confidence signals (trigger words → pattern)
Fold-in of the full trigger table (single source of truth; supersedes the old plan's table).

| Trigger in the problem | Pattern |
|---|---|
| find pair / group / count / seen-before | Hashing (1) |
| sorted + pair/triple, palindrome, in-place | Two Pointers (2) |
| contiguous subarray/substring, "at most K", longest/shortest such-that | Sliding Window (3) |
| sorted / rotated / "minimize max, maximize min" / O(log n) | Binary Search (4) |
| matching/nesting brackets | Stack (5) |
| next greater/smaller, histogram | Monotonic Stack (5) |
| reverse / middle / cycle / merge lists | Linked List (6) |
| depth / path / subtree info / validate BST | Tree DFS (7) |
| level order / right view / min depth | Tree BFS (8) |
| prefix / starts-with / word dictionary | Trie (9) |
| top-K / K-th / median stream / merge-K | Heap (10) |
| all subsets/permutations/combinations, n ≤ 20 | Backtracking (11) |
| islands / connected region / reachable grid | Graph BFS/DFS (12) |
| prerequisites / build order / cycle in directed | Topological Sort (13) |
| connected components / redundant edge | Union-Find (14) |
| ways / min-max reach, one index | DP 1D (15) |
| two strings/grids, edit distance, subsequence | DP 2D (16) |
| intervals / meetings / overlap | Intervals (17) |
| min-number-of / reach in one pass / jump | Greedy (18) |
| single number / count bits / no extra space | Bit Manipulation (19) |

## The honest fallback
If nothing matches in 2 minutes: state the **brute force** out loud, give its
complexity, then ask "can I trade space for time (hash), exploit sorting (two
pointers / binary search), or is there overlapping subwork (DP)?" — those three
questions convert most brute forces into the intended pattern.
