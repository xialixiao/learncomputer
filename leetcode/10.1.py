#十一、盛最多水的容器
# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

# 返回容器可以储存的最大水量。

# 说明：你不能倾斜容器。
#第一种做法：
class Solution:
    def maxArea(self,height:List[int])->int:
        cur,ans=0,0
        l,r=0,len(height)-1
        while l<r:
            cur=(r-l)*min(height[r],height[l])
            ans=max(cur,ans)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return ans
#四、 整数转罗马数字
# 七个不同的符号代表罗马数字，其值如下：

# 符号	值
# I	1
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1000
# 罗马数字是通过添加从最高到最低的小数位值的转换而形成的。将小数位值转换为罗马数字有以下规则：

# 1. 如果该值不是以 4 或 9 开头，请选择可以从输入中减去的最大值的符号，将该符号附加到结果，减去其值，然后将其余部分转换为罗马数字。
# 2. 如果该值以 4 或 9 开头，使用 减法形式，表示从以下符号中减去一个符号，例如 4 是 5 (V) 减 1 (I): IV ，9 是 10 (X) 减 1 (I)：IX。仅使用以下减法形式：4 (IV)，9 (IX)，40 (XL)，90 (XC)，400 (CD) 和 900 (CM)。
# 4. 只有 10 的次方（I, X, C, M）最多可以连续附加 3 次以代表 10 的倍数。你不能多次附加 5 (V)，50 (L) 或 500 (D)。如果需要将符号附加4次，请使用 减法形式。
# 给定一个整数，将其转换为罗马数字。
#第一种做法
#1.因为有最大值到3999，把所有的可能全部写出，
#时间复杂度：O(1)。空间复杂度：O(1)。
R = (
    ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"),  # 个位
    ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"),  # 十位
    ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"),  # 百位
    ("", "M", "MM", "MMM"),  # 千位
)

class Solution:
    def intToRoman(self, num: int) -> str:
        return R[3][num // 1000] + R[2][num // 100 % 10] + R[1][num // 10 % 10] + R[0][num % 10]
#第二种做法
#2.贪心做法
#时间复杂度：O(1)
#空间复杂度：O(1)
class Solution:
    def intToRoman(self, num: int) -> str:
        #使用哈希表，按照从大到小的顺序排列
        hashmap = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        res=''
        for key in hashmap:
            if num//key!=0:
                count=num//key
                res+=hashmap[key]*count #例如输入3000，count为4
                num%=key
        return res
#十三、罗马数字转整数
# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1 。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 给定一个罗马数字，将其转换成整数。
#时间复杂度：O(n)，其中 n 是 s 的长度。
#空间复杂度：O(1)。
class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        if 'IV' in s:
            num += 4
            s = s.replace('IV','')
        if 'IX' in s:
            num += 9
            s = s.replace('IX','')
        if 'XL' in s:
            num += 40
            s = s.replace('XL','')
        if 'XC' in s:
            num += 90
            s = s.replace('XC','')
        if 'CD' in s:
            num += 400
            s = s.replace('CD','')
        if 'CM' in s:
            num += 900
            s = s.replace('CM','')
        for i in s:
            if i =='I':
                num +=1
            if i=='V':
                num +=5
            if i=='X':
                num +=10
            if i =='L':
                num+=50
            if i=='C':
                num+=100
            if i =='D':
                num+=500
            if i=='M':
                num+=1000
        return num
#十四、最长公共前缀
# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 “”。
class Solution:
    def longestCommonPrefix(self,strs:List[str])->str:
        s0=strs[0]
        for j,c in enumerate(s0):
            for s in strs:
                if j==len(s) or s[j]!=c:
                    return s0[:j]
        return s0
# 十五、三数之和
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        n=len(nums)
        for i in range(n-2):
            x=nums[i]
            if i>0 and x==nums[i-1]:
                continue
            if x+nums[i+1]+nums[i+2]>0:
                break
            if x+nums[-2]+nums[-1]<0:
                continue
            j=i+1
            k=n-1
            while j < k:
                s = x + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:  # 三数之和为 0
                    ans.append([x, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:  # 跳过重复数字
                        j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:  # 跳过重复数字
                        k -= 1
        return ans
#十六. 最接近的三数之和
# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。

# 返回这三个数的和。

# 假定每组输入只存在恰好一个解。

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        min_diff = inf  #维护[s-target]的最小值
        for i in range(n - 2):
            x = nums[i]
            if i and x == nums[i - 1]:
                continue  #跳过重复的数据

            # 优化一
            s = x + nums[i + 1] + nums[i + 2] 
            if s > target:  # 后面无论怎么选，选出的三个数的和不会比 s 还小
                if s - target < min_diff:
                    ans = s  # 由于下一行直接 break，这里无需更新 min_diff
                break

            # 优化二
            s = x + nums[-2] + nums[-1]
            if s < target:  # x 加上后面任意两个数都不超过 s，所以下面的双指针就不需要跑了
                if target - s < min_diff:
                    min_diff = target - s
                    ans = s
                continue

            # 双指针
            j, k = i + 1, n - 1
            while j < k:
                s = x + nums[j] + nums[k]
                if s == target:
                    return s
                if s > target:
                    if s - target < min_diff:  # s 与 target 更近
                        min_diff = s - target
                        ans = s
                    k -= 1
                else:  # s < target
                    if target - s < min_diff:  # s 与 target 更近
                        min_diff = target - s
                        ans = s
                    j += 1
        return ans
#十七、电话号码的字母组合
#给定一个仅包含数字2-9的字符串，返回所有它能表示的字母组合。答案可以按任意顺序返回，给出数字到字母的映射如下（与电话案件相同）。注意1不对应任何字母
#回溯算法：利用用了DFS和剪枝的思想，回溯问题确定三个就行，确定边界，当前要干什么，下一个子问题要干什么，写对这些就行。
MAPPING = "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        ans = []
        path = [''] * n  # 注意 path 长度一开始就是 n，不是空列表
        def dfs(i: int) -> None:
        #确定边界
            if i == n:
                ans.append(''.join(path))
                return
            #处理当前问题
            for c in MAPPING[int(digits[i])]:
                path[i] = c  # 先从第一个要选的数组中选第一，在从第二个要选的数组中选第一个值，假如就两个数，既i等于n，就是够长了，输入ans，并进行回退，然后在进行第二要选第二个值，一次类推，来判断生成的数组。并且这里因为是覆盖了数据，所以不需要进行回退操作
                #下一个子问题
                dfs(i + 1)
        dfs(0)
        return ans
#十八. 四数之和
# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

# 0 <= a, b, c, d < n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 你可以按 任意顺序 返回答案 。
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans=[]
        for i in range(n - 3):
            x = nums[i]
            if i and x == nums[i - 1]:
                continue  #跳过重复的数据
            if x+nums[i+1]+nums[i+2]+nums[i+3]>target:
                break
            if x+nums[-1]+nums[-2]+nums[-3]<target:
                continue
            for j in range(i+1,n-2):
                y=nums[j]
                if j>i+1 and y==nums[j-1]:
                    continue
                if x+y+nums[j+1]+nums[j+2]>target:
                    break
                if x+y+nums[-2]+nums[-1]<target:
                    continue
                k=j+1
                l=n-1
                while k < l:
                    s=x+y+nums[k]+nums[l]
                    if s > target:
                        l-=1
                    elif s<target:
                        k+=1
                    else:
                        ans.append([x, y, nums[k], nums[l]])
                        k += 1
                        while k < l and nums[k] == nums[k - 1]:  # 跳过重复数字
                            k += 1
                        l -= 1
                        while l > k and nums[l] == nums[l + 1]:  # 跳过重复数字
                            l -= 1
        return ans
#19、删除链表的倒数第 N 个结点
#给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
#第一种做法
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #第一种：大神的方法:由于可能会删除链表头部，用哨兵节点简化代码，两个指针，right先走n步，随后left在跟上，这样就可以得出left指针下一个数据就要被删除。
        left=right=dummy=ListNode(next=head)#虚拟头结点位于链表的开始处，其next指针指向链表的第一个实际节点。
        for _ in range(n):
            right=right.next
        while right.next:
            left=left.next
            right=right.next
        left.next=left.next.next
        return dummy.next
#第二种做法
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #方法二：还是要借用虚拟头节点，思路差不多，这是从正向出发，先算出有多少节点，再用这些节点数减去倒数第几个，就可以得出正序是第几个
        dummy=ListNode(0)
        dummy.next=head
        cur,length=head,0
        while cur:
            length+=1
            cur=cur.next
        cur=dummy
        for _ in range(length-n):
            cur=cur.next
        cur.next=cur.next.next
        return dummy.next
#二十、 有效的括号
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。
#利用栈的知识，必须成双针对的存在，即对称存在
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:  # s 长度必须是偶数
            return False
        st = []
        for c in s:
            if c == '(':
                st.append(')')  # 入栈对应的右括号
            elif c == '[':
                st.append(']')
            elif c == '{':
                st.append('}')
            elif not st or st.pop() != c:  # c 是右括号
                return False  # 没有左括号，或者左括号类型不对
        return not st  # 所有左括号必须匹配完毕
        

