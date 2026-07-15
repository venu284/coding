"""
TEMPLATE BANK — memorize these skeletons cold.

Rule: you should be able to type each template from a blank file in < 2 min.
Every template is REAL, RUNNABLE, and TESTED. Run this file before you trust it:

    python3 patterns/01_template_bank.py

If it prints "ALL TEMPLATES PASS", the skeletons below are correct.
Memorize the SHAPE (variable names, loop structure, boundary conditions), not
the specific problem. Each function is the minimal correct form of its pattern.
"""

from collections import defaultdict, Counter, deque
from typing import List, Optional
import heapq


# ============================================================
# 1. HASHING — lookup / frequency / group. Turns O(n^2) into O(n).
# ============================================================
def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}                              # value -> index
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))             # canonical form is the hash key
        groups[key].append(s)
    return list(groups.values())


# ============================================================
# 2. TWO POINTERS — sorted array, pair/triple, opposite ends.
# ============================================================
def two_sum_sorted(nums: List[int], target: int) -> List[int]:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        total = nums[lo] + nums[hi]
        if total == target:
            return [lo, hi]
        elif total < target:
            lo += 1                        # need bigger -> move left up
        else:
            hi -= 1                        # need smaller -> move right down
    return []


# ============================================================
# 3. SLIDING WINDOW — longest/shortest contiguous run under a constraint.
# ============================================================
def longest_unique_substring(s: str) -> int:
    last = {}                              # char -> last index seen
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1            # shrink: jump past the duplicate
        last[ch] = right
        best = max(best, right - left + 1)
    return best


# ============================================================
# 4. BINARY SEARCH — sorted space OR "search on the answer".
# ============================================================
def binary_search(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1              # inclusive both ends
    while lo <= hi:
        mid = lo + (hi - lo) // 2          # avoids overflow in other langs
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def lower_bound(nums: List[int], target: int) -> int:
    """Leftmost index where target could be inserted (first >= target)."""
    lo, hi = 0, len(nums)                  # half-open [lo, hi)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


# ============================================================
# 5. STACK — matching/nesting; MONOTONIC stack for next-greater.
# ============================================================
def valid_parentheses(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack


def daily_temperatures(temps: List[int]) -> List[int]:
    ans = [0] * len(temps)
    stack = []                             # indices, temps DECREASING down the stack
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)
    return ans


# ============================================================
# 6. LINKED LIST — dummy head, reverse, fast/slow.
# ============================================================
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        nxt = curr.next                    # save
        curr.next = prev                   # reverse pointer
        prev = curr                        # advance both
        curr = nxt
    return prev


def has_cycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


# ============================================================
# 7. TREE DFS — bottom-up recursion: get info from children, combine.
# ============================================================
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# ============================================================
# 8. TREE BFS — level-order with a deque.
# ============================================================
def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):            # freeze the level size
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)
    return result


# ============================================================
# 9. TRIE — prefix tree for word/prefix lookup.
# ============================================================
class Trie:
    def __init__(self):
        self.root = {}                     # nested dicts; "$" marks word end

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return "$" in node

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True


# ============================================================
# 10. HEAP — top-K (heap of size K) and streaming.
# ============================================================
def top_k_frequent(nums: List[int], k: int) -> List[int]:
    freq = Counter(nums)
    # min-heap of size k: push (count, val), pop smallest when over k
    heap = []
    for val, count in freq.items():
        heapq.heappush(heap, (count, val))
        if len(heap) > k:
            heapq.heappop(heap)
    return [val for count, val in heap]


# ============================================================
# 11. BACKTRACKING — build partial solution, recurse, undo (choose/explore/unchoose).
# ============================================================
def subsets(nums: List[int]) -> List[List[int]]:
    result = []
    path = []

    def backtrack(start: int) -> None:
        result.append(path[:])             # every node is a valid subset
        for i in range(start, len(nums)):
            path.append(nums[i])           # choose
            backtrack(i + 1)               # explore
            path.pop()                     # unchoose

    backtrack(0)
    return result


def permutations(nums: List[int]) -> List[List[int]]:
    result = []
    path = []
    used = [False] * len(nums)

    def backtrack() -> None:
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return result


# ============================================================
# 12. GRAPH — grid flood fill (DFS). Visited via mutation or a set.
# ============================================================
def num_islands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"                   # mark visited
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)
    return count


# ============================================================
# 13. TOPOLOGICAL SORT — Kahn's (BFS on in-degree). Detects cycles.
# ============================================================
def can_finish(num_courses: int, prereqs: List[List[int]]) -> bool:
    adj = defaultdict(list)
    indegree = [0] * num_courses
    for course, need in prereqs:
        adj[need].append(course)           # need -> course
        indegree[course] += 1
    q = deque(c for c in range(num_courses) if indegree[c] == 0)
    done = 0
    while q:
        node = q.popleft()
        done += 1
        for nxt in adj[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
    return done == num_courses             # all taken => no cycle


# ============================================================
# 14. UNION-FIND — connectivity / cycle in undirected graph.
# ============================================================
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]   # path compression
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False                   # already connected -> cycle
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True


# ============================================================
# 15. DP 1D — climbing-stairs / house-robber shape (rolling variables).
# ============================================================
def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    a, b = 1, 2                            # ways to reach step 1, step 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def rob(nums: List[int]) -> int:
    prev, curr = 0, 0                      # best up to i-2, best up to i-1
    for num in nums:
        prev, curr = curr, max(curr, prev + num)
    return curr


# ============================================================
# 16. DP 2D — grid / two-sequence table.
# ============================================================
def longest_common_subsequence(a: str, b: str) -> int:
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[len(a)][len(b)]


# ============================================================
# 17. INTERVALS — sort by start, merge overlaps.
# ============================================================
def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:         # overlap
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


# ============================================================
# 18. GREEDY — local best -> global best (jump game reachability).
# ============================================================
def can_jump(nums: List[int]) -> bool:
    reach = 0
    for i, jump in enumerate(nums):
        if i > reach:                      # cannot even arrive at i
            return False
        reach = max(reach, i + jump)
    return True


# ============================================================
# 19. BIT MANIPULATION — XOR cancels pairs; & isolates bits.
# ============================================================
def single_number(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num                      # pairs cancel, loner remains
    return result


def count_bits(num: int) -> int:
    count = 0
    while num:
        num &= num - 1                     # drop lowest set bit
        count += 1
    return count


# ============================================================
# TESTS — this is the point. Run this file; every assert must pass.
# ============================================================
def _build_list(vals):
    dummy = ListNode()
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def _list_to_array(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    # 1. hashing
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert sorted(map(sorted, group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))) == \
        sorted(map(sorted, [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]))

    # 2. two pointers
    assert two_sum_sorted([1, 2, 3, 4, 6], 6) == [1, 3]
    assert two_sum_sorted([2, 3, 4], 6) == [0, 2]

    # 3. sliding window
    assert longest_unique_substring("abcabcbb") == 3
    assert longest_unique_substring("bbbbb") == 1
    assert longest_unique_substring("pwwkew") == 3
    assert longest_unique_substring("") == 0

    # 4. binary search
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert lower_bound([1, 2, 4, 4, 5], 4) == 2
    assert lower_bound([1, 2, 4, 4, 5], 3) == 2
    assert lower_bound([1, 2, 3], 9) == 3

    # 5. stack
    assert valid_parentheses("()[]{}") is True
    assert valid_parentheses("(]") is False
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]

    # 6. linked list
    assert _list_to_array(reverse_list(_build_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    _cyc = _build_list([1, 2, 3])
    assert has_cycle(_cyc) is False
    _cyc.next.next.next = _cyc            # make a cycle
    assert has_cycle(_cyc) is True

    # 7/8. trees
    _t = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(_t) == 3
    assert level_order(_t) == [[3], [9, 20], [15, 7]]

    # 9. trie
    _tr = Trie()
    _tr.insert("apple")
    assert _tr.search("apple") is True
    assert _tr.search("app") is False
    assert _tr.starts_with("app") is True
    assert _tr.starts_with("xyz") is False

    # 10. heap
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]

    # 11. backtracking
    assert sorted(map(sorted, subsets([1, 2, 3]))) == \
        sorted(map(sorted, [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]))
    assert len(permutations([1, 2, 3])) == 6

    # 12. graph flood fill
    _grid = [
        list("11110"),
        list("11010"),
        list("11000"),
        list("00000"),
    ]
    assert num_islands(_grid) == 1
    _grid2 = [
        list("11000"),
        list("11000"),
        list("00100"),
        list("00011"),
    ]
    assert num_islands(_grid2) == 3

    # 13. topological sort
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False

    # 14. union-find
    _uf = UnionFind(3)
    assert _uf.union(0, 1) is True
    assert _uf.union(1, 2) is True
    assert _uf.union(0, 2) is False        # already connected
    assert _uf.find(0) == _uf.find(2)

    # 15. dp 1d
    assert climb_stairs(5) == 8
    assert rob([2, 7, 9, 3, 1]) == 12

    # 16. dp 2d
    assert longest_common_subsequence("abcde", "ace") == 3

    # 17. intervals
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]

    # 18. greedy
    assert can_jump([2, 3, 1, 1, 4]) is True
    assert can_jump([3, 2, 1, 0, 4]) is False

    # 19. bits
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert count_bits(11) == 3             # 1011 -> three set bits

    print("ALL TEMPLATES PASS")
