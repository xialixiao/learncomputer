#51. N 皇后
# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
class Solution:
    def solveNQueens(self,n:int)->List[List[str]]:
        ans=[]
        queens=[0]*n #皇后放在（r，queens[r])
        col=[False]*n
        diag1=[False]*(n*2-1)
        diag2=[False]*(n*2-1)
        def dfs(r:int)->None:
            if r==n:
                ans.append(['.'*c+'Q'+'.'*(n-1-c) for c in queens])
                return
        #在（r,c)放皇后
        for c,ok in enumerate(col):
            if not ok and not diag1[r+c] and not diag2[r-c]: #判断是否放皇后
                queens[r]=c #直接覆盖，无需会反复现场
                col[c]=diag1[r+c]=diag2[r-c]=True #皇后占用了c列，和两条斜线
                dfs(r+1)
                col[c] = diag1[r + c] = diag2[r - c] = False  # 恢复现场
        dfs(0)
        return ans
#52. N 皇后 II
# n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。
#大神做法：排列型回溯
class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        col = [False] * n
        diag1 = [False] * (n * 2 - 1)
        diag2 = [False] * (n * 2 - 1)
        def dfs(r: int) -> None:
            if r == n:
                nonlocal ans
                ans += 1  # 找到一个合法方案
                return
            for c, ok in enumerate(col):
                if not ok and not diag1[r + c] and not diag2[r - c]:
                    col[c] = diag1[r + c] = diag2[r - c] = True
                    dfs(r + 1)
                    col[c] = diag1[r + c] = diag2[r - c] = False  # 恢复现场
        dfs(0)
        return ans
#53. 最大子数组和
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组是数组中的一个连续部分。
#第一种做法
class Solution:
    def maxSubArray(self,nums:List[int])->int:
        ans=-inf
        min_pro_sum=pre_sum=0
        for x in nums:
            pre_sum+=x  #当前前缀和
            ans=max(ans,pre_sum-min_pro_sum)  #减去前缀和的最小值
            min_pro_sum=min(min_pro_sum,pre_sum)  #维护前缀和的最小值
        return ans
#第二种做法：动态规划的思想
#2.利用动态规划的思想
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        f=[0]*len(nums)
        f[0]=nums[0]
        for i in range(1,len(nums)):
            f[i]=max(f[i-1],0)+nums[i]
        return max(f)
#3.空间优化
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf  # 注意答案可以是负数，不能初始化成 0
        f = 0
        for x in nums:
            f = max(f, 0) + x
            ans = max(ans, f)
        return ans
#54. 螺旋矩阵
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:return []
        l,r,t,b,res=0,len(matrix[0])-1,0,len(matrix)-1,[]
        while True:
            for i in range(l,r+1):
                res.append(matrix[t][i]) #第一行,此时t要往下走了
            t+=1
            if t>b:break #走完了
            for i in range(t,b+1):
                res.append(matrix[i][r])
            r-=1
            if l>r:break
            for i in range(r,l-1,-1):
                res.append(matrix[b][i])
            b-=1
            if t>b:break
            for i in range(b,t-1,-1):
                res.append(matrix[i][l])
            l+=1
            if l>r:break
        return res
#55. 跳跃游戏
# 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
class Solution:
    def canJump(self,nums:List[int])->bool:
        mx=0
        for i,jump in enumerate(nums):
            if i>mx:
                return False
            mx=max(nx,i+jump)
            if mx>=len(nums)-1:
                return True
#56. 合并区间  
#     以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。    
class Solution:
    def merge(self,intervals:List[List[int]])->List[List[int]]:
        intervals.sort(key=lambda p:p[0]) #按照左端点从小到大排序
        ans=[]
        for p in intervals:
            if ans and p[0]<ans[-1][1]:
                ans[-1][1]=max(a[-1][1],p[1])
            else:#不相交，无法合并
                ans.appedn(p) #新的合并区间
        return ans 
#57. 插入区间
# 给你一个 无重叠的 ，按照区间起始端点排序的区间列表 intervals，其中 intervals[i] = [starti, endi] 表示第 i 个区间的开始和结束，并且 intervals 按照 starti 升序排列。同样给定一个区间 newInterval = [start, end] 表示另一个区间的开始和结束。
# 在 intervals 中插入区间 newInterval，使得 intervals 依然按照 starti 升序排列，且区间之间不重叠（如果有必要的话，可以合并区间）。
# 返回插入之后的 intervals。
# 注意 你不需要原地修改 intervals。你可以创建一个新数组然后返回它。
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda p:p[0])  #按照左端点从小到大排序
        ans=[]
        for p in intervals:
            if ans and p[0]<=ans[-1][1]:#可以，新的元素左端点不大于右端点，可以合并
                ans[-1][1]=max(ans[-1][1],p[1])   #更新右端最大值
            else:  #不相交，无法合并
                ans.append(p)      #新的合并区间
        return ans     
#58. 最后一个单词的长度
# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。
#单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
#split() 函数用于将字符串按照指定的分隔符拆分为多个子字符串，并返回一个列表。它是处理字符串的常用方法。
#59. 螺旋矩阵 II
#给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l,r,t,b=0,n-1,0,n-1
        #按照所给的n创建要求的全是0的矩阵
        res=[[0 for _ in range(n)] for _ in range(n)]
        num=1
        while num<=n*n:
            for i in range(l,r+1):
                res[t][i]=num
                num+=1
            t+=1
            for i in range(t,b+1):
                res[i][r]=num
                num+=1
            r-=1
            for i in range(r,l-1,-1):
                res[b][i]=num
                num+=1
            b-=1
            for i in range(b,t-1,-1):
                res[i][l]=num
                num+=1
            l+=1
        return res
# 60. 排列序列
# 给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 给定 n 和 k，返回第 k 个排列。
class Solution:
    def getPermutation(self,n:int,k:int)->str:
        #初始化数字列表
        nums=list(range(1,n+1))
        #转化为从0开始的索引
        k-=1
        result=[]
        #构造排列
        for i in range(n,0,-1):
            fact=factorial(i-1)
            index=k//fact
            result.append(str(nums.pop(index)))
            k%=fact
        return ''.join(result)
# math.factorial()方法是Python标准库中math模块的一部分，它接受一个正整数作为参数，并返回该数的阶乘。如果传入的参数是负数或非整数，则会抛出ValueError异常。如果传入的参数是0，则按照数学定义，其阶乘结果为1。