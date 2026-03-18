#211. 添加与搜索单词 - 数据结构设计
# 请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。
# 实现词典类 WordDictionary ：
# WordDictionary() 初始化词典对象
# void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
# bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。
class Node:
    def __init__(self):
        self.son = dict()
        self.end = False
    
class WordDictionary:
    # 时间复杂度O(nlogn)
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.son:
                cur.son[c] = Node()
            cur = cur.son[c]
        cur.end = True

    def search(self, word: str) -> bool:
        return self.match(word, 0, self.root)

    def match(self, word: str, idx: int, cur: Node) -> bool:
        if idx == len(word):
            return cur.end

        c = word[idx]
        if c != '.':
            if c not in cur.son:
                return False
            else:
                return self.match(word, idx + 1, cur.son[c])
            
        return any(self.match(word, idx + 1, node) for node in cur.son.values())
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
#212. 单词搜索 II
# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words， 返回所有二维网格上的单词 。
# 单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        directions = ((0,1), (0,-1), (1,0), (-1,0))
        m, n = len(board), len(board[0])
        
        # 预处理：记录每个字母在 board 中的位置
        start = defaultdict(list)
        for i in range(m):
            for j in range(n):
                start[board[i][j]].append((i, j))

        # DFS 尝试匹配单词
        def dfs(i, j, word, index):
            if index == len(word) - 1:
                return True
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj] and board[ni][nj] == word[index + 1]:
                    visited[ni][nj] = True
                    if dfs(ni, nj, word, index + 1):
                        return True
                    visited[ni][nj] = False
            return False

        ans = []
        for word in words:
            # 剪枝 1：字符检查
            if any(c not in start for c in word):
                continue

            # 剪枝 2：逆序判断
            rev = False
            if len(start[word[-1]]) < len(start[word[0]]):
                word = word[::-1]
                rev = True

            # 对所有起点尝试 DFS
            for i, j in start[word[0]]:
                visited = [[False] * n for _ in range(m)]
                visited[i][j] = True
                if dfs(i, j, word, 0):
                    ans.append(word[::-1] if rev else word)
                    break

        return ans
#213. 打家劫舍 II
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
class Solution:
    def rob(self, nums: List[int]) -> int:
        def cun(nums):
            cur,pre=0,0
            for num in nums:
                cur,pre=max(pre+num,cur),cur
            return cur
        return max(cun(nums[:-1]),cun(nums[1:])) if len(nums)!=1 else nums[0]
#214. 最短回文串      
#给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reverse=s[::-1]
        for i in range(len(s)+1):
            #startswith用于检查一个字符串是否以指定的前缀开始。如果以该前缀开头，则返回 true
            if s.startswith(reverse[i:]):
                return reverse[:i]+s
#215. 数组中的第K个最大元素
# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]
#216. 组合总和 III
# 找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：
# 只使用数字1到9
# 每个数字 最多使用一次 
# 返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i: int, left_sum: int) -> None:
            d = k - len(path)  # 还要选 d 个数
            if left_sum < 0 or left_sum > (i * 2 - d + 1) * d // 2:  # 剪枝
                return
            if d == 0:  # 找到一个合法组合
                ans.append(path.copy())
                return
            # 枚举的数不能太小，否则后面没有数可以选
            for j in range(i, d - 1, -1):
                path.append(j)
                dfs(j - 1, left_sum - j)
                path.pop()  # 恢复现场

        dfs(9, n)  # 从 i=9 开始倒着枚举
        return ans
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i: int, left_sum: int) -> None:
            d = k - len(path)  # 还要选 d 个数
            if left_sum < 0 or left_sum > (i * 2 - d + 1) * d // 2:  # 剪枝
                return
            if d == 0:  # 找到一个合法组合
                ans.append(path.copy())
                return

            # 不选 i
            if i > d:
                dfs(i - 1, left_sum)

            # 选 i
            path.append(i)
            dfs(i - 1, left_sum - i)
            path.pop()

        dfs(9, n)
        return ans
#217. 存在重复元素
#给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))
#218. 天际线问题
# 城市的 天际线 是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回 由这些建筑物形成的 天际线 。
# 每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti] 表示：
# lefti 是第 i 座建筑物左边缘的 x 坐标。
# righti 是第 i 座建筑物右边缘的 x 坐标。
# heighti 是第 i 座建筑物的高度。
# 你可以假设所有的建筑都是完美的长方形，在高度为 0 的绝对平坦的表面上。
# 天际线 应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标 进行 排序 。关键点是水平线段的左端点。列表中最后一个点是最右侧建筑物的终点，y 坐标始终为 0 ，仅用于标记天际线的终点。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。
# 注意：输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        buildings.sort(key = lambda x: x[0])
        xset = [] # 换成数组从而减小时间常数
        for l, r, _ in buildings:
            xset.append(l)
            xset.append(r)
        h = []
        ans = []
        i = 0
        n = len(buildings)
        for x in sorted(xset):
            while i < n and buildings[i][0] <= x:
                heappush(h, (-buildings[i][2], buildings[i][1]))
                i += 1
            while h and h[0][1] <= x:
                heappop(h)
            height = -h[0][0] if h else 0
            if not ans or ans[-1][1] != height:
                ans.append([x, height])
        return ans
#219. 存在重复元素 II
#给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last={}
        for i,x in enumerate(nums):
            if x in last and i-last[x]<=k:
                return True
            last[x]=i
        return False
#220. 存在重复元素 III          
# 给你一个整数数组 nums 和两个整数 indexDiff 和 valueDiff 。
# 找出满足下述条件的下标对 (i, j)：
# i != j,
# abs(i - j) <= indexDiff
# abs(nums[i] - nums[j]) <= valueDiff
# 如果存在，返回 true ；否则，返回 false 。
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucket = dict()
        if t < 0: return False
        for i in range(len(nums)):
            nth = nums[i] // (t + 1)
            if nth in bucket:
                return True
            if nth - 1 in bucket and abs(nums[i] - bucket[nth - 1]) <= t:
                return True
            if nth + 1 in bucket and abs(nums[i] - bucket[nth + 1]) <= t:
                return True
            bucket[nth] = nums[i]
            if i >= k: bucket.pop(nums[i - k] // (t + 1))
        return False


 
