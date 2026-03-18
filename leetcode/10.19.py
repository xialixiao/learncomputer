#191. 位1的个数
#给定一个正整数 n，编写一个函数，获取一个正整数的二进制形式并返回其二进制表达式中 设置位 的个数（也被称为汉明重量）。
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
        #与操作，只要是1，就是1
            res += n & 1
            n >>= 1
        return res
#n &= n - 1 ： 消去数字 n 最右边的 1 。
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res
#198. 打家劫舍
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
#时间复杂度：O(n)，其中 n 是 nums 的长度。
#空间复杂度：O(n)。
class Solution:
    def rob(self, nums: List[int]) -> int:
        # dfs(i) 表示从 nums[0] 到 nums[i] 最多能偷多少
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int) -> int:
            if i < 0:  # 递归边界（没有房子）
                return 0
            return max(dfs(i - 1), dfs(i - 2) + nums[i])

        return dfs(len(nums) - 1)  # 从最后一个房子开始思考
# 直接翻译的话，dfs(i) 翻译成 f[i]。
# 但记忆化搜索会访问 dfs(−2) 和 dfs(−1)，f[−2] 和 f[−1] 下标越界了。
# 解决办法：在 f 数组的前面插入两个 0，把 f 数组整体往右偏移 2 位。偏移后，dfs(i) 翻译成 f[i+2]。
#1：1翻译成堆
#时间复杂度：O(n)。其中 n 是 nums 的长度。
#空间复杂度：O(n)。
class Solution:
    def rob(self, nums: List[int]) -> int:
        f = [0] * (len(nums) + 2)
        for i, x in enumerate(nums):
            f[i + 2] = max(f[i + 1], f[i] + x)
        return f[-1]
#空间优化
#时间复杂度：O(n)。其中 n 是 nums 的长度。
#空间复杂度：O(1)。
class Solution:
    def rob(self, nums: List[int]) -> int:
        f0 = f1 = 0
        for x in nums:
            f0, f1 = f1, max(f1, f0 + x)
        return f1
#199. 二叉树的右视图
#给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #递归，先递归右子树，再递归左子树，当某个深度首次到达时，对应的节点就在右视图中。
        ans=[]
        def dfs(node:Optional[TreeNode],depth:int)->None:
            if node is None:
                return
            if depth==len(ans): #这个深度首次遇到
                ans.append(node.val)
            dfs(node.right,depth+1) #先递归右子树，保证首次遇到的一定是最右边的节点
            dfs(node.left,depth+1)
        dfs(root,0)
        return ans
#200. 岛屿数量
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 此外，你可以假设该网格的四条边均被水包围。
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        def dfs(i:int,j:int)->None:
            #出界，或者不是1，就不再往下递归
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]!="1":
                return 
            grid[i][j]="2"
            dfs(i,j-1) #往左走
            dfs(i,j+1) #往右走
            dfs(i-1,j) #往上走
            dfs(i+1,j) #往下走
        ans=0
        for i,row in enumerate(grid):
            for j,c in enumerate(row):
                if c=="1":
                    dfs(i,j)
                    ans+=1
        return ans
