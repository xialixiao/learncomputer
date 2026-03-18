#221. 最大正方形
# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
class Solution:
    # 84. 柱状图中最大的矩形
    # 改成计算最大正方形的边长
    def largestSize(self, heights: List[int]) -> int:
        st = [-1]  # 在栈中只有一个数的时候，栈顶的「下面那个数」是 -1，对应 left[i] = -1 的情况
        ans = 0
        for right, h in enumerate(heights):
            while len(st) > 1 and heights[st[-1]] >= h:
                i = st.pop()  # 矩形的高（的下标）
                left = st[-1]  # 栈顶下面那个数就是 left
                ans = max(ans, min(heights[i], right - left - 1))
            st.append(right)
        return ans

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])
        heights = [0] * (n + 1)  # 末尾多一个 0，理由见我 84 题题解
        ans = 0
        for row in matrix:
            # 计算底边为 row 的柱子高度
            for j, c in enumerate(row):
                if c == '0':
                    heights[j] = 0  # 柱子高度为 0
                else:
                    heights[j] += 1  # 柱子高度加一
            ans = max(ans, self.largestSize(heights))
        return ans * ans  # 最后再计算面积
#222. 完全二叉树的节点个数
# 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
# 完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层（从第 0 层开始），则该层包含 1~ 2h 个节点。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 求二叉树的深度
    def height(self, root:TreeNode):
        height = 0
        while root:
            root = root.left
            height += 1

        return height

    def countNodes(self, root: TreeNode) -> int:
        # 空树，节点数为 0
        if root == None:
            return 0
        # 求左子树和右子树的深度
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        
        # 如果左子树的深度 = 右子树的深度，左子树为满二叉树
        # 节点数 = 左子树的深度 + 右子树的深度 + 根节点
        if leftHeight == rightHeight:
            return (2 ** leftHeight - 1) + self.countNodes(root.right) + 1
        # 如果左子树的深度 ＞ 右子树的深度，右子树为满二叉树
        # 节点数 = 左子树的深度 + 右子树的深度 + 根节点
        else:
            return (2 ** rightHeight - 1) + self.countNodes(root.left) + 1
#223. 矩形面积
# 给你 二维 平面上两个 由直线构成且边与坐标轴平行/垂直 的矩形，请你计算并返回两个矩形覆盖的总面积。
# 每个矩形由其 左下 顶点和 右上 顶点坐标表示：
# 第一个矩形由其左下顶点 (ax1, ay1) 和右上顶点 (ax2, ay2) 定义。
# 第二个矩形由其左下顶点 (bx1, by1) 和右上顶点 (bx2, by2) 定义。
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        # 调整两个矩形位置, 让第一个矩形靠最左边
        if A > E:
            return self.computeArea(E, F, G, H, A, B, C, D)
        # 没有重叠的情况
        if B >= H or D <= F or C <= E:
            return abs(A - C) * abs(B - D) + abs(E - G) * abs(F - H)
        # 重叠情况
        # 下边界
        down = max(A, E)
        # 上
        up = min(C, G)
        # 左
        left = max(B, F)
        # 右
        right = min(D, H)
        return abs(A - C) * abs(B - D) + abs(E - G) * abs(F - H) - abs(up - down) * abs(left - right)
#224. 基本计算器
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
# 注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。
class Solution(object):
    def calculate(self, s):
        res, num, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == "+" or c == "-":
                res += sign * num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res += sign * num
        return res
#225. 用队列实现栈
# 请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。
# 实现 MyStack 类：
# void push(int x) 将元素 x 压入栈顶。
# int pop() 移除并返回栈顶元素。
# int top() 返回栈顶元素。
# boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。
# 注意：
# 你只能使用队列的标准操作 —— 也就是 push to back、peek/pop from front、size 和 is empty 这些操作。
# 你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可
class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0
#226. 翻转二叉树
#给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """第一种：从底向上
        if root is None:
            return None
        left=self.invertTree(root.left) #反转左子树
        right=self.invertTree(root.right) #反转右子树
        root.left=right
        root.right=left
        return root"""
        #从上向下
        if root is None:
            return None
        root.left, root.right = root.right, root.left  # 交换左右儿子
        self.invertTree(root.left)  # 翻转左子树
        self.invertTree(root.right)  # 翻转右子树
        return root
#227. 基本计算器 II       
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
# 整数除法仅保留整数部分。
# 你可以假设给定的表达式总是有效的。所有中间结果将在 [-231, 231 - 1] 的范围内。
# 注意：不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。
class Solution:
    def calculate(self, s: str) -> int:
        # solve mul and div instantly
        # solve add and sub later
        # use a stack store all values for later calculation

        st=[]
        num=""
        prev="+" #keep tracking previous operator

        for i, ch in enumerate(s):
            if ch.isdigit():
                num+=ch
            if i==len(s)-1 or ch in "+-*/": #reach end or meet an operator
                # push value into the stack for later calculation
                if prev=="+":
                    st.append(int(num))
                if prev=="-":
                    st.append(-int(num))
                # calculate the value and push result back instantly
                if prev=="*":
                    st.append(st.pop()*int(num))
                if prev=="/":
                    st.append(int(st.pop()/int(num)))
                # restore the num, and update the previous operator
                num=""
                prev=ch
        
        return sum(st)
#228. 汇总区间
# 给定一个  无重复元素 的 有序 整数数组 nums 。
# 区间 [a,b] 是从 a 到 b（包含）的所有整数的集合。
# 返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个区间但不属于 nums 的数字 x 。
# 列表中的每个区间范围 [a,b] 应该按如下格式输出：
# "a->b" ，如果 a != b
# "a" ，如果 a == b
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans=[]
        i=0
        n=len(nums)
        while i<n:
            start=i
            while i<n-1 and nums[i]+1==nums[i+1]:
                i+=1
            if start==i:
                ans.append(str(nums[start]))
            else:
                ans.append(f"{nums[start]}->{nums[i]}")
            i+=1
        return ans
#229. 多数元素 II
#给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 摩根投票 每三个不一样的数抵消一次
        numA = numB = None
        cntA = cntB = 0
        for num in nums:
            if num == numA:
                cntA += 1
            elif num == numB:
                cntB += 1
            elif numA is None:
                numA = num
                cntA += 1
            elif numB is None:
                numB = num
                cntB += 1
            else:
                cntA -= 1
                cntB -= 1
                if not cntA:
                    numA = None
                if not cntB:
                    numB = None
        # 个数验证
        cntA = cntB = 0
        for num in nums:
            if num == numA:
                cntA += 1
            elif num == numB:
                cntB += 1
        s = len(nums)//3
        ans = []
        if cntA > s:
            ans.append(numA)
        if cntB > s:
            ans.append(numB)
        return ans
#230. 二叉搜索树中第 K 小的元素
#给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 小的元素（k 从 1 开始计数）。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            dfs(node.left)  # 左
            nonlocal k, ans
            k -= 1
            if k == 0:
                ans = node.val  # 根
                return
            dfs(node.right)  # 右
        dfs(root)
        return ans
        



