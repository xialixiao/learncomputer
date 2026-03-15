#91. 解码方法
# 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
# "1" -> 'A'
# "2" -> 'B'
# ...
# "25" -> 'Y'
# "26" -> 'Z'
# 然而，在 解码 已编码的消息时，你意识到有许多不同的方式来解码，因为有些编码被包含在其它编码当中（"2" 和 "5" 与 "25"）。
# 例如，"11106" 可以映射为：
# "AAJF" ，将消息分组为 (1, 1, 10, 6)
# "KJF" ，将消息分组为 (11, 10, 6)
# 消息不能分组为  (1, 11, 06) ，因为 "06" 不是一个合法编码（只有 "6" 是合法的）。
# 注意，可能存在无法解码的字符串。
# 给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。如果没有合法的方式解码整个字符串，返回 0。
# 题目数据保证答案肯定是一个 32 位 的整数。
class Solution:
    def numDecoding(self,s:str)->int:
        @cahce
        def dfs(i:int)->int:
            if i<0:
                return 1
            ans=0
            num=int(s[i:i+1])
            if 1<=num<=9:
                ans+=dfs(i-1)
            num=int(s[max(i-1,0):i+1])
            if 10<=num<=26:
                ans+=dfs(i-2)
            return ans
        return dfs(len(s)-1)
#92. 反转链表 II
#给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        p0=dummy=ListNode(next=head)
        for _ in range(left-1):
            p0=p0.next
        pre=None
        cur=p0.next
        for _ in range(right-left+1):
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt
        p0.next.next=cur
        p0.next=pre
        return dummy.next    
#93. 复原 IP 地址
# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
# 给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能 重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。
class Solution:
    def restoreIpAddress(self,s:str)->List[str]:
        def is_valid(t:str)->bool:
            if len(t)>3 or len(t)>1 and t[0]=='0':
                return False
            return int(t)<=255
        n=len(s)
        ans=[]
        for i in range(1,n):
            if not is_valid(s[:i]):
                break
            for j in range(i+1,n):
                if not is_valid(s[i:j]):
                    break
                for k in range(j+1,n):
                    if not is_valid(s[j:k]):
                        break
                    if is_valid(s[k:]):
                        ans.append(f"{s[:i]}.{s[i:j]}.{s[j:k]}.{s[k:]}")
        return ans
#94. 二叉树的中序遍历
#给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
#非递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #如果根节点为空，直接返回空链表
        if not root:
            return []
        stack=[]
        res=[]
        while root or stack:
            # 一直向左子树走，每一次将当前节点保存到栈中
            if root:
                stack.append(root)
                root=root.left
            # 当前节点为空，证明走到了最左边，从栈中弹出节点加入结果数组
            # 开始对右子树重复上述过程。
            else:
                cur=stack.pop()
                res.append(cur.val)
                root=cur.right
        return res
#递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def dfs(node:TreeNode)->None:
            if not node:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
        dfs(root)
        return ans
#95. 不同的二叉搜索树 II    
#给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if(n==0):
            return []
        def build_Trees(left,right):
            all_trees=[]
            if(left>right):
                return [None]
            for i in range(left,right+1):
                left_trees=build_Trees(left,i-1)
                right_trees=build_Trees(i+1,right)
                for l in left_trees:
                    for r in right_trees:
                        cur_tree=TreeNode(i)
                        cur_tree.left=l
                        cur_tree.right=r
                        all_trees.append(cur_tree)
            return all_trees
        res=build_Trees(1,n)
        return res
#96. 不同的二叉搜索树
#给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。
class Solution:
    def numTrees(self, n: int) -> int:
        dp=[0 for _ in range(n+1)]
        dp[0]=1
        for i in range(1,n+1):
            for j in range(0,i):
                dp[i]+=dp[j]*dp[i-j-1]
        return dp[n]
#97. 交错字符串
# 给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。
# 两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# 交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
# 注意：a + b 意味着字符串 a 和 b 连接。
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（一行代码实现记忆化）
        def dfs(i: int, j: int) -> bool:
            if i < 0 and j < 0:
                return True
            return i >= 0 and s1[i] == s3[i + j + 1] and dfs(i - 1, j) or \
                   j >= 0 and s2[j] == s3[i + j + 1] and dfs(i, j - 1)

        return dfs(n - 1, m - 1)
#98. 验证二叉搜索树
# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

# 有效 二叉搜索树定义如下：

# 节点的左子树只包含 严格小于 当前节点的数。
# 节点的右子树只包含 严格大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    pre = -inf
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if not self.isValidBST(root.left):  # 左
            return False
        if root.val <= self.pre:  # 中
            return False
        self.pre = root.val
        return self.isValidBST(root.right)  # 右
#99. 恢复二叉搜索树
#给你二叉搜索树的根节点 root ，该树中的 恰好 两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树 。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.firstNode = None
        self.secondNode = None
        self.preNode = TreeNode(float("-inf"))

        def in_order(root):
            if not root:
                return
            in_order(root.left)
            if self.firstNode == None and self.preNode.val >= root.val:
                self.firstNode = self.preNode
            if self.firstNode and self.preNode.val >= root.val:
                self.secondNode = root
            self.preNode = root
            in_order(root.right)

        in_order(root)
        self.firstNode.val, self.secondNode.val = self.secondNode.val, self.firstNode.val
#100. 相同的树
# 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p is q
        return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
