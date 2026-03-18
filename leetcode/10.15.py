# #151. 反转字符串中的单词
# 给你一个字符串 s ，请你反转字符串中 单词 的顺序。
# 单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
# 返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。
# 注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()                            # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1 # 搜索首个空格
            res.append(s[i + 1: j + 1])          # 添加单词
            while i >= 0 and s[i] == ' ': i -= 1 # 跳过单词间空格
            j = i                                # j 指向下个单词的尾字符
        return ' '.join(res)                     # 拼接并返回
#152. 乘积最大子数组
# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续 子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
# 测试用例的答案是一个 32-位 整数。
# 请注意，一个只包含一个元素的数组的乘积是这个元素的值。
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        f_max = [0] * n
        f_min = [0] * n
        f_max[0] = f_min[0] = nums[0]
        for i in range(1, n):
            x = nums[i]
            # 把 x 加到右端点为 i-1 的（乘积最大/最小）子数组后面，
            # 或者单独组成一个子数组，只有 x 一个元素
            f_max[i] = max(f_max[i - 1] * x, f_min[i - 1] * x, x)
            f_min[i] = min(f_max[i - 1] * x, f_min[i - 1] * x, x) 
        return max(f_max)
#153. 寻找旋转排序数组中的最小值        
# 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
# 若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
# 若旋转 7 次，则可以得到 [0,1,2,4,5,6,7
# 注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
# 给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
# 你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>nums[-1]:
                left=mid+1
            else:
                right=mid-1
        return nums[left]
#154. 寻找旋转排序数组中的最小值 II
# 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,4,4,5,6,7] 在变化后可能得到：
# 若旋转 4 次，则可以得到 [4,5,6,7,0,1,4]
# 若旋转 7 次，则可以得到 [0,1,4,4,5,6,7]
# 注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
# 给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
# 你必须尽可能减少整个过程的操作步骤。
class Solution:
    def findMin(self, nums: [int]) -> int:
        nums=sorted(nums)
        return nums[0]
class Solution:
    def findMin(self, nums: [int]) -> int:
        i, j = 0, len(nums) - 1
        #关于选择点这里，左边的都要大于右边的数据
        while i < j:
            m = (i + j) // 2
            if nums[m]>nums[j]:i=m+1
            elif nums[m]<nums[j]:j=m
            else: return min(nums[i:j])
        return nums[i]
#155. 最小栈
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
# 实现 MinStack 类:
# MinStack() 初始化堆栈对象。
# void push(int val) 将元素val推入堆栈。
# void pop() 删除堆栈顶部的元素。
# int top() 获取堆栈顶部的元素。
# int getMin() 获取堆栈中的最小元素。
class MinStack:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]
    def push(self,val:int)->None:
        self.stack.append(val)
        if not self.min_stack or val<=self.min_stack[-1]:
            self.min_stack.append(val)
    def pop(self)->None:
        if self.stack.pop()==self.min_stack[-1]:
            self.min_stack.pop()
    def top(self)->int:
        return self.stack[-1]
    def getMin(self)->int:
        return self.min_stack[-1]
#160. 相交链表      
# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
# 图示两个链表在节点 c1 开始相交：
# 题目数据 保证 整个链式结构中不存在环。
# 注意，函数返回结果后，链表必须 保持其原始结构 。
# 自定义评测：
# 评测系统 的输入如下（你设计的程序 不适用 此输入）：
# intersectVal - 相交的起始节点的值。如果不存在相交节点，这一值为 0
# listA - 第一个链表
# listB - 第二个链表
# skipA - 在 listA 中（从头节点开始）跳到交叉节点的节点数
# skipB - 在 listB 中（从头节点开始）跳到交叉节点的节点数
# 评测系统将根据这些输入创建链式数据结构，并将两个头节点 headA 和 headB 传递给你的程序。如果程序能够正确返回相交节点，那么你的解决方案将被 视作正确答案 。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #假设公共部分是z，上半段是x，下半段是y，在（x+z）+y=（y+z）+x，意思就说两者都开始走，走完以后再走对方的路，x走y，y走x，会相遇，如果没相遇则是有空节点。
        p,q=headA,headB
        while p is not q:
            if p:
                p=p.next
            else:
                p=headB
            if q:
                q=q.next
            else:
                q=headA
        return p
        

        

 




