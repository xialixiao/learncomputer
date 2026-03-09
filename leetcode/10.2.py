#21. 合并两个有序链表
#将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#第一种做法
class Solution:
    def mergeTwoList(self,list1:Optional[ListNode],list2:Optional[ListNode])->Optional[ListNode]:
        cur=dum=ListNode(0)
        while list1 and list2:
            if list1.val <list2.val:
                cur.next,list1=list1,list1.next
            else:
                cur.next,list2=list2,list2.next
        cur.next=list1 if list1 else list2
        return dum.next
#第二种做法
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:return list2
        if not list2:return list1
        if list1.val<=list2.val:
            list1.next=self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next=self.mergeTwoLists(list1,list2.next)
            return list2
#22. 括号生成
#数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#第一种做法（选和不选）
class Solution:
    def generateParenthesis(self,n:int)->List[str]:
        ans=[]
        path=['']*(n*2) #所有括号的总长度
        def dfs(left:int ,right:int)->None:
            if right==n:
                ans.append(''.join(path))
                return 
            if left<n:
                path[left+right]='('  #直接覆盖，不用回退
                dfs(left+1,right)
            if right<left:
                path[left+right]=')'
                dfs(left,right+1)
        dfs(0,0)
        return ans
#第二种枚举哪一个的思路
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = []  # 记录左括号的下标
        # 目前填了 i 个括号
        # balance = 这 i 个括号中的左括号个数 - 右括号个数
        def dfs(i: int, balance: int) -> None:
            #边界条件
            if len(path) == n:
                s = [')'] * (n * 2)
                for j in path:
                    s[j] = '('
                ans.append(''.join(s))
                return
            # 枚举填 right=0,1,2,...,balance 个右括号
            for right in range(balance + 1):
                # 先填 right 个右括号，然后填 1 个左括号，记录左括号的下标 i+right
                path.append(i + right)
                dfs(i + right + 1, balance - right + 1)
                path.pop()  # 恢复现场

        dfs(0, 0)
        return ans
#23. 合并 K 个升序链表
# 给你一个链表数组，每个链表都已经按升序排列。
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
#第一种方法
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#分治思想，加递归
class Solution:
    # 21. 合并两个有序链表
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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        m = len(lists)
        if m == 0:
            return None
        if m == 1:
            return lists[0]  # 无需合并，直接返回
        left = self.mergeKLists(lists[:m // 2])  # 合并左半部分
        right = self.mergeKLists(lists[m // 2:])  # 合并右半部分
        return self.mergeTwoLists(left, right)  # 最后把左半和右半合并
#第二种做法
#借助最小堆的思想
ListNode.__lt__ = lambda a, b: a.val < b.val  # 让堆可以比较节点大小
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 哨兵节点，作为合并后链表头节点的前一个节点
        h = [head for head in lists if head]  # 把所有非空链表的头节点入堆
        heapify(h)  # 堆化
        while h:  # 循环直到堆为空·
            node = heappop(h)  # 剩余节点中的最小节点
            if node.next:  # 下一个节点不为空
                heappush(h, node.next)  # 下一个节点有可能是最小节点，入堆
            cur.next = node  # 把 node 添加到新链表的末尾
            cur = cur.next  # 准备合并下一个节点
        return dummy.next  # 哨兵节点的下一个节点就是新链表的头节点
#24. 两两交换链表中的节点
#给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
#第一种做法：
class Solution:
    def swapPairs(self,head:Optional[ListNode])->Optional[ListNode]:
        #迭代：采用哨兵
        node0=dummy=ListNode(next=head)
        node1=head
        while node 1 and node1.next:
            node2=node1.next
            node3=node2.next
            node0.next=node2
            node2.next=node1
            node1.next=node3
            node0=node1
            node1=node3
        return dummy.next
#第二种做法：
class Solution:
    def swapPairs(self,head:Optional[ListNode])->Optional[List]:
        dump=node1=head
        while node1 and node1.next:
            node2=node1.next
            node1.val,node2.val=node2.val,node2.val
            node1=node2.next
        return dump 
#第三种做法：
#3.递归的方式
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:  # 递归边界
            return head  # 不足两个节点，无需交换

        node1 = head
        node2 = head.next
        node3 = node2.next

        node1.next = self.swapPairs(node3)  # 1 指向递归返回的链表头
        node2.next = node1  # 2 指向 1

        return node2  # 返回交换后的链表头节点
#25. K 个一组翻转链表（困难）
# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换
class Solution:
    def reverseKGroup(self,head:Optional[ListNode],k:int)->Optional[ListNode]:
        #统计节点个数
        n=0
        cur=head
        while cur:
            n+=1
            cur=cur.next
        p0=dummy=ListNode(next=head)
        pre=None
        cur=head
        #k个一组的处理
        while n>=k:
            n-=k
            for _ in range(k):
                nxt=cur.next
                cur.next=pre
                pre=cur
                cur=next
            nxt=p0.next
            nxt.next=cur
            p0.next=pre
            p0=nxt
        return dummy.next
#26. 删除有序数组中的重复项
# 给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。
# 考虑 nums 的唯一元素的数量为 k。去重后，返回唯一元素的数量 k。
# nums 的前 k 个元素应包含 排序后 的唯一数字。下标 k - 1 之后的剩余元素可以忽略。
# 判题标准:
# 系统会用下面的代码来测试你的题解:
# int[] nums = [...]; // 输入数组
# int[] expectedNums = [...]; // 长度正确的期望答案
# int k = removeDuplicates(nums); // 调用
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
#第一种做法
class Solution:
    def removeDuplicates(self,nums:Lisrt[int])->int:
        k=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k
#第二种做法：
class Solution:
    def removeDuplicates(self,nums:Lisrt[int])->int:
        nums[:]=sorted(set(nums))
        return len(nums) 
#27. 移除元素
# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。
# 假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：
# 更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
# 返回 k。
# 用户评测：
# 评测机将使用以下代码测试您的解决方案：
# int[] nums = [...]; // 输入数组
# int val = ...; // 要移除的值
# int[] expectedNums = [...]; // 长度正确的预期答案。
#                             // 它以不等于 val 的值排序。
# int k = removeElement(nums, val); // 调用你的实现
# assert k == expectedNums.length;
# sort(nums, 0, k); // 排序 nums 的前 k 个元素
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }
#第一种做法
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in nums:
            if i!=val:
                nums[k]=i
                k+=1
        return k
#28. 找出字符串中第一个匹配项的下标
# 给你两个字符串 haystack  和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回 -1 。
class Solution:
    def strStr(self,haystack:str,needle:str)->int:
        hy=len(haystack)
        ne=len(needle)
        for i in range(hy):
            if haystack[i:i+ne]==needle:
                return i
        return -1
#29. 两数相除
# 给你两个整数，被除数 dividend 和除数 divisor。将两数相除，要求 不使用 乘法、除法和取余运算。
# 整数除法应该向零截断，也就是截去（truncate）其小数部分。例如，8.345 将被截断为 8 ，-2.7335 将被截断至 -2 。
# 返回被除数 dividend 除以除数 divisor 得到的 商 。
# 注意：假设我们的环境只能存储 32 位 有符号整数，其数值范围是 [−231,  231 − 1] 。本题中，如果商 严格大于 231 − 1 ，则返回 231 − 1 ；如果商 严格小于 -231 ，则返回 -231 。
class Solution:
    def divide(self,dividend:int,divisor:int)->int:
        if abs(dividend)<abs(divisor):return 0
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        a,b,res=abs(dividend),abs(divisor),0
        for i in range(31,-1,-1):
             2^i * b <= a 换句话说 a/b = 2^i + (a-2^i*b)/b
            if (b << i) <= a:
                res += 1 << i
                a -= b << i
        return res if (dividend > 0) == (divisor > 0) else -res
#30. 串联所有单词的子串(困难题)
# 给定一个字符串 s 和一个字符串数组 words。 words 中所有字符串 长度相同。

#  s 中的 串联子串 是指一个包含  words 中所有字符串以任意顺序排列连接起来的子串。

# 例如，如果 words = ["ab","cd","ef"]， 那么 "abcdef"， "abefcd"，"cdabef"， "cdefab"，"efabcd"， 和 "efcdab" 都是串联子串。 "acdbef" 不是串联子串，因为他不是任何 words 排列的连接。
# 返回所有串联子串在 s 中的开始索引。你可以以 任意顺序 返回答案。
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])  # 一个单词的长度
        window_len = word_len * len(words)  # 所有单词的总长度，即窗口大小

        # 目标：窗口中的单词出现次数必须与 target_cnt 完全一致
        target_cnt = Counter(words)

        ans = []
        # 枚举第一个窗口的左端点，做 word_len 次起点不同的滑动窗口
        for start in range(word_len):
            cnt = defaultdict(int)
            overload = 0  # 统计过多的单词个数（包括不在 words 中的单词）
            # 枚举窗口最后一个单词的右开端点
            for right in range(start + word_len, len(s) + 1, word_len):
                # 1. in_word 进入窗口
                in_word = s[right - word_len: right]
                # 下面 cnt[in_word] += 1 后，in_word 的出现次数过多
                if cnt[in_word] == target_cnt[in_word]:
                    overload += 1
                cnt[in_word] += 1

                left = right - window_len  # 窗口第一个单词的左端点
                if left < 0:  # 窗口大小不足 window_len
                    continue

                # 2. 更新答案
                # 如果没有超出 target_cnt 的单词，那么也不会有少于 target_cnt 的单词
                if overload == 0:
                    ans.append(left)

                # 3. 窗口最左边的单词 out_word 离开窗口，为下一轮循环做准备
                out_word = s[left: left + word_len]
                cnt[out_word] -= 1
                if cnt[out_word] == target_cnt[out_word]:
                    overload -= 1

        return ans

        
