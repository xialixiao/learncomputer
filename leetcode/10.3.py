#31. 下一个排列
# 整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。

# 例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
# 整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

# 例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
# 类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
# 而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
# 给你一个整数数组 nums ，找出 nums 的下一个排列。

# 必须 原地 修改，只允许使用额外常数空间。
#1.第一步先找出下一次需要调动到后面的数据；
#2.如果没有，直接跳过第二步，第二部确定需要调到前面的数据
#3.需要反转已经调转到前面数据的后半部分，这样才满足，因为这个题就是在一步一步寻找比上一个大一点的值，最大值就返回最小值。
#建议多写一点例子，找规律。
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        #第一步：从右向左找到第一个小于右边相邻数组的数nums[i+1]，此时得出nums[i]就是要交换的哪一位
        i=n-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        #如果找到了，进入第二步，否则跳过第二步，反转整个数组
        if i>=0:
            #第二步：从右向左找到nums[i]右边最小的大于nums[i]的数
            j=n-1 
            while nums[j]<=nums[i]:
                j-=1
            #交换nums[i]和nums[j]
            nums[i],nums[j]=nums[j],nums[i]
        #第三步：反转nums[i+1:] （如果上面跳过第二步，此时 i = -1）也就是数值是最大的时候需要反转整个数组
        # nums[i+1:] = nums[i+1:][::-1] 这样写也可以，但空间复杂度不是 O(1) 的
        left,right=i+1,n-1
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1     
#32. 最长有效括号（困难题）
# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号 子串 的长度。

# 左右括号匹配，即每个左括号都有对应的右括号将其闭合的字符串是格式正确的，比如 "(()())"。
#第一种
class Solution:
    def longestValidParentheses(self,s:str)->int:
        stk=[-1]#虚拟红线，一开始的栈底
        ans=0
        for i,ch in enumerate(s):
            if ch=="(":
                stk.append(i)
            elif len(stk)>1:
                stk.pop()
                ans=max(ans,i-stk[-1])
            else:
                stk[0]=i #替换栈底
        return ans
#第二种
#2.优化，不用栈，空间复杂度变为O（1）
class Solution:
    def solve(self, s: Iterable[str], left_ch: str) -> int:
        ans = left = right = 0
        for ch in s:
            if ch == left_ch:
                left += 1
            else:
                right += 1
            if left < right:  # 拆弹器太多了，ch 变成红线，重置计数器
                left = right = 0
            elif left == right:  # 完美拆弹
                ans = max(ans, right * 2)
        return ans

    def longestValidParentheses(self, s: str) -> int:
    #这里是为了防止左括号比右括号多的情况，所以倒叙也走一遍，这样就是包含了所有情况的代码
        return max(self.solve(s, '('), self.solve(reversed(s), ')'))  # reversed 是 O(1) 的
#第三种方法
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stack = []
        for i, c in enumerate(s):
            if stack and s[stack[-1]] == '(' and c == ')':
                stack.pop()
                if not stack: 
                    ans = max(ans, i+1)  #注意如果栈已经为空，表示都匹配成功，共i+1个括号
                else:
                    ans = max(ans, i-stack[-1])
            else:
                stack.append(i)
        return ans
#33. 搜索旋转排序数组
# 整数数组 nums 按升序排列，数组中的值 互不相同 。

# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 向左旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 下标 3 上向左旋转后可能变为 [4,5,6,7,0,1,2] 。

# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

# 你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
#第一种方法
#1.有点操蛋，不按照他的时间复杂度做，O（n）
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1  
#第二种做法
#2.两次二分
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=self.findMin(nums)
        if target>nums[-1]:#terget在第一段
           return self.lower_bound(nums,-1,i,target) #开区间（-1，i）
        #target在第二段
        return self.lower_bound(nums,i-1,len(nums),target)
    # 153. 寻找旋转排序数组中的最小值（返回的是下标）
    def findMin(self, nums: List[int]) -> int:
        left, right = -1, len(nums) - 1  # 开区间 (-1, n-1)
        while left + 1 < right:  # 开区间不为空
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid
            else:
                left = mid
        return right
    #有序数组中找到target的下标
    def lower_bound(self,nums:List[int],left:int,right:int,target:int)->int:
        while left+1<right:
            mid=(left+right)//2
            if nums[mid]>=target:
                right=mid
            else:
                left=mid
        return right if nums[right]==target else -1      
#第三种做法
#3.一次二分查找
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums) - 1  # 开区间 (-1, n-1)
        while left + 1 < right:  # 开区间不为空
            mid = (left + right) // 2
            x = nums[mid]
            if target > nums[-1] >= x:  # target 在第一段，x 在第二段
                right = mid  # 下轮循环去左边找
            elif x > nums[-1] >= target:  # x 在第一段，target 在第二段
                left = mid  # 下轮循环去右边找
            elif x >= target:  # 否则，x 和 target 在同一段，这就和方法一的 lower_bound 一样了
                right = mid
            else:
                left = mid
        return right if nums[right] == target else -1
#34. 在排序数组中查找元素的第一个和最后一个位置
# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

# 如果数组中不存在目标值 target，返回 [-1, -1]。

# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
#折半查找
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start=self.low_bound(nums,target)
        if start==len(nums) or nums[start]!=target:
            return [-1,-1]
        end=self.low_bound(nums,target+1)-1
        return [start,end]
    def low_bound(slef,nums:List[int],target:int)->int:
        left,right=0,len(nums)-1   #闭区间
        while left<=right:  #区间不为空
            mid=(left+right)//2
            if nums[mid]>=target:
                right=mid-1
            else:
                left=mid+1
        return left
#35. 搜索插入位置
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

# 请必须使用时间复杂度为 O(log n) 的算法。
#1.大神的代码，比较详细
# lower_bound 返回最小的满足 nums[i] >= target 的 i
# 如果数组为空，或者所有数都 < target，则返回 len(nums)
# 要求 nums 是非递减的，即 nums[i] <= nums[i + 1]

# 闭区间写法
def lower_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1  # 闭区间 [left, right]
    while left <= right:  # 区间不为空
        # 循环不变量：
        # nums[left-1] < target
        # nums[right+1] >= target
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # 范围缩小到 [mid+1, right]
        else:
            right = mid - 1  # 范围缩小到 [left, mid-1]
    return left

# 左闭右开区间写法
def lower_bound2(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)  # 左闭右开区间 [left, right)
    while left < right:  # 区间不为空
        # 循环不变量：
        # nums[left-1] < target
        # nums[right] >= target
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # 范围缩小到 [mid+1, right)
        else:
            right = mid  # 范围缩小到 [left, mid)
    return left  # 或者 right

# 开区间写法
def lower_bound3(nums: List[int], target: int) -> int:
    left, right = -1, len(nums)  # 开区间 (left, right)
    while left + 1 < right:  # 区间不为空
        mid = (left + right) // 2
        # 循环不变量：
        # nums[left] < target
        # nums[right] >= target
        if nums[mid] < target:
            left = mid  # 范围缩小到 (mid, right)
        else:
            right = mid  # 范围缩小到 (left, mid)
    return right

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return lower_bound(nums, target)  # 选择其中一种写法即可
        
#第二种
#2.库函数
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)
#36. 有效的数独
# 请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
 

# 注意：

# 一个有效的数独（部分已被填充）不一定是可解的。
# 只需要根据以上规则，验证已经填入的数字是否有效即可。
# 空白格用 '.' 表示。
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_has=[[False]*9 for _ in range(9)] #row_has[i][x] 表示i行是否有数字x
        col_has=[[False]*9 for _ in range(9)]#col_has[j][x]表示j列是否有数字x
        sub_box_has=[[[False]*9 for _ in range(3)] for _ in range (3)] # sub_box_has[i'][j'][x] 表示 (i',j') 宫是否有数字 x
        for i,row in enumerate(board):
            for j,b in enumerate(row):
                if b=='.':
                    continue
                x=int(b)-1 # 字符 '1'~'9' 转成数字 0~8
                if row_has[i][x] or col_has[j][x] or sub_box_has[i//3][j//3][x]:# 重复遇到数字 x
                    return False
                # 标记行、列、宫包含数字 x
                row_has[i][x] = col_has[j][x] = sub_box_has[i // 3][j // 3][x] = True
        return True 
#37. 解数独（困难题）
# 编写一个程序，通过填充空格来解决数独问题。

# 数独的解法需 遵循如下规则：

# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
# 数独部分空格内已填入了数字，空白格用 '.' 表示。
#注：纯大神做法，up也不会，太难了
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row_set = [set() for _ in range(9)]  # 每行填入的数字
        col_set = [set() for _ in range(9)]  # 每列填入的数字
        sub_box_set = [[set() for _ in range(3)] for _ in range(3)]  # 每宫填入的数字
        empty_pos = []  # 空格子的位置

        for i, row in enumerate(board):
            for j, b in enumerate(row):
                if b == '.':
                    empty_pos.append((i, j))  # 记录空格子的位置
                else:
                    x = int(b)
                    # 标记行、列、宫包含数字 x
                    row_set[i].add(x)
                    col_set[j].add(x)
                    sub_box_set[i // 3][j // 3].add(x)

        # get_candidates(i, j) 计算 (i, j) 这个空格子的待定数字个数，最小的在堆顶
        get_candidates = lambda i, j: 9 - len(row_set[i] | col_set[j] | sub_box_set[i // 3][j // 3])
        empty_heap = [(get_candidates(i, j), i, j) for i, j in empty_pos]
        heapify(empty_heap)

        # 每次递归，选一个空格子，枚举填入的数字
        def dfs() -> bool:
            if not empty_heap:  # 所有格子都已填入数字
                return True  # 完成数独

            # 数独玩法：优先考虑待定数字个数最少的空格子
            _, i, j = heappop(empty_heap)

            candidates = 0  # 受之前填入的数字影响，实际待定数字个数可能比入堆时的少，需要重新计算
            # 枚举 1~9 中没填过的数字 x，填入 board[i][j]
            for x in range(1, 10):
                if x in row_set[i] or x in col_set[j] or x in sub_box_set[i // 3][j // 3]:
                    continue  # x 填过了

                # 把数字 x 转成字符，填入 board[i][j]
                board[i][j] = digits[x]
                # 标记行、列、宫包含数字 x
                row_set[i].add(x)
                col_set[j].add(x)
                sub_box_set[i // 3][j // 3].add(x)

                # 填下一个空格子
                if dfs():
                    return True  # 完成数独

                # 恢复现场（撤销）
                # 注意 board[i][j] 无需恢复现场，因为我们会直接覆盖掉之前填入的数字
                row_set[i].remove(x)
                col_set[j].remove(x)
                sub_box_set[i // 3][j // 3].remove(x)

                # 统计待定数字个数
                candidates += 1

            # 恢复现场（撤销）
            heappush(empty_heap, (candidates, i, j))  # 重新入堆（更新待定数字个数）
            # 所有填法都不行，说明之前（祖先节点）的填法是错的
            return False

        dfs()
#38. 外观数列
# 「外观数列」是一个数位字符串序列，由递归公式定义：

# countAndSay(1) = "1"
# countAndSay(n) 是 countAndSay(n-1) 的行程长度编码。
 

# 行程长度编码（RLE）是一种字符串压缩方法，其工作原理是通过将连续相同字符（重复两次或更多次）替换为字符重复次数（运行长度）和字符的串联。例如，要压缩字符串 "3322251" ，我们将 "33" 用 "23" 替换，将 "222" 用 "32" 替换，将 "5" 用 "15" 替换并将 "1" 用 "11" 替换。因此压缩后字符串变为 "23321511"。

# 给定一个整数 n ，返回 外观数列 的第 n 个元素。
#第一种
#1.递归的思想
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s = self.countAndSay(n-1)
    
        i, res = 0, ''
        for j, c in enumerate(s):
            if c != s[i]:
                res += str(j-i) + s[i]
                i = j
        res += str(len(s) - i) + s[-1]  # 最后一个元素莫忘统计
        return res
#第二种做法
#2.迭代
def countAndSay(self, n: int) -> str:
    res = '1'
    for _ in range(n-1):  # 控制循环次数
        i, tmp = 0, ''
        for j, c in enumerate(res):
            if c != res[i]:
                tmp += str(j-i) + res[i]
                i = j
        res = tmp + str(len(res) - i) + res[-1]
    return res
#39. 组合总和
# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

# candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

# 对于给定的输入，保证和为 target 的不同组合数少于 150 个。
#方法一：选或不选
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i: int, left: int) -> None:
            if left == 0:
                # 找到一个合法组合
                ans.append(path.copy())
                return

            if i == len(candidates) or left < 0:
                return

            # 不选
            dfs(i + 1, left)

            # 选
            path.append(candidates[i])
            dfs(i, left - candidates[i])
            path.pop()  # 恢复现场

        dfs(0, target)
        return ans
#剪枝优化
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []

        def dfs(i: int, left: int) -> None:
            if left == 0:
                # 找到一个合法组合
                ans.append(path.copy())
                return

            if i == len(candidates) or left < candidates[i]:
                return

            # 不选
            dfs(i + 1, left)

            # 选
            path.append(candidates[i])
            dfs(i, left - candidates[i])
            path.pop()  # 恢复现场

        dfs(0, target)
        return ans
#方法二：枚举选哪个
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []

        def dfs(i: int, left: int) -> None:
            if left == 0:
                # 找到一个合法组合
                ans.append(path.copy())
                return

            # 枚举选哪个
            for j in range(i, len(candidates)):
                if candidates[j] > left:  # 排序了，后面的数都太大
                    break
                path.append(candidates[j])
                dfs(j, left - candidates[j])
                path.pop()  # 恢复现场

        dfs(0, target)
        return ans
#方法三：完全背包预处理 + 可行性剪枝
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        # 完全背包
        f = [[False] * (target + 1) for _ in range(n + 1)]
        f[0][0] = True
        for i, x in enumerate(candidates):
            for j in range(target + 1):
                f[i + 1][j] = f[i][j] or j >= x and f[i + 1][j - x]

        ans = []
        path = []

        def dfs(i: int, left: int) -> None:
            if left == 0:
                # 找到一个合法组合
                ans.append(path.copy())
                return

            # 无法用下标在 [0, i] 中的数字组合出 left
            if left < 0 or not f[i + 1][left]:
                return

            # 不选
            dfs(i - 1, left)

            # 选
            path.append(candidates[i])
            dfs(i, left - candidates[i])
            path.pop()

        # 倒着递归，这样参数符合 f 数组的定义
        dfs(n - 1, target)
        return ans
#40. 组合总和 II
# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

# candidates 中的每个数字在每个组合中只能使用 一次 。

# 注意：解集不能包含重复的组合。 
#选和不选
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []
        path = []

        def dfs(i: int, left: int) -> None:
            # 所选元素之和恰好等于 target
            if left == 0:
                ans.append(path.copy())  # 也可以写 path[:]
                return

            # 没有可以选的数字
            if i == n:
                return

            # 所选元素之和无法恰好等于 target
            x = candidates[i]
            if left < x:
                return

            # 选 x
            path.append(x)
            dfs(i + 1, left - x)
            path.pop()  # 恢复现场

            # 不选 x，那么后面所有等于 x 的数都不选
            # 如果不跳过这些数，会导致「选 x 不选 x'」和「不选 x 选 x'」这两种情况都会加到 ans 中，这就重复了
            i += 1
            while i < n and candidates[i] == x:
                i += 1
            dfs(i, left)

        dfs(0, target)
        return ans
#第二种
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []
        path = []

        def dfs(i: int, left: int) -> None:
            # 所选元素之和恰好等于 target
            if left == 0:
                ans.append(path.copy())  # 也可以写 path[:]
                return

            # 在 [i,n-1] 中选一个 candidates[j]
            # 注意选 candidates[j] 意味着 [i,j-1] 中的数都没有选
            for j in range(i, n):
                # 后面的数不需要选了，元素之和必然无法恰好等于 target
                if left < candidates[j]:
                    break
                # 考虑选 candidates[j]
                # 如果 j>i，说明 candidates[j-1] 没有选 
                # 同方法一，所有等于 candidates[j-1] 的数都不选
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                path.append(candidates[j])
                dfs(j + 1, left - candidates[j])
                path.pop()  # 恢复现场

        dfs(0, target)
        return ans

