"""Runnable DSA concept templates.

Run:
    python3 concepts/03_template_bank.py
"""

from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from heapq import heappop, heappush
from math import inf


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []


def frequency_map(items):
    return Counter(items)


def group_by_key(items, key_fn):
    groups = defaultdict(list)
    for item in items:
        groups[key_fn(item)].append(item)
    return dict(groups)


def prefix_sums(nums):
    pref = [0]
    for num in nums:
        pref.append(pref[-1] + num)
    return pref


def range_sum(prefix, left, right):
    return prefix[right + 1] - prefix[left]


def binary_search_left(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def search_on_answer(lo, hi, can):
    while lo < hi:
        mid = (lo + hi) // 2
        if can(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        if total < target:
            left += 1
        else:
            right -= 1
    return []


def longest_unique_substring(s):
    seen = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        best = max(best, right - left + 1)
    return best


def daily_temperatures(temps):
    ans = [0] * len(temps)
    stack = []
    for i, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)
    return ans


def sliding_window_max(nums, k):
    q = deque()
    ans = []
    for i, num in enumerate(nums):
        while q and q[0] <= i - k:
            q.popleft()
        while q and nums[q[-1]] <= num:
            q.pop()
        q.append(i)
        if i >= k - 1:
            ans.append(nums[q[0]])
    return ans


@dataclass
class ListNode:
    val: int
    next: object = None


def reverse_list(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


@dataclass
class TreeNode:
    val: int
    left: object = None
    right: object = None


def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def level_order(root):
    if not root:
        return []
    ans = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level)
    return ans


def top_k_frequent(nums, k):
    heap = []
    for num, count in Counter(nums).items():
        heappush(heap, (count, num))
        if len(heap) > k:
            heappop(heap)
    return [num for _, num in sorted(heap, reverse=True)]


class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def add_num(self, num):
        heappush(self.small, -num)
        heappush(self.large, -heappop(self.small))
        if len(self.large) > len(self.small):
            heappush(self.small, -heappop(self.large))

    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True


def graph_bfs(adj, start):
    seen = {start}
    q = deque([start])
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nei in adj[node]:
            if nei not in seen:
                seen.add(nei)
                q.append(nei)
    return order


def graph_dfs(adj, start):
    seen = set()
    order = []

    def dfs(node):
        seen.add(node)
        order.append(node)
        for nei in adj[node]:
            if nei not in seen:
                dfs(nei)

    dfs(start)
    return order


def topo_sort(n, edges):
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    for pre, course in edges:
        adj[pre].append(course)
        indeg[course] += 1
    q = deque(i for i, deg in enumerate(indeg) if deg == 0)
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nei in adj[node]:
            indeg[nei] -= 1
            if indeg[nei] == 0:
                q.append(nei)
    return order if len(order) == n else []


def dijkstra(adj, source):
    dist = defaultdict(lambda: inf)
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        cost, node = heappop(heap)
        if cost != dist[node]:
            continue
        for nei, weight in adj[node]:
            new_cost = cost + weight
            if new_cost < dist[nei]:
                dist[nei] = new_cost
                heappush(heap, (new_cost, nei))
    return dict(dist)


def subsets(nums):
    ans = []
    path = []

    def backtrack(i):
        if i == len(nums):
            ans.append(path[:])
            return
        backtrack(i + 1)
        path.append(nums[i])
        backtrack(i + 1)
        path.pop()

    backtrack(0)
    return ans


def house_robber(nums):
    prev2 = 0
    prev1 = 0
    for num in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + num)
    return prev1


def longest_common_subsequence(a, b):
    prev = [0] * (len(b) + 1)
    for i in range(1, len(a) + 1):
        cur = [0] * (len(b) + 1)
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                cur[j] = prev[j - 1] + 1
            else:
                cur[j] = max(prev[j], cur[j - 1])
        prev = cur
    return prev[-1]


def can_jump(nums):
    farthest = 0
    for i, jump in enumerate(nums):
        if i > farthest:
            return False
        farthest = max(farthest, i + jump)
    return True


def single_number(nums):
    ans = 0
    for num in nums:
        ans ^= num
    return ans


def count_bits(n):
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return "$" in node

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True


def merge_sort(nums):
    if len(nums) <= 1:
        return nums[:]
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    ans = []
    i = j = 0
    while i < len(left) or j < len(right):
        if j == len(right) or (i < len(left) and left[i] <= right[j]):
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1
    return ans


def max_overlap(intervals):
    events = []
    for start, end in intervals:
        events.append((start, 1))
        events.append((end, -1))
    active = best = 0
    for _, delta in sorted(events, key=lambda x: (x[0], x[1])):
        active += delta
        best = max(best, active)
    return best


class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        for i, num in enumerate(nums):
            self.tree[self.n + i] = num
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        pos = index + self.n
        self.tree[pos] = value
        pos //= 2
        while pos:
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]
            pos //= 2

    def query(self, left, right):
        left += self.n
        right += self.n
        total = 0
        while left <= right:
            if left % 2 == 1:
                total += self.tree[left]
                left += 1
            if right % 2 == 0:
                total += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return total


class FenwickTree:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def add(self, index, delta):
        index += 1
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & -index

    def prefix_sum(self, index):
        index += 1
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total

    def range_sum(self, left, right):
        return self.prefix_sum(right) - (self.prefix_sum(left - 1) if left else 0)


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.left = [0, 0]
        self.right = [0, 0]
        self.left[1] = self.right
        self.right[0] = self.left

    def _remove(self, node):
        prev, nxt = node[0], node[1]
        prev[1] = nxt
        nxt[0] = prev

    def _insert_right(self, node):
        prev = self.right[0]
        prev[1] = node
        node[0] = prev
        node[1] = self.right
        self.right[0] = node

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_right(node)
        return node[3]

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = [None, None, key, value]
        self.cache[key] = node
        self._insert_right(node)
        if len(self.cache) > self.capacity:
            lru = self.left[1]
            self._remove(lru)
            del self.cache[lru[2]]


def kmp_prefix(pattern):
    pi = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    return pi


def _list_values(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals


def _run_tests():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert frequency_map("banana")["a"] == 3
    grouped = group_by_key(["eat", "tea", "bat"], lambda s: "".join(sorted(s)))
    assert sorted(grouped["aet"]) == ["eat", "tea"]
    pref = prefix_sums([1, 2, 3, 4])
    assert pref == [0, 1, 3, 6, 10]
    assert range_sum(pref, 1, 3) == 9
    assert binary_search_left([1, 3, 3, 5], 3) == 1
    assert search_on_answer(1, 10, lambda x: x >= 6) == 6
    assert two_sum_sorted([2, 7, 11, 15], 9) == [0, 1]
    assert longest_unique_substring("abcabcbb") == 3
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]

    head = ListNode(1, ListNode(2, ListNode(3)))
    assert _list_values(reverse_list(head)) == [3, 2, 1]
    cyc = ListNode(1, ListNode(2))
    cyc.next.next = cyc
    assert has_cycle(cyc) is True

    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert max_depth(root) == 2
    assert inorder(root) == [1, 2, 3]
    assert level_order(root) == [[2], [1, 3]]

    assert set(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    mf = MedianFinder()
    for num in [1, 2, 3]:
        mf.add_num(num)
    assert mf.find_median() == 2

    uf = UnionFind(3)
    assert uf.union(0, 1) is True
    assert uf.union(1, 2) is True
    assert uf.union(0, 2) is False

    adj = {0: [1, 2], 1: [2], 2: []}
    assert graph_bfs(adj, 0) == [0, 1, 2]
    assert graph_dfs(adj, 0) == [0, 1, 2]
    assert topo_sort(3, [(0, 1), (1, 2)]) == [0, 1, 2]
    weighted = {"a": [("b", 2), ("c", 5)], "b": [("c", 1)], "c": []}
    assert dijkstra(weighted, "a")["c"] == 3

    assert sorted(subsets([1, 2])) == [[], [1], [1, 2], [2]]
    assert house_robber([2, 7, 9, 3, 1]) == 12
    assert longest_common_subsequence("abcde", "ace") == 3
    assert can_jump([2, 3, 1, 1, 4]) is True
    assert can_jump([3, 2, 1, 0, 4]) is False
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert count_bits(5) == [0, 1, 1, 2, 1, 2]

    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.starts_with("app") is True
    assert merge_sort([5, 2, 3, 1]) == [1, 2, 3, 5]
    assert max_overlap([(0, 30), (5, 10), (15, 20)]) == 2

    seg = SegmentTree([1, 3, 5])
    assert seg.query(0, 2) == 9
    seg.update(1, 2)
    assert seg.query(0, 2) == 8

    bit = FenwickTree(4)
    for i, num in enumerate([1, 2, 3, 4]):
        bit.add(i, num)
    assert bit.range_sum(1, 3) == 9

    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1

    assert kmp_prefix("ababaca") == [0, 0, 1, 2, 3, 0, 1]


if __name__ == "__main__":
    _run_tests()
    print("ALL CONCEPT TEMPLATES PASS")
