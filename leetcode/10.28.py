#282. 给表达式添加运算符
# 给定一个仅包含数字 0-9 的字符串 num 和一个目标值整数 target ，在 num 的数字之间添加 二元 运算符（不是一元）+、- 或 * ，返回 所有 能够得到 target 的表达式。
# 注意，返回表达式中的操作数 不应该 包含前导零。
# 注意，一个数字可以包含多个数位。
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(num, target, pos, exp, prev, curr, ans):
            if pos == len(num):
                if curr == target:
                    ans.append(exp)
                return 
            for l in range(1, len(num)-pos+1):
                t = num[pos:pos+l]
                if t[0] == "0" and len(t) > 1: break
                n = int(t)
                if pos == 0:
                    dfs(num, target, l, t, n, n, ans)
                    continue 
                dfs(num, target, pos+l, exp+'+'+t, n, curr+n, ans)
                dfs(num, target, pos+l, exp+'-'+t, -n, curr-n, ans)
                dfs(num, target, pos+l, exp+'*'+t, prev*n, curr-prev + prev*n, ans) 
                
        ans = []
        dfs(num, target, 0, "", 0, 0, ans)
        return ans



#283. 移动零
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[k]=nums[j]
                k+=1
        if k!=len(nums):
            for i in range(k,len(nums)):
                nums[i]=0
        return nums

#284. 窥视迭代器
# 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
# 假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
# 你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.pk = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.pk is None:
            self.pk = self.iter.next()
        return self.pk

    def next(self):
        """
        :rtype: int
        """
        if self.pk is not None:
            val = self.pk
            self.pk = None
            return val
        return self.iter.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pk is not None or self.iter.hasNext()


#287. 寻找重复数
# 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
# 假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
# 你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow, fast = 0, 0
        while True:
            slow = nums[slow]           # 类比链表slow=slow.next
            fast = nums[nums[fast]]     # 类比链表fast=fast.next.next
            if fast == slow:    # 首次相遇点
                break
        
        fast = 0                # fast回到起点
        while slow != fast:     # 再次相遇点即为重复数字
            slow = nums[slow]
            fast = nums[fast]
        
        return fast
#289. 生命游戏
# 根据 百度百科 ， 生命游戏 ，简称为 生命 ，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。
# 给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态： 1 即为 活细胞 （live），或 0 即为 死细胞 （dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
# 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
# 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
# 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
# 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
# 下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是 同时 发生的。给你 m x n 网格面板 board 的当前状态，返回下一个状态。
# 给定当前 board 的状态，更新 board 到下一个状态。
# 注意 你不需要返回任何东西。
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)      # 行数
        n = len(board[0])   # 列数
        for i in range(m):
            for j in range(n):
                count = 0   # 统计每个格子周围八个位置的活细胞数，每个格子计数重置为0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        # 枚举周围八个位置，其中去掉本身（x = y = 0）和越界的情况
                        if (x == 0 and y == 0) or i + x < 0 or i + x >= m or j + y < 0 or j + y >= n: continue
                        # 如果周围格子是活细胞（1）或者是活细胞变死细胞（2）的，都算一个活细胞
                        if board[i + x][j + y] == 1 or board[i + x][j + y] == 2: count += 1
                if board[i][j] == 1 and (count < 2 or count > 3): board[i][j] = 2   # 格子本身是活细胞，周围满足变成死细胞的条件，标记为2
                if board[i][j] == 0 and count == 3: board[i][j] = 3         # 格子本身是死细胞，周围满足复活条件，标记为3
        
        for i in range(m):
            for j in range(n):
                # 死细胞为0，活细胞变成死细胞为2，都为偶数，模2为0，刚好是死细胞
                # 活细胞为1，死细胞变成活细胞为3，都为奇数，模2为1，刚好是活细胞
                board[i][j] %= 2

#290. 单词规律
# 给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。具体来说：
# pattern 中的每个字母都 恰好 映射到 s 中的一个唯一单词。
# s 中的每个唯一单词都 恰好 映射到 pattern 中的一个字母。
# 没有两个字母映射到同一个单词，也没有两个单词映射到同一个字母。
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_p=s.split(' ')
        return len(pattern)==len(s_p) and len(set(zip(pattern,s_p)))==len(set(s_p))==len(set(pattern))
