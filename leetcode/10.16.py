#162. 寻找峰值
# 峰值元素是指其值严格大于左右相邻值的元素。
# 给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
# 你可以假设 nums[-1] = nums[n] = -∞ 。
# 你必须实现时间复杂度为 O(log n) 的算法来解决此问题。
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #1.使用二分
        left,right=-1,len(nums)-1
        while left+1<right:
            mid=(left+right)//2
            if nums[mid]>nums[mid+1]: #下坡，峰顶位置在mid左边
                right=mid
            else:
                left=mid
        return right      
#164. 最大间距
# 给定一个无序的数组 nums，返回 数组在排序之后，相邻元素之间最大的差值 。如果数组元素个数小于 2，则返回 0 。
# 您必须编写一个在「线性时间」内运行并使用「线性额外空间」的算法。
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        #1.不是用桶排序
        if not nums or len(nums)<=1:
            return 0
        nums.sort(reverse = True)
        return max(nums[i] - nums[i+1]   for i in range(len(nums)-1))
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        #2.桶排序
        m = min(nums)
        M = max(nums)
        if M - m <= 1:
            return M - m

        n = len(nums)
        ans = d = (M - m + n - 2) // (n - 1)  # 答案至少是 d
        buckets = [[inf, -inf] for _ in range((M - m) // d + 1)]
        for x in nums:
            b = buckets[(x - m) // d]
            b[0] = min(b[0], x)  # 维护桶内元素的最小值和最大值
            b[1] = max(b[1], x)

        pre_max = inf
        for mn, mx in buckets:
            if mn != inf:  # 非空桶
                # 桶内最小值，减去上一个非空桶的最大值
                ans = max(ans, mn - pre_max)
                pre_max = mx
        return ans
#165. 比较版本号
# 给你两个 版本号字符串 version1 和 version2 ，请你比较它们。版本号由被点 '.' 分开的修订号组成。修订号的值 是它 转换为整数 并忽略前导零。
# 比较版本号时，请按 从左到右的顺序 依次比较它们的修订号。如果其中一个版本字符串的修订号较少，则将缺失的修订号视为 0。
# 返回规则如下：
# 如果 version1 < version2 返回 -1，
# 如果 version1 > version2 返回 1，
# 除此之外返回 0。
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        #2.双指针做法
        m, n = len(version1), len(version2)
        i = j = 0
        while i < m or j < n:
            a = b = 0
            while i < m and version1[i] != '.':
                a = a * 10 + int(version1[i])
                i += 1
            while j < n and version2[j] != '.':
                b = b * 10 + int(version2[j])
                j += 1
            if a != b:
                return -1 if a < b else 1
            i, j = i + 1, j + 1
        return 0
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        #1.库函数做法
        a=map(int,version1.split('.'))
        b=map(int,version2.split('.'))
        for ver1,ver2 in zip_longest(a,b,fillvalue=0):
            if ver1!=ver2:
                return -1 if ver1<ver2 else 1
        return 0
#166. 分数到小数      
# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。
# 如果小数部分为循环小数，则将循环的部分括在括号内。
# 如果存在多个答案，只需返回 任意一个 。
# 对于所有给定的输入，保证 答案字符串的长度小于 104 。
# 注意，如果分数可以表示为有限长度的字符串，则 必须 返回它。
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = '-' if numerator * denominator < 0 else ''
        numerator = abs(numerator)  # 保证下面的计算过程不产生负数
        denominator = abs(denominator)

        # 计算整数部分 q 和初始余数 r
        q, r = divmod(numerator, denominator)
        if r == 0:  # 没有小数部分
            return sign + str(q)

        ans = [sign + str(q) + '.']
        r_to_pos = {r: 1}  # 初始余数对应小数点后第一位
        while r:
            # 计算小数点后的数字 q，更新 r
            q, r = divmod(r * 10, denominator)
            ans.append(str(q))
            if r in r_to_pos:  # 有循环节
                pos = r_to_pos[r]  # 循环节的开始位置
                return f"{''.join(ans[:pos])}({''.join(ans[pos:])})"
            r_to_pos[r] = len(ans)  # 记录余数对应位置
        return ''.join(ans)  # 有限小数
#167. 两数之和 II - 输入有序数组
# 给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列  ，请你从数组中找出满足相加之和等于目标数 target 的两个数。如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。
# 以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。
# 你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。
# 你所设计的解决方案必须只使用常量级的额外空间。
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        left,right=0,n-1
        while left<right:
            count=numbers[left]+numbers[right]
            if count==target:
                return [left+1,right+1]
            elif count<target:
                left+=1
            else:
                right-=1
        return []
#168. Excel 表列名称    
# 给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。

# 例如：

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = []
        while n:
            n -= 1
            ans.append(chr(n % 26 + ord('A')))
            n //= 26
        return ''.join(ans[::-1])
#169. 多数元素
# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #第一种做法
        #nums.sort()
        #return nums[len(nums)//2]
        #第二种做法:mode通常用于统计数据集中出现频率最高的元素
        #return mode(nums)
        #第三种解法：哈希表
        #dict_1={}
        #for item in nums:
        #    if item not in dict_1:
        #        dict_1[item]=0
        #    else:
        #        dict_1[item]+=1
        #return max(dict_1,key=dict_1.get)  # 返回出现次数最多的元素
        #第三种解法：摩尔投票
        #推论一： 若记 众数 的票数为 +1 ，非众数 的票数为 −1 ，则一定有所有数字的 票数和 >0 。推论二： 若数组的前 a 个数字的 票数和 =0 ，则 数组剩余 (n−a) 个数字的 票数和一定仍 >0 ，即后 (n−a) 个数字的 众数仍为 x 。
        votes = 0  #初始化：票数统计votes=0,众数x
        for num in nums:
            if votes == 0: x = num#当票数 votes 等于 0 ，则假设当前数字 num 是众数。
            votes += 1 if num == x else -1#当 num = x 时，票数 votes 自增 1 ；当 num != x 时，票数 votes 自减 1 。
        return x



 

