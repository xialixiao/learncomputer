#101. 对称二叉树
#给你一个二叉树的根节点 root ， 检查它是否轴对称。
class Solution:
    def isSameTree(self,p:Optional[TreeNode],q:Optional[TreeNode])->bool:
        if p is None or q is None:
            return p is q
        return p.val==q.val and self.isSameTree(p.left,q.right) and self.isSameTree(p.right,q.left)
    def isSymmetric(self,root:Optional[TreeNode])->bool:
        return self.isSameTree(root.left,root.right)
#102. 二叉树的层序遍历
#给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
#方法一：两个数组
class Solution:
    def levelOrder(self,root:Optional[TreeNode])->List[List[int]]:
        if root is None:
            return []
        ans=[]
        cur=[root]
        while cur:
            nxt=[]
            vals=[]
            for node in cur:
                vals.append(node.val)
                if node.left:nxt.append(node.left)
                if node.right:nxt.append(node.right)
            cur=nxt
            ans.append(vals)
#一个队列
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans=[]
        q=deque([root])
        while q:
            vals=[]
            for _ in range(len(q)):
                node=q.popleft()
                vals.append(node.val)
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)
            ans.append(vals)
        return ans
#103. 二叉树的锯齿形层序遍历
#给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res=[]
        q=deque([root])
        while q:
            vals=deque()
            for _ in range(len(q)):
                node=q.popleft()
                if len(res)%2==0:
                    vals.append(node.val)
                else:
                    vals.appendleft(node.val)
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)
            res.append(list(vals))
        return res
#104. 二叉树的最大深度
# 给定一个二叉树 root ，返回其最大深度。
# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
#第一种：自底向上
class Solution:
    def maxDepth(self,root:Optional[TreeNode])->int:
        if root is None:
            return 0
        l_depth=self.maxDepth(root.left)
        r_depth=self.maxDepth(root.right)
        return max(l_depth,r_depth)+1
#第二种：自顶向下
class Solution:
    def maxDepth(self,root:Optional[TreeNode])->int:
        ans=0
        def dfs(node:Optional[TreeNode],depth:int)->int:
            if node is None:
                return
            depth+=1
            nonlocal ans
            ans=max(ans,depth)
            dfs(node.left,depth)
            dfs(node.right,depth)
        dfs(root,0)
#nonlocal关键字修饰变量后标识该变量是上一级函数中的局部变量，如果上一级函数中不存在该局部变量，nonlocal位置会发生错误（最上层的函数使用nonlocal修饰变量必定会报错）。
#105. 从前序与中序遍历序列构造二叉树
#给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bulidTress(self,preorder:List[int],inorder:List[int])->Optional[TreeNode]:
        if not preorder:
            return None
        left_size=inorder.index(preorder[0])
        left=self.bulidTress(prerorder[1:1+left_zize],inorder[:left_size])
        right=self.bulidTress(preorder[1+left_zize:],inorder[1+left_size:])
        return TreeNode(preorder[0],left,right)
#106. 从中序与后序遍历序列构造二叉树
#给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:  # 空节点
            return None
        left_size = inorder.index(postorder[-1])  # 左子树的大小
        left = self.buildTree(inorder[:left_size], postorder[:left_size])
        right = self.buildTree(inorder[left_size + 1:], postorder[left_size: -1])
        return TreeNode(postorder[-1], left, right)
#107. 二叉树的层序遍历 II
#给你二叉树的根节点 root ，返回其节点值 自底向上的层序遍历 。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
#第一个方法：两个数组
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        cur = [root]
        while cur:
            nxt = []
            vals = []
            for node in cur:
                vals.append(node.val)
                if node.left:  nxt.append(node.left)
                if node.right: nxt.append(node.right)
            cur = nxt
            ans.append(vals)
        return ans[::-1]
#第二个方法：一个队列
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        q = deque([root])
        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left:  q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(vals)
        return ans[::-1]
#108. 将有序数组转换为二叉搜索树
#给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self,nums:List[int])->Optional[TreeNode]:
        if not nums:
            return None
        m=len(nums)//2
        left=self.sortedArrayToBST(nums[:m])
        right=self.sortedArrayToBST(nums[m+1:])
        return TreeNode(nums[m],left,right)
#109. 有序链表转换二叉搜索树
#给定一个单链表的头节点  head ，其中的元素 按升序排序 ，将其转换为 平衡 二叉搜索树。
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return head
        pre,slow,fast=None,head,head
        while fast and fast.next:
            fast=fast.next.next
            pre=slow
            slow=slow.next
        if pre:
            pre.next=None
        node=TreeNode(slow.val)
        if slow==fast:
            return node
        node.left=self.sortedListToBST(head)
        node.right=self.sortedListToBST(slow.next)
        return node
#110. 平衡二叉树
#给定一个二叉树，判断它是否是 平衡二叉树  
class Solution:
    def isBalanced(self,root:Optional[TreeNode])->bool:
        if not root:return True
        return abs(self.depth(root.left)-self.depth(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    def depth(self,root):
        if not root:return 0
        return max(self.depth(root.left),self.depth(root.right))+1