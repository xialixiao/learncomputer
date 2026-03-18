#263. 丑数
# 丑数 就是只包含质因数 2、3 和 5 的 正 整数。
# 给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。
class Solution:
    def isUgly(self, n: int) -> bool:
        if n<1:
            return False
        while n%5==0:
            n//=5
        while n%3==0:
            n//=3
        while n%2==0:
            n//=2
        return n==1
#264. 丑数 II
# 给你一个整数 n ，请你找出并返回第 n 个 丑数 。
# 丑数 就是质因子只包含 2、3 和 5 的正整数。
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = res[a] * 2, res[b] * 3, res[c] * 5
            res[i] = min(n2, n3, n5)
            if res[i] == n2: a += 1
            if res[i] == n3: b += 1
            if res[i] == n5: c += 1
        return res[-1]
#268. 丢失的数字    
#给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #1.原地哈希
        n=len(nums)
        for i in range(n):
            while nums[i]!=i and nums[i]!=n:
                #对于不属于该位置的数据进行换位操作
                j=nums[i]
                nums[i]=nums[j]
                nums[j]=j
        #最后遍历看看是否有错
        for i in range(n):
            if nums[i]!=i:
                return i
        return n

 

