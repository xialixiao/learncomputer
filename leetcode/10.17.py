#171. Excel 表列序号
# 给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回 该列名称对应的列序号 。
# 例如：
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for c in columnTitle:
            ans = ans * 26 + ord(c) - ord('A') + 1
        return ans
#172. 阶乘后的零
# 给定一个整数 n ，返回 n! 结果中尾随零的数量。
# 提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n:
            # 循环 k 次后，n 变成了 floor(n/5^k)
            n //= 5
            ans += n
        return ans
#173. 二叉搜索树迭代器
# 实现一个二叉搜索树迭代器类BSTIterator ，表示一个按中序遍历二叉搜索树（BST）的迭代器：
# BSTIterator(TreeNode root) 初始化 BSTIterator 类的一个对象。BST 的根节点 root 会作为构造函数的一部分给出。指针应初始化为一个不存在于 BST 中的数字，且该数字小于 BST 中的任何元素。
# boolean hasNext() 如果向指针右侧遍历存在数字，则返回 true ；否则返回 false 。
# int next()将指针向右移动，然后返回指针处的数字。
# 注意，指针初始化为一个不存在于 BST 中的数字，所以对 next() 的首次调用将返回 BST 中的最小元素。
# 你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 的中序遍历中至少存在一个下一个数字。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.node=root #初始化当前的节点为根节点
        self.st=[]   #缓存遍历的节点的栈

    def next(self) -> int:
        while self.node:
            #中序遍历
            self.st.append(self.node)
            self.node=self.node.left
        self.node=self.st.pop()  #栈顶元素为当前要处理的节点
        val=self.node.val  #缓存节点值
        self.node=self.node.right
        return val
        

    def hasNext(self) -> bool:
        return self.node is not None or len(self.st)>0 # 只有当节点和栈同时为空，整个树遍历结束
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
#174. 地下城游戏
# 恶魔们抓住了公主并将她关在了地下城 dungeon 的 右下角 。地下城是由 m x n 个房间组成的二维网格。我们英勇的骑士最初被安置在 左上角 的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。
# 骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。
# 有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。
# 为了尽快解救公主，骑士决定每次只 向右 或 向下 移动一步。
# 返回确保骑士能够拯救到公主所需的最低初始健康点数。
# 注意：任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n=len(dungeon),len(dungeon[0])
        dp=[[inf]*(n+1) for i in range(m+1)]
        dp[-1][-2]=dp[-2][-1]=1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j]=max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)
        return dp[0][0]


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        @cache
        def dfs(i, j):
            if i>=m or j>=n:
                return inf  
            if i ==m-1 and j ==n-1:
                return max(1 - dungeon[m-1][n-1], 1)
            return max(min(dfs(i+1, j), dfs(i, j+1)) - dungeon[i][j], 1)
        return dfs(0,0)

#179. 最大数
# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def sort_rule(x,y):
            a,b=x+y,y+x
            if a<b:return 1
            elif a>b:return -1
            else: return 0
        #转化成字符的形式
        strs=[str(num) for num in nums]
        strs.sort(key=cmp_to_key(sort_rule))
        if strs[0]=="0":
            return "0"
        return ''.join(strs)
