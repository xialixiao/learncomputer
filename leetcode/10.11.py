#111. 二叉树的最小深度
# 给定一个二叉树，找出其最小深度。
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 说明：叶子节点是指没有子节点的节点。
class Solution:
    def minDepth(self,root:Optional[TreeNode])->int:
        #1.从底层向上，递归
        if root is None:
            return 0
        if root.right is None:
            return self.minDepth(root.left)+1
        if root.left is None:
            return self.minDepth(root.right)+1
        return min(self.minDepth(root.left),self.minDepth(root.right))+1
class Solution:
    def minDepth(self,root:Optional[TreeNode])->int:
        #2,从顶向下
        ans=inf
        def dfs(node:Optional[TreeNode],cnt:int)->None:
            if node is None:
                return
            cnt+=1
            if node.left is None and node.right is None:
                nonlocal ans
                ans=min(ans,cnt)
                return 
            dfs(node.left,cnt)
            dfs(node.right,cnt)
        dfs(root,0)
        return ans if root else 0
#112. 路径总和
# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。
# 叶子节点 是指没有子节点的节点。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self,root:Optional[TreeNode],targetSum:int)->bool:
        if root is None:
            return False
        targetSum-=root.val
        if root.left is None and root.right is None:
            return targetSum==0
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)
#113. 路径总和 II   
# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
# 叶子节点 是指没有子节点的节点。
class Solution:
    def pathSum(self,root:Optional[TreeNode],targetSum:int)->List[List[int]]:
        #利用先序遍历
        res,path=[],[]
        def recur(root,tar):
            if not root:return
            path.append(root.val)
            tar-=root.val
            if tar==0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left,tar)
            recur(root.right,tar)
            path.pop()
        recur(root,targetSum)
        return res
#114. 二叉树展开为链表
# 给你二叉树的根结点 root ，请你将它展开为一个单链表：
# 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
# 展开后的单链表应该与二叉树 先序遍历 顺序相同。
class Solution:
    def flatten(self,root:Optional[TreeNode])->Optional[TreeNode]:
        if root is None:
            return None
        left_tail=self.flatten(root.left)
        right_tail=self.flatten(root.right)
        if left_tail:
            left_tail.right=root.right
            root.right=root.left
            root.left=None
        return right_tail or left_tail or root
#115. 不同的子序列
# 给你两个字符串 s 和 t ，统计并返回在 s 的 子序列 中 t 出现的个数。
# 测试用例保证结果在 32 位有符号整数范围内。
class Solution:
    def numDistinct(self,s:str,t:str)->int:
        @cache
        def dfs(i:int,j:int)->int:
            if i<j:
                return 0
            if j<0:
                return 1
            res=dfs(i-1,j)
            if s[i]==t[j]:
                res+dfs(i-1,j-1)
            return res
        return dfs(len(s)-1,len(t)-1)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if n < m:
            return 0

        f = [[1] + [0] * m for _ in range(n + 1)]
        for i, x in enumerate(s):
            for j in range(max(m - n + i, 0), min(i + 1, m)):
                f[i + 1][j + 1] = f[i][j + 1]
                if x == t[j]:
                    f[i + 1][j + 1] += f[i][j]
        return f[n][m]
#116. 填充每个节点的下一个右侧节点指针
# 给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
# 初始状态下，所有 next 指针都被设置为 NULL。
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #1.DFS
        pre=[]
        def dfs(node:'Node',depth:int)->None:
            if node is None:
                return
            if depth==len(pre):  #node是这一层的最左边的节点
                pre.append(node)
            else:  #pre[depth]是node左边的节点
                pre[depth].next=node #这里是是让next指向右边那个元素
                pre[depth]=node  #这里是更新数组
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        dfs(root,0) #根节点深度为0
        return root
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #2.BFS
        if root is None:
            return None
        q=[root]
        while q:
            #pairwise它表示的是一个迭代器（有点废话，itertools里面都是各种迭代器），他的含义是，从对象中获取连续的重叠对。
            for x,y in pairwise(q):
                x.next=y
            temp=q
            q=[]
            for node in temp:
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)
        return root
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #3.BFS+链表
        cur=root
        while cur:
            nxt=dummy=Node()
            while cur:
                if cur.left:
                    nxt.next=cur.left  # 下一层的相邻节点连起来
                    nxt=cur.left   
                if cur.right:
                    nxt.next=cur.right    # 下一层的相邻节点连起来
                    nxt=cur.right
                cur=cur.next  #当前层链表的下一个节点
            cur=dummy.next  #下一层链表的头节点
        return root
#117. 填充每个节点的下一个右侧节点指针 II
# 给定一个二叉树：
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL 。
# 初始状态下，所有 next 指针都被设置为 NULL 。

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = root
        while cur:
            nxt = dummy = Node()  # 下一层的链表
            while cur:  # 遍历当前层的链表
                if cur.left:
                    nxt.next = cur.left  # 下一层的相邻节点连起来
                    nxt = cur.left
                if cur.right:
                    nxt.next = cur.right  # 下一层的相邻节点连起来
                    nxt = cur.right
                cur = cur.next  # 当前层链表的下一个节点
            cur = dummy.next  # 下一层链表的头节点
        return root     
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        #2.BFS
        if root is None:
            return None
        q = [root]
        while q:
            # 从左到右依次连接
            for x, y in pairwise(q):
                x.next = y
            # 准备下一层的节点
            tmp = q
            q = []
            for node in tmp:
                if node.left:  q.append(node.left)
                if node.right: q.append(node.right)
        return root     


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        q = [root]
        while q:
            # 从左到右依次连接
            for x, y in pairwise(q):
                x.next = y
            # 准备下一层的节点
            tmp = q
            q = []
            for node in tmp:
                if node.left:  q.append(node.left)
                if node.right: q.append(node.right)
        return root
#118. 杨辉三角
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        c=[[1]*(i+1) for i in range(numRows)]
        for i in range(2,numRows):
            for j in range(1,i):
                c[i][j]=c[i-1][j-1]+c[i-1][j]
        return c
#119. 杨辉三角 II
MX = 34
c = [[1] * (i + 1) for i in range(MX)]
for i in range(2, MX):
    for j in range(1, i):
        # 左上方的数 + 正上方的数
        c[i][j] = c[i - 1][j - 1] + c[i - 1][j]

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return c[rowIndex]
#120. 三角形最小路径和
# 给定一个三角形 triangle ，找出自顶向下的最小路径和。
# 每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        @cache
        def dfs(i:int,j:int )->int:
            if i==n-1:
                return triangle[i][j]
            return min(dfs(i + 1, j), dfs(i + 1, j + 1)) + triangle[i][j]
        return dfs(0,0)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [[0] * (i + 1) for i in range(n)]
        f[-1] = triangle[-1]
        for i in range(n - 2, -1, -1):
            for j, x in enumerate(triangle[i]):
                f[i][j] = min(f[i + 1][j], f[i + 1][j + 1]) + x
        return f[0][0]
       


            
 

