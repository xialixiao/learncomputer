#一、两数之和
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target。
# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
# 你可以按任意顺序返回答案。
#第一种做法
class Solution:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        for i in rnage(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
#第二种做法
class Solution:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        for i,x in enumerate(nums):
            for j in range(i+1,len(nums)):
                if x+nums[j]==target:
                    return [i,j]
#第三种做法
class Solution:
    def twoSum(self,nums:List[int],tagret:int)->List[int]:
        idx={}
        for i,x in enumerate(nums):
            if tagret-x in idx:
                return [idx[tagret-x],i]
            idx[x]=i
#二、两数之和
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#第一种做法：
class Soution:
    def addTwoNumbers(self,l1:Optional[ListNode],l2:Optional[ListNode])
        if not l1:
            return l2
        if not l2:
            return l1
        l1.val+=l2.val
        if l1.val>=10:
            l1.next=self.addTwoNumbers(ListNode(l1.val//10),l1.next)
            l1.val%=10
        l1.next=self.addTwoNumbers(l1.next,l2.next)
        return l1
#第二种做法：
class Solution:
    def addTwoNumbers(self,l1:Optional[ListNode],l2:Optional[ListNode],carry=0)->Optional[ListNode]:
        if l1 is None and l2 is None and carry==0:
            return None
        s=carry
        if l1:
            s+=l1.val
            l1=l1.next
        if l2:
            s+=l2.val
            l2=l2.next
        return ListNode(s%10,self.addTwoNumbers(l1,l2,s//10))
#第三种做法：
class Solution:
    # l1 和 l2 为当前遍历的节点，carry 为进位
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        if l1 is None and l2 is None:  # 递归边界
            return ListNode(carry) if carry else None  # 如果进位了，就额外创建一个节点
        if l1 is None:  # 如果 l1 是空的，那么此时 l2 一定不是空节点
            l1, l2 = l2, l1  # 交换 l1 与 l2，保证 l1 非空，从而简化代码
        s = carry + l1.val + (l2.val if l2 else 0)  # 节点值和进位加在一起
        l1.val = s % 10  # 每个节点保存一个数位（直接修改原链表）
        l1.next = self.addTwoNumbers(l1.next, l2.next if l2 else None, s // 10)  # 进位
        return l1
#三、无重复字符的最长字串
#给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
#第一种做法：
class Solution:
    def lengthOfLongestSubstring(self,s:str)->int:
        cnt=defaultdict(int)
        ans=left=0
        for right,x in enumerate(s):
            cnt[x]+=1
            while cnt[x]>1"
                cnt[s[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans
#第二种做法：
class Solution:
    def lengthOfLongestSubstring(self,s:str)->int:
        ans=left=0
        window=set()
        for right,c in enumerate(s):
            while c in window:
                window.remove(s[left])
                left+=1
            window.add(c)
            ans=max(ans,right-left+1)
        return ans
#四、 寻找两个正序数组的中位数
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
# 算法的时间复杂度应该为 O(log (m+n)) 。
#第一种做法：
class Solution:
    def findMedianSortedArrays(self,nums1:List[int],nums2:List[int])->float:
        nums=sorted(nums1+nums2)
        n=len(nums)
        return (nums[n//2]+nums[(n-1)//2])/2
#第二种做法：
class Solution:
    def findMedianSortedArrays(self,a:List[int],b:List[int])->float:
        if len(a)>len(b):
            a,b=b,a
        m,n=len(a),len(b)
        a=[-inf]+a+[inf]
        b=[-inf]+b+[inf]
        i,j=0,(m+n+1)//2
        while a[i+1]<=b[j]:
            i+=1
            j-=1
        max1=max(a[i],b[j]) #第一组的最大值
        min2=max(a[i+1],b[j+1]) #第二组的最小值
        return max1 if (m+n)%2 else(max1+min2)/2
#五、最长回文子串
#给你一个字符串 s，找到 s 中最长的 回文 子串。
#第一种做法：
class Solution:
    def longestPalindrome(self,s:str)->str:
        n=len(s)
        ans_left=ans_right=0
        #奇数回文
        for i in range(n):
            l=r=i
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            if r-1-l>ans_right-ans_left:
                ans_left,ans_right=l+1,r
        #偶数回文
        for i in range(n-1):
            l,r=i,i+1
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            if r-1-l>ans_right-ans_left:
                ans_left,ans_right=l+1,r
        return s[ans_left:ans_right]
#第二种做法：
class Soultion:
    def longestPalindrome(self,s:str)->str:
        n=len(s)
        ans_left=ans_right=0
        for i in range(2*n-1):
            l,r=i//2,(i+1)//2
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            if r-1-l>ans_right-ans_left:
                ans_left,ans_right=l+1,r
        return s[ans_left:ans_right]
#六. Z 字形变换
# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
# 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
# 请你实现这个将字符串进行指定行数变换的函数：
# string convert(string s, int numRows);
#第一种做法：
class Solution:
    def convert(self,s:str,numRows:int)->str:
        if numRows==1:
            return s
        res=[""]*numRows
        flag=-1
        i=0
        for ch in s:
            res[i]+=cj
            if i==0 or i==numRows-1:
                flag=-flag
            i+=flag
        return "".join(res)
#七、整数反转
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
#第一种做法：
class Solution:
    def reverse(self,x:int)->int:
        if -10<x<10:
            return x
        str_x=str(x)
        if str_x[0]=="-":
            res="-"+str_x[:0:-1]
        else:
            res=str_x[::-1]
        return int(res) if -2**31<=int(res)<2**31 else 0
#第二种做法：
class Solution:
    def reverse(self,x:int)->int:
        res=0
        sign=1 if x>=0 else -1
        x=abs(x)
        while x:
            res=res*10+x%10
            x//=10
        return sign*res if -2**31<=sign*res<2**31 else 0
#第三种做法：
class Solution:
    def reverse(slef,x:int)->int:
        r=int(str(abs(x))[::-1])*(1 if x>=0 else -1)
        return r if -2**31<=r<2**31 else 0
#八、字符串转换整数 (atoi)
# 请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数。

# 函数 myAtoi(string s) 的算法如下：

# 空格：读入字符串并丢弃无用的前导空格（" "）
# 符号：检查下一个字符（假设还未到字符末尾）为 '-' 还是 '+'。如果两者都不存在，则假定结果为正。
# 转换：通过跳过前置零来读取该整数，直到遇到非数字字符或到达字符串的结尾。如果没有读取数字，则结果为0。
# 舍入：如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被舍入为 −231 ，大于 231 − 1 的整数应该被舍入为 231 − 1 。
# 返回整数作为最终结果。
#第一种方法：
class Solution:
    def myAtoi(self,s:str)->int:
        s=s.strip() #去除前导空格
        if not s:return 0
        res,i,sign=0,1,1
        int_max=2**31-1,int_min=-2**31,2**31//10
        if s[0]=="-":
            sign=-1
        elif s[0]!="+":
            i=0
        for c in s[i:]:
            if not '0'<c<='9':break
            if res>bndry or res==bndry and c>'7':
                return int_max if sign==1 else int_min
            res=res*10+ord(c)-ord('0')
        return sign*res
# 九、回文数
# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 例如，121 是回文，而 123 不是。
# 第一种做法：
class Solution:
    def isPalindrome(self,x:int)->bool:
        if x<0:return False
        return str(x)==str(x)[::-1]
# 第二种做法：
class Solution:
    def isPalindrome(self,x:int)->bool:
        if x<0 or x>0 and x%10==0:return False
        res=0
        while res<x//10:
            res=res*10+x%10
            x//=10
        return res==x or res==x//10  #这里考虑奇偶数的特性
#十、10. 正则表达式匹配
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s 的，而不是部分字符串。
#第一种做法
#1.动态规划二维
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        
        # 初始化
        dp[0][0] = True
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        # 状态更新
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':             # 【题目保证'*'号不会是第一个字符，所以此处有j>=2】
                    dp[i][j] = dp[i][j-2]       # '*'号复制前一个字符0次（即消去前一个字符）
                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        dp[i][j] |= dp[i-1][j]      # '*'号复制前一个字符1-k次
        
        return dp[m][n]
#第二种做法
#2.一维数组DP
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m, n = len(s), len(p)
        dp = [False] * (n+1)
        
        # 初始化
        dp[0] = True
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[j] = dp[j-2]

        # 状态更新
        for i in range(1, m+1):
            dp2 = [False] * (n+1)           # 滚动数组
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp2[j] = dp[j-1]
                elif p[j-1] == '*':
                    dp2[j] = dp2[j-2]       # '*'号复制前一个字符0次（即消去前一个字符）
                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        dp2[j] |= dp[j]     # '*'号复制前一个字符1-k次
            dp = dp2                        # 滚动数组
        
        return dp[n]
#第三种做法：
#此方法根据灵神的来从回溯出发，
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #保证每次出现字符*时，前面都匹配到有效的字符
        m,n=len(s),len(p)
        # dfs(i, j)表示s[0, i]和p[0, j]是否匹配
        # 即s[:i + 1]和p[:j + 1]是否匹配
        #这里的cache是python的一大好处
        @cache
        def dfs(i:int,j:int)->bool:
            #递归边界的操作
            if i<0:#s消耗完
                if j<0:#p也消耗完，表示匹配
                    return True
                if p[j]!='*':  #如果p[j]不是*，肯定不匹配
                    return False
                return dfs(i,j-2) # p[j]是'*', 让p干掉'*'和'*'前面一个字符消掉
            elif j<0:
                return False
            # case1: s[i] == p[j], 即当前字符匹配，消掉，然后判断子问题
            if s[i]==p[j] or p[j]=='.':
                return dfs(i-1,j-1)
            #case2:s[i] != p[j]时：
            #case2.1 p[j] == '*'
            elif p[j]=='*':  # p[j - 1]表示'*'前一个字符
            # 如果p[j] == '*' 且 s[i] 和 p[j - 1]匹配
                if s[i]==p[j-1] or p[j-1]=='.':
                     # 需要考虑三种情况
                    # p[j]的'*'让p[j - 1]消失 dfs(i, j - 2)
                    # p[j]的'*'让p[j - 1]重复1次, 正好就和s[i]匹配了, 直接下一个子问题dfs(i - 1, j - 2)
                    # p[j]的'*'让p[j - 1]重复>=2次, 消掉s[i], 继续子问题 dfs(i - 1, j)
                    return dfs(i,j-2) or dfs(i-1,j-2) or dfs(i-1,j)
                # 如果p[j] == '*' 且 s[i] 和 p[j - 1]不匹配
                else:
                    return dfs(i,j-2)
            # case2.2 p[j]不是'*', 肯定不匹配
            else:  
                return False
        return dfs(m-1,n-1)
        
