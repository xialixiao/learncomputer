#61. 旋转链表
#给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置
class Solution:
    def rotateRight(self,head:Optional[ListNode],k:int)->Optional[ListNode]:
        if not head:
            return head
        #计算链表长度
        n=0
        cur=head
        while cur:
            n+=1
            cur=cur.next
        #对k取余
        k%=n
        fast,last=head,head
        for i in range(k):
            fast=fast.next
        while fast.next:
            fast=fast.next
            last=last.next
        fast.next=head
        last.next=None
        return fast
#62. 不同路径
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
# 问总共有多少条不同的路径？
#第一种做法记忆化搜索
class Solution:
    def uniquePaths(self,m:int,n:int)->int:
        @cached
        def dfs(i:int,j:int)->int:
            if i<0 and j<0:
                return 0
            if i==0 and j==0:
                return 1
            return dfs(i-1,j)+dfs(i,j-1)
        return dfs(m-1,n-1)
#第二种做法：1：1翻译成堆
class Solution:
    def uniquePaths(self,m:int,n:int)->int:
        f=[[0]*(n+1) for _ in range(m+1)]
        f[0][1]=1
        for i in range(m):
            for j in range(n):
                f[i+1][j+1]=f[i][j+1]+f[i+1][j]
        return f[m][n]
#3.空间优化
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [0] * (n + 1)
        f[1] = 1
        for _ in range(m):
            for j in range(n):
                f[j + 1] += f[j]
        return f[n]
#63. 不同路径 II
# 给定一个 m x n 的整数数组 grid。一个机器人初始位于 左上角（即 grid[0][0]）。机器人尝试移动到 右下角（即 grid[m - 1][n - 1]）。机器人每次只能向下或者向右移动一步。
# 网格中的障碍物和空位置分别用 1 和 0 来表示。机器人的移动路径中不能包含 任何 有障碍物的方格。
# 返回机器人能够到达右下角的不同路径数量。
# 测试用例保证答案小于等于 2 * 109。
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（一行代码实现记忆化）
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0 or obstacleGrid[i][j]:
                return 0
            if i == 0 and j == 0:
                return 1
            return dfs(i - 1, j) + dfs(i, j - 1)

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        return dfs(m - 1, n - 1)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        f = [[0] * (n + 1) for _ in range(m + 1)]
        f[0][1] = 1
        for i, row in enumerate(obstacleGrid):
            for j, x in enumerate(row):
                if x == 0:
                    f[i + 1][j + 1] = f[i][j + 1] + f[i + 1][j]
        return f[m][n]
#64. 最小路径和
# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 说明：每次只能向下或者向右移动一步。
class Solution:
    def minPathSum(self,grid:List[List[int]])->int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==j==0:continue
                elif i==0:grid[i][j]=grid[i][j-1]+grid[i][j]
                elif j==0:grid[i][j]=grid[i-1][j]+grid[i][j]
                else:grid[i][j]=min(grid[i-1][j],grid[i][j-1])+grid[i][j]
        return grid[-1][-1]
#65. 有效数字
# 给定一个字符串 s ，返回 s 是否是一个 有效数字。
# 例如，下面的都是有效数字："2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"，而接下来的不是："abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"。
# 一般的，一个 有效数字 可以用以下的规则之一定义：
# 一个 整数 后面跟着一个 可选指数。
# 一个 十进制数 后面跟着一个 可选指数。
# 一个 整数 定义为一个 可选符号 '-' 或 '+' 后面跟着 数字。
# 一个 十进制数 定义为一个 可选符号 '-' 或 '+' 后面跟着下述规则：
# 数字 后跟着一个 小数点 .。
# 数字 后跟着一个 小数点 . 再跟着 数位。
# 一个 小数点 . 后跟着 数位。
# 指数 定义为指数符号 'e' 或 'E'，后面跟着一个 整数。
# 数字 定义为一个或多个数位。
class Solution:
    def isNumber(self,s:str)->bool:
        n=len(s)
        i=0
        if s[i] in "+-":
            i+=1
        #指数符号之前，至多一个小数点，其余必须全是数字
        has_dot=has_digit=False
        while i<n and s[i] not in "eE":
            if s[i]==".":
                if has_dot: #不能有两个小数点
                    return False
                has_dot=True
            elif '0' <= s[i] <= '9':
                has_digit = True
            else:
                return False
            i += 1

        # 必须有数字
        if not has_digit:
            return False

        # 指数符号之后，必须是整数
        if i < n and s[i] in "eE":
            i += 1

            # 正负号
            if i < n and s[i] in "+-":
                i += 1

            # 必须有数字
            if i == n:
                return False

            # 剩下的必须全是数字
            while i < n and '0' <= s[i] <= '9':
                i += 1

        # 如果 i < n 说明有非法字符，不是有效数字
        return i == n
#66. 加一    
# 给定一个表示 大整数 的整数数组 digits，其中 digits[i] 是整数的第 i 位数字。这些数字按从左到右，从最高位到最低位排列。这个大整数不包含任何前导 0。
# 将大整数加 1，并返回结果的数字数组。
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=len(digits)
        for i in range(a-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0

        return [1]+[0]*len(digits)
#67. 二进制求和
# 给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。   
#第一个做法
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        while len(a) > len(b):
            b = "0" + b

        while len(a) < len(b):
            a = "0" + a

        tmp = 0
        a, b = list(a), list(b)
        for i in range(len(a) - 1, -1, -1):
            cur = int(a[i]) + int(b[i]) + tmp
            if cur == 3:
                b[i] = "1"
                tmp = 1
            elif cur == 2:
                b[i] = "0"
                tmp = 1
            elif cur == 1:
                b[i] = "1"
                tmp = 0
            else:
                b[i] = "0"
                tmp = 0
        if tmp == 1:
            b = ["1"] + b
        return "".join(b)
#第二种做法
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
#68. 文本左右对齐
# 给定一个单词数组 words 和一个长度 maxWidth ，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
# 你应该使用 “贪心算法” 来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
# 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
# 文本的最后一行应为左对齐，且单词之间不插入额外的空格。
# 注意:
# 单词是指由非空格字符组成的字符序列。
# 每个单词的长度大于 0，小于等于 maxWidth。
# 输入单词数组 words 至少包含一个单词。
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        n = len(words)
        i = 0
        while i < n:
            start = i  # 这一行第一个单词的下标
            sum_len = -1  # 第一个单词之前没有空格
            while i < n and sum_len + len(words[i]) + 1 <= maxWidth:
                sum_len += len(words[i]) + 1  # 单词之间至少要有一个空格
                i += 1

            extra_spaces = maxWidth - sum_len  # 这一行剩余未分配的空格个数
            gaps = i - start - 1  # 这一行单词之间的空隙个数（单词个数减一）

            # 特殊情况：如果只有一个单词，或者是最后一行，那么左对齐，末尾补空格
            if gaps == 0 or i == n:
                row = ' '.join(words[start: i]) + ' ' * extra_spaces  # 末尾补空格
                ans.append(row)
                continue

            # 一般情况：把 extra_spaces 个空格均匀分配到 gaps 个空隙中（靠左的空格更多）
            avg, rem = divmod(extra_spaces, gaps)
            spaces = ' ' * (avg + 1)  # +1 表示加上单词之间已有的一个空格
            # 前 rem 个空隙多一个空格
            row = (spaces + ' ').join(words[start: start + rem + 1]) + \
                  spaces + spaces.join(words[start + rem + 1: i])
            ans.append(row)
        return ans
#69. x 的平方根
# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
class Solution:
    def mySqrt(self, x: int) -> int:
        s = 0
        while s*s <= x:
            s +=1
            if s*s > x:
                return s-1
#70. 爬楼梯
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#从上往下，会超时
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache #缓存装饰器，避免重复计算dfs的结果
        def dfs(i: int) -> int:
            if i <= 1:  # 递归边界
                return 1
            return dfs(i - 1) + dfs(i - 2)
        return dfs(n)
        
