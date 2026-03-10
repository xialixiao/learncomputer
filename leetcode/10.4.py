#41. 缺失的第一个正数
# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
#第一种做法
class Solution:
    def firstMissingPositive(self,nums:List[int])->int:
        #熬不熬时，全看最小数是不是最小。而且遍历的最大的数，有一定的侥幸
        a=set(nums)
        for i in range(1,len(nums)+3):
            if i not in a:
                return i
#第二种做法
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #第二种：换座位，通过例子理解算法思想
        n=len(nums)
        for i in range(n):
            #如果当前学生的学号在[1,n]中，但（真身）没有坐在正确的座位上
            while 1<=nums[i]<=n and nums[i]!=nums[nums[i]-1]:
                #那么就交换nums[i]和nums[j],其中j是i的学号
                j=nums[i]-1
                nums[i],nums[j]=nums[j],nums[i]
        #找第一个学号与座位编号不匹配的同学
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        #所有学生都坐在正确的座位上
        return n+1      
#42. 接雨水
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#做法1：单调栈
class Solution:
    def trap(self,height:List[int])->int:
        ans=0
        st=[]
        for i,h in enumerate(height):
            while st and h>height[st[-1]]:
                bottom_h=height[st.pop()]
                if not st:
                    break
                left=st[-1]
                dh=min(height[left],h)-bottom_h
                ans+=dh*(i-left+1)
            st.append(i)
        return ans
#2.相向双指针
class Solution:
    def trap(self, height: List[int]) -> int:
        ans=pre_max=suf_max=0
        left,right=0,len(height)-1
        while left<right:
            pre_max=max(pre_max,height[left])
            suf_max=max(suf_max,height[right])
            if pre_max<suf_max:
                ans+=pre_max-height[left]
                left+=1
            else:
                ans+=suf_max-height[right]
                right-=1
        return ans 
#3.大神补充，前后缀分解
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre_max = [0] * n  # pre_max[i] 表示从 height[0] 到 height[i] 的最大值
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])

        suf_max = [0] * n  # suf_max[i] 表示从 height[i] 到 height[n-1] 的最大值
        suf_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i])

        ans = 0
        for h, pre, suf in zip(height, pre_max, suf_max):
            ans += min(pre, suf) - h  # 累加每个水桶能接多少水
        return ans
#43. 字符串相乘
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

# 注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。
#第一种做法
class Solution:
    def multiply(self,num1:str,num2:str)->str:
        return str(int(num1)*int(num2))
#2.复杂一些的做法
class Solution:
    def multiply(self,num1:str,num2:str)->str:
        res=0
        for i in range(1,len(num1)+1):
            for j in range(1,len(num2)+1):
                res+=int(num1[-i])*int(num2[-j])*(10**(i+j-2))
        return str(res)
#44. 通配符匹配
# 给你一个输入字符串 (s) 和一个字符模式 (p) ，请你实现一个支持 '?' 和 '*' 匹配规则的通配符匹配：
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符序列（包括空字符序列）。
# 判定匹配成功的充要条件是：字符模式必须能够 完全匹配 输入字符串（而不是部分匹配）。
#1.记忆化搜索
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        @cache
        def dfs(i: int, j: int) -> bool:
            # 边界判断
            if i < 0: 
                if j < 0: 
                    return True
                if p[j] != '*': 
                    return False
                return dfs(i, j - 1)
            elif j < 0: 
                return False
            
            # 其他语言记忆化位置

            # 状态转移
            if s[i] == p[j] or p[j] == '?': 
                return dfs(i - 1, j - 1)
            elif p[j] == '*':  
                # '*'匹配多个字符 or '*'当成空串 
               return dfs(i - 1, j) or dfs(i, j - 1)
            else:  
                return False

        return dfs(m - 1, n - 1)
#2.二维数组递推 
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        f = [[False] * (n + 1) for _ in range(m + 1)] # f[m + 1][n + 1]

        # 初始条件：翻译自递归边界
        # 对应边界 i<0 and j < 0 return True
        f[0][0] = True
        # 对应边界 i<0 j>=0的处理
        for j in range(n):
            f[0][j + 1] = p[j] == '*' and f[0][j]
        # 对应边界 j<0 (f初始化已经赋值了False, 不用写)
        # for i in range(m):
        #     f[i + 1][0] = False

        # dp翻译自状态转移
        for i in range(m):
            for j in range(n):
                if s[i] == p[j] or p[j] == '?':
                    f[i + 1][j + 1] = f[i][j]
                elif p[j] == '*':
                    f[i + 1][j + 1] = f[i][j + 1] or f[i + 1][j]

        # 返回值翻译自递归入口
        return f[m][n]
#3.一维数组递推
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        f = [False] * (n + 1)  # f[n + 1]

        # 初始条件：翻译自递归边界
        # 对应边界 i<0 and j < 0 return True
        f[0] = True
        # 对应边界 i<0 j>=0的处理
        for j in range(n):
            f[j + 1] = p[j] == '*' and f[j]

        # dp翻译自状态转移
        for i in range(m):
            pre = f[0]
            f[0] = False # 对应边界 j<0
            for j in range(n):
                tmp = f[j + 1]
                if s[i] == p[j] or p[j] == '?':
                    f[j + 1] = pre
                elif p[j] == '*':
                    f[j + 1] = f[j + 1] or f[j]
                else:
                    f[j + 1] = False
                    # 注意，由于每行都是复用f, 所以也需要更新f[j + 1]，否则会让上一行的错误结果保留到这一行
                    # 而二维数组不需要是因为每行都是独立的，初始化时已经是False了
                pre = tmp

        # 返回值翻译自递归入口
        return f[n]
#45. 跳跃游戏 II
# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置在下标 0。

# 每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在索引 i 处，你可以跳转到任意 (i + j) 处：

# 0 <= j <= nums[i] 且
# i + j < n
# 返回到达 n - 1 的最小跳跃次数。测试用例保证可以到达 n - 1。
class Solution:
    def jump(self,nums:List[int])->int:
        ans=0
        cur_right=0
        nxt_right=0
        for i in range(len(nums)-1):
            nxt_right=max(nxt_right,i+nums[i])  #每个端点可以到达的最长距离
            if i==cur_right:  #无路可走，必须建桥
                cur_right=nxt_right
                ans+=1
        return ans
#46. 全排列
#给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
class Solution:
    def permute(self,nums:List[int])->List[List[int]]:
        n=len(nums)
        ans=[]
        path=[0]*n
        on_path=[False]*n
        def dfs(i:int)->None:
            if i==n:
                ans.append(path.copy())
                return 
            for j,on in enumerate(on_path):
                if not on:
                    path[i]=num[j]
                    on_path[j]=True
                    dfs(i+1)
                    on_path[j]=False
        dfs(0)
        return ans
#47. 全排列 II
#给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的 全排列。
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(x):
            if x==len(nums)-1:
                res.append(list(nums))
                return 
            dic=set()
            for i in range(x,len(nums)):
                if nums[i] in dic :continue
                dic.add(nums[i])
                nums[i],nums[x]=nums[x],nums[i]#交换位置，使nums[i]的值固定在x位置上、
                dfs(x+1)
                nums[i],nums[x]=nums[x],nums[i]
            res=[]
            dfs(0)
            return res
#48. 旋转图像
# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """方法一：辅助矩阵,找规律
        n=len(matrix)
        #深拷贝
        tmp=copy.deepcopy(matrix)
        for i in range(n):
            for j in range(n):
                matrix[j][n-1-i]=tmp[i][j]"""
        """方法二：原地修改,需要暂存一些元素"""
        n=len(matrix)
        for i in range(n//2):
            for j in range((n+1)//2):
                tmp=matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = tmp
#49. 字母异位词分组
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
class Solution:
    def groupAngrams(self,strs:List[str])->List[List[str]]:
        d=defaultdict(list)
        for s in strs:
            sorted_s="".join(sorted(s))
            d[sorted_s].append(s)
        return list(d.values())
#50. Pow(x, n)
#实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，xn ）。
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0: return 0.0
        res = 1
        if n < 0: x, n = 1 / x, -n
        while n:
            if n & 1: res *= x  #这一步很重要，需要用它来判断做的有用没用
            x *= x
            n >>= 1
        return res
