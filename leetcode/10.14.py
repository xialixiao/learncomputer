#141. 环形链表
# 给你一个链表的头节点 head ，判断链表中是否有环。
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
# 如果链表中存在环 ，则返回 true 。 否则，返回 false 。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #快慢指针，再有环的情况下，这俩指针终会相遇，没有环，fast走到头就结束了
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast is slow:
                return True
        return False  #访问到了链表末尾，没有环
#142. 环形链表 II
# 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
# 不允许修改 链表。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast is slow:
                while slow is not head: #再走a步,到达入环扣，此时正确位置，因为利用快慢指针，相遇的地方不是入环扣。
                    slow=slow.next
                    head=head.next
                return slow
        return None
#143. 重排链表                  
# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：
# L0 → L1 → … → Ln - 1 → Ln
# 请将其重新排列后变为：
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 快慢指针找到链表中点
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # cur 指向右半部分链表
        cur = slow.next
        slow.next = None
        
        # 反转右半部分链表
        pre = None
        while cur:
            t = cur.next
            cur.next = pre
            pre, cur = cur, t
        cur = head

        # 此时 cur, pre 分别指向链表左右两半的第一个节点
        # 合并
        while pre:
            t = pre.next
            pre.next = cur.next
            cur.next = pre
            cur, pre = pre.next, t
#144. 二叉树的前序遍历
#给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #2.迭代
        ans=[]
        st=[]
        cur=root
        while cur or st:
            while cur:
                ans.append(cur.val)
                st.append(cur)
                cur=cur.left
            cur=st.pop()
            cur=cur.right
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #1.递归
        ans=[]
        def dfs(root):
            if root is None:
                return
            ans.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ans
#145. 二叉树的后序遍历     
#给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #1.递归
        ans=[]
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            dfs(root.right)
            ans.append(root.val)
        dfs(root)
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 注意：根节点为空，直接返回空列表
        if not root:
            return []
        stack = []
        res = []
        while root or stack:
            while root:
                # 当前节点入栈
                stack.append(root)
                # 如果当前节点有左子树，继续向左子树找
                if root.left:
                    root = root.left
                # 如果当前节点无左子树，在右子树继续找
                else:
                    root = root.right
            # 跳出循环的条件是 root 为空，那当前栈顶元素为叶子节点。
            # 弹出栈顶元素，并加入结果数组
            cur = stack.pop()
            res.append(cur.val)
            # 如果栈不为空，且当前栈顶元素的左节点是刚刚跳出的栈顶元素 cur
            # 则转向遍历右子树当前栈顶元素的右子树
            if stack and stack[-1].left == cur:
                root = stack[-1].right
            # 否则证明当前栈顶元素无左右子树，那当前的栈顶元素弹出。
            else:
                root = None
        return res
#146. LRU 缓存
# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 实现 LRUCache 类：
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
class Node:
    # 提高访问属性的速度，并节省内存
    __slots__ = 'prev', 'next', 'key', 'value'

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()  # 哨兵节点
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.key_to_node = {}

    # 获取 key 对应的节点，同时把该节点移到链表头部
    def get_node(self, key: int) -> Optional[Node]:
        if key not in self.key_to_node:  # 没有这本书
            return None
        node = self.key_to_node[key]  # 有这本书
        self.remove(node)  # 把这本书抽出来
        self.push_front(node)  # 放在最上面
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)  # get_node 会把对应节点移到链表头部
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)  # get_node 会把对应节点移到链表头部
        if node:  # 有这本书
            node.value = value  # 更新 value
            return
        self.key_to_node[key] = node = Node(key, value)  # 新书
        self.push_front(node)  # 放在最上面
        if len(self.key_to_node) > self.capacity:  # 书太多了
            back_node = self.dummy.prev
            del self.key_to_node[back_node.key]
            self.remove(back_node)  # 去掉最后一本书

    # 删除一个节点（抽出一本书）
    def remove(self, x: Node) -> None:
        x.prev.next = x.next
        x.next.prev = x.prev

    # 在链表头添加一个节点（把一本书放在最上面）
    def push_front(self, x: Node) -> None:
        x.prev = self.dummy
        x.next = self.dummy.next
        x.prev.next = x
        x.next.prev = x


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
#147. 对链表进行插入排序
# 给定单个链表的头 head ，使用 插入排序 对链表进行排序，并返回 排序后链表的头 。
# 插入排序 算法的步骤:
# 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
# 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
# 重复直到所有输入数据插入完为止。
# 下面是插入排序算法的一个图形示例。部分排序的列表(黑色)最初只包含列表中的第一个元素。每次迭代时，从输入数据中删除一个元素(红色)，并就地插入已排序的列表中。
# 对链表进行插入排序。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #1.转为列表
        if not head:
            return None
        node=head
        res=[]
        while node:
            res.append(node.val)
            node=node.next
        res.sort()
        node=head
        for i in range(len(res)):
            node.val=res[i]
            node=node.next
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #2.借助虚拟节点
        dummy=ListNode(0)
        pre=dummy

        cur=head
        while cur:
            #把下一个节点保存下来
            tmp=cur.next
            while pre.next and pre.next.val<cur.val:
                pre=pre.next
            cur.next=pre.next
            pre.next=cur
            pre=dummy
            cur=tmp
        return dummy.next
#148. 排序链表
#给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 876. 链表的中间结点（快慢指针）
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            pre = slow  # 记录 slow 的前一个节点
            slow = slow.next
            fast = fast.next.next
        pre.next = None  # 断开 slow 的前一个节点和 slow 的连接
        return slow

    # 21. 合并两个有序链表（双指针）
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 用哨兵节点简化代码逻辑
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1  # 把 list1 加到新链表中
                list1 = list1.next
            else:  # 注：相等的情况加哪个节点都是可以的
                cur.next = list2  # 把 list2 加到新链表中
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2  # 拼接剩余链表
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 如果链表为空或者只有一个节点，无需排序
        if head is None or head.next is None:
            return head
        # 找到中间节点 head2，并断开 head2 与其前一个节点的连接
        # 比如 head=[4,2,1,3]，那么 middleNode 调用结束后 head=[4,2] head2=[1,3]
        head2 = self.middleNode(head)
        # 分治
        head = self.sortList(head)
        head2 = self.sortList(head2)
        # 合并
        return self.mergeTwoLists(head, head2)
#149. 直线上最多的点数
#给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i, (x, y) in enumerate(points):  # 假设直线一定经过 points[i]
            cnt = defaultdict(int)
            for x2, y2 in points[i + 1:]:
                dx, dy = x2 - x, y2 - y
                k = dy / dx if dx else inf
                cnt[k] += 1
                ans = max(ans, cnt[k])  # 这里没有算上 (x,y) 这个点，最后再加一
        return ans + 1
#150. 逆波兰表达式求值
# 给你一个字符串数组 tokens ，表示一个根据 逆波兰表示法 表示的算术表达式。
# 请你计算该表达式。返回一个表示表达式值的整数。
# 注意：
# 有效的算符为 '+'、'-'、'*' 和 '/' 。
# 每个操作数（运算对象）都可以是一个整数或者另一个表达式。
# 两个整数之间的除法总是 向零截断 。
# 表达式中不含除零运算。
# 输入是一个根据逆波兰表示法表示的算术表达式。
# 答案及所有中间计算结果可以用 32 位 整数表示。
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if len(token) > 1 or token[0].isdigit():  # token 是数字
                st.append(int(token))
                continue

            x = st.pop()
            if token == '+':
                st[-1] += x
            elif token == '-':
                st[-1] -= x
            elif token == '*':
                st[-1] *= x
            else:
                # 题目要求除法向零取整，但 // 是向下取整
                st[-1] = trunc(st[-1] / x) 
        return st[0]
