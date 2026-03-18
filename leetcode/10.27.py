#273. 整数转换英文表示
#将非负整数 num 转换为其对应的英文表示。
ones = ("", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen")
tens = ("", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety")
large_numbers = ("", "Thousand", "Million", "Billion")

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ans = []

        # 1_234_567_811
        # One Billion + Two Hundred Thirty Four Million + Five Hundred Sixty Seven Thousand + Eight Hundred Eleven
        # 拆分后，都是小于 1000 的数 + 大数单位（Billion/Million/Thousand/空）
        for i in range(len(large_numbers) - 1, -1, -1):
            x = num // 10 ** (i * 3) % 1000
            if x == 0:
                continue
            # 百位
            if x >= 100:
                ans.append(ones[x // 100])
                ans.append("Hundred")
            # 十位和个位
            if x % 100 < 20:  # 特殊处理小于 20 的数
                ans.append(ones[x % 100])
            else:
                ans.append(tens[x // 10 % 10])
                ans.append(ones[x % 10])
            ans.append(large_numbers[i])  # 大数单位

        return ' '.join(s for s in ans if s)
#274. H 指数
# 给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。计算并返回该研究者的 h 指数。
# 根据维基百科上 h 指数的定义：h 代表“高引用次数” ，一名科研人员的 h 指数 是指他（她）至少发表了 h 篇论文，并且 至少 有 h 篇论文被引用次数大于等于 h 。如果 h 有多种可能的值，h 指数 是其中最大的那个。
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        cnt = [0] * (n + 1)
        for c in citations:
            cnt[min(c, n)] += 1  # 引用次数 > n，等价于引用次数为 n
        s = 0
        for i in range(n, -1, -1):  # i=0 的时候，s>=i 一定成立
            s += cnt[i]
            if s >= i:  # 说明有至少 i 篇论文的引用次数至少为 i
                return i
#275. H 指数 II
# 给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数，citations 已经按照 非降序排列 。计算并返回该研究者的 h 指数。
# h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （n 篇论文中）至少 有 h 篇论文分别被引用了至少 h 次。
# 请你设计并实现对数时间复杂度的算法解决此问题。
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        low,high=0,n-1
        while low<=high:
            mid=(low+high)//2
            if citations[mid]>=n-mid:
                high=mid-1
            else:
                low=mid+1
        return n-low            
#278. 第一个错误的版本        
# 你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。
# 假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
# 你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i,j=1,n
        while i<=j:
            m=(i+j)//2
            #如果是错误版本
            if isBadVersion(m):
                j=m-1
            #如果是正确版本
            else:
                i=m+1
        return i
#279. 完全平方数
# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
# 写在外面，多个测试数据之间可以共享，减少计算量
@cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
def dfs(i: int, j: int) -> int:
    if i == 0:
        return inf if j else 0
    if j < i * i:
        return dfs(i - 1, j)  # 只能不选
    return min(dfs(i - 1, j), dfs(i, j - i * i) + 1)  # 不选 vs 选

class Solution:
    def numSquares(self, n: int) -> int:
        return dfs(isqrt(n), n)
        
