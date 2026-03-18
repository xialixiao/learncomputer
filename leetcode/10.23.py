#231. 2 的幂
# 给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
# 如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。
class Solution:
    def isPowerOfTwo(self,n:int)->bool:
        a=0
        while 2**a<=n:
            if 2**a!=n:
                a+=1
            else:
                return True
        return False
class Solution:
    def isPowerOfTwo(self,n:int)->bool:
        return n>0 and n&(n-1)==0
#232. 用栈实现队列
# 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：
# 实现 MyQueue 类：
# void push(int x) 将元素 x 推到队列的末尾
# int pop() 从队列的开头移除并返回元素
# int peek() 返回队列开头的元素
# boolean empty() 如果队列为空，返回 true ；否则，返回 false
# 说明：
# 你 只能 使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
# 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
class MyQueue:
    def __init__(self):
        self.A,self.B=[],[]
    def push(self,x:int)->None:
        self.A.append(x)
    def pop(self)->int:
        peek=self.peek()
        self.B.pop()
        return peek
    def peek(self)->int:
        if self.B: return self.B[-1]
        if not self.A:return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B[-1]
    def empty(self)->bool:
        return not self.A and not self.B
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
#233. 数字 1 的个***
#给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
class Solution:
    def countDigitOne(self, n: int) -> int:
        s = list(map(int, str(n)))  # 避免在 dfs 中频繁调用 int()

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（一行代码实现记忆化）
        def dfs(i: int, cnt1: int, is_limit: bool) -> int:
            if i == len(s):
                return cnt1

            up = s[i] if is_limit else 9
            res = 0
            for d in range(up + 1):  # 枚举要填入的数字 d
                res += dfs(i + 1, cnt1 + (d == 1), is_limit and d == up)

            return res

        return dfs(0, 0, True)
#234. 回文链表
#给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 876. 链表的中间结点
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # 206. 反转链表
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.middleNode(head)
        head2 = self.reverseList(mid)
        while head2:
            if head.val != head2.val:  # 不是回文链表
                return False
            head = head.next
            head2 = head2.next
        return True
#235. 二叉搜索树的最近公共祖先
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# 例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
class Solution:
    def lowestCommonAncestor(self,root:TreeNode,p:TreeNode,q:TreeNode)->TreeNode:
        #进行对比，只要有一个相同的，就可以返回
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:  # 左右都找到
            return root  # 当前节点是最近公共祖先
        return left or right
#237. 删除链表中的节点
# 有一个单链表的 head，我们想删除它其中的一个节点 node。
# 给你一个需要删除的节点 node 。你将 无法访问 第一个节点  head。
# 链表的所有值都是 唯一的，并且保证给定的节点 node 不是链表中的最后一个节点。
# 删除给定的节点。注意，删除节点并不是指从内存中删除它。这里的意思是：
# 给定节点的值不应该存在于链表中。
# 链表中的节点数应该减少 1。
# node 前面的所有值顺序相同。
# node 后面的所有值顺序相同。
# 自定义测试：
# 对于输入，你应该提供整个链表 head 和要给出的节点 node。node 不应该是链表的最后一个节点，而应该是链表中的一个实际节点。
# 我们将构建链表，并将节点传递给你的函数。
# 输出将是调用你函数后的整个链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next
#238. 除自身以外数组的乘积 
# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
# 请 不要使用除法，且在 O(n) 时间复杂度内完成此题。
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #前缀和求解
        n=len(nums)
        pre=[1]*n
        #正向
        for i in range(1,n):
            pre[i]=pre[i-1]*nums[i-1]

        #逆向
        sur=[1]*n
        for i in range(n-2,-1,-1):
            sur[i]=sur[i+1]*nums[i+1]
        return [p*s for p,s in zip(pre,sur)]
#239. 滑动窗口最大值    
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
# 返回 滑动窗口中的最大值 。
#使用单调队列
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        q=deque() #双端队列
        for i,x in enumerate(nums):
            while q and nums[q[-1]]<=x:  #队列不为空，且队列的最后一个元素小于等于x
                q.pop() #维护q的单调性   队尾不要了
            q.append(i)  #入队
            if i-q[0]>=k: #出队
                q.popleft()  #队首已经离开窗口
            #记录答案，因为是从k-1才开始记录
            if i>=k-1:
                #由于队首到队尾单调递减，所以窗口最大值就是队首
                ans.append(nums[q[0]])
        return ans
#240. 搜索二维矩阵 II
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #第一种：从右边找对简单，并且给的数组是排序好的，简单了不少
        m,n=len(matrix),len(matrix[0])
        i,j=0,n-1  #从右上角开始
        while i<m and j>=0:  #还有剩余元素
            if matrix[i][j]==target:
                return True #找到target
            if matrix[i][j]<target:
                i+=1
            else:
                j-=1
        return False
        

        
