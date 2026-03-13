#71. 简化路径
# 给你一个字符串 path ，表示指向某一文件或目录的 Unix 风格 绝对路径 （以 '/' 开头），请你将其转化为 更加简洁的规范路径。
# 在 Unix 风格的文件系统中规则如下：
# 一个点 '.' 表示当前目录本身。
# 此外，两个点 '..' 表示将目录切换到上一级（指向父目录）。
# 任意多个连续的斜杠（即，'//' 或 '///'）都被视为单个斜杠 '/'。
# 任何其他格式的点（例如，'...' 或 '....'）均被视为有效的文件/目录名称。
# 返回的 简化路径 必须遵循下述格式：
# 始终以斜杠 '/' 开头。
# 两个目录名之间必须只有一个斜杠 '/' 。
# 最后一个目录名（如果存在）不能 以 '/' 结尾。
# 此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 '.' 或 '..'）。
# 返回简化后得到的 规范路径 。
class Solution:
    def simplifyPath(self,path:str)->str:
        stk=[]
        for s in path.split('/'):
            if s=='' or s=='.':
                continue
            if s!='..':
                stk.append(s)
            elif stk:
                stk.pop()
        return '/'+'/'.join(stk)
#72. 编辑距离
# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
# 你可以对一个单词进行如下三种操作：
# 插入一个字符
# 删除一个字符
# 替换一个字符
#1.大神做法，记忆化搜索
class Solution:
    def minDistance(self,s:str,t:str)->int:
        n,m=len(s),len(t)
        @cache
        def dfs(i:int,j:int)->int:
            if i<0:
                return j+1
            if j<0:
                return i+1
            if s[i]==t[j]:
                return dfs(i-1,j-1)
            return min(dfs(i-1,j),dfs(i,j-1),dfs(i-1,j-1))+1
        return dfs(n-1,m-1)
#2.大神做法：1:1 翻译成递推
class Solution:
    def minDistance(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        f[0] = list(range(m + 1))
        for i, x in enumerate(s):
            f[i + 1][0] = i + 1
            for j, y in enumerate(t):
                f[i + 1][j + 1] = f[i][j] if x == y else \
                        min(f[i][j + 1], f[i + 1][j], f[i][j]) + 1
        return f[n][m]
3.大神做法：空间优化：两个数组（滚动数组）
class Solution:
    def minDistance(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        f = [list(range(m + 1)), [0] * (m + 1)]
        for i, x in enumerate(s):
            f[(i + 1) % 2][0] = i + 1
            for j, y in enumerate(t):
                f[(i + 1) % 2][j + 1] = f[i % 2][j] if x == y else \
                        min(f[i % 2][j + 1], f[(i + 1) % 2][j], f[i % 2][j]) + 1
        return f[n % 2][m]
#4.大神做法：空间优化：一个数组
class Solution:
    def minDistance(self, s: str, t: str) -> int:
        f = list(range(len(t) + 1))
        for x in s:
            pre = f[0]
            f[0] += 1  # f[0] = i + 1
            for j, y in enumerate(t):
                tmp = f[j + 1]
                f[j + 1] = pre if x == y else min(f[j + 1], f[j], pre) + 1
                pre = tmp
        return f[-1]
#73. 矩阵置零
#给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
#第一种做法
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        x=set()
        y=set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    x.add(i)
                    y.add(j)
        for i in range(n):
            for j in range(m):
                if i in x or j in y:matrix[i][j]=0
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #做法二：
        ans = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    # 记录一下行和列
                    ans.append([i,j])
        # 再遍历一遍更新val
        while ans:
            que = ans.pop(0)
            # 更新行
            for i in range(len(matrix[0])):
                matrix[que[0]][i] = 0
            # 更新列
            for i in range(len(matrix)):
                matrix[i][que[1]] = 0
#74. 搜索二维矩阵
# 给你一个满足下述两条属性的 m x n 整数矩阵：
# 每行中的整数从左到右按非严格递增顺序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #1.最普通的寻找
        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==target:
                    return True
        return False
#2.简化，从最右侧开始查找
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:  # 还有剩余元素
            if matrix[i][j] == target:
                return True  # 找到 target
            if matrix[i][j] < target:
                i += 1  # 这一行剩余元素全部小于 target，排除
            else:
                j -= 1  # 这一列剩余元素全部大于 target，排除
        return False    
#3.二分做法
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #二分查找
        m,n=len(matrix),len(matrix[0])
        left,right=-1,m*n
        while left+1<right:
            mid=(left+right)//2
            x=matrix[mid//n][mid%n]
            if x==target:
                return True
            if x<target:
                left=mid
            else:
                right=mid
        return False
#75. 颜色分类        
# 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
# 必须在不使用库内置的 sort 函数的情况下解决这个问题。
#1.就用sort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #做法二：三指针,（维护左指针，枚举右指针），这次是三指针，所以中间加一个
        n=len(nums)
        left=0
        right=n-1
        mid=0
        while mid<=right:
            if nums[mid]==0:
                nums[mid],nums[left]=nums[left],nums[mid]
                left+=1
                mid+=1
            elif nums[mid]==2:
                nums[mid],nums[right]=nums[right],nums[mid]
                right-=1
            else:
                mid+=1
#76. 最小覆盖子串
# 给定两个字符串 s 和 t，长度分别是 m 和 n，返回 s 中的 最短窗口 子串，使得该子串包含 t 中的每一个字符（包括重复字符）。如果没有这样的子串，返回空字符串 ""。
# 测试用例保证答案唯一。
#滑动窗口+哈希
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans_left,ans_right=-1,len(s)
        cnt_s=Counter()   #s字串字母出现的次数
        cnt_t=Counter(t)  #t中字母出现的次数
        left=0
        for right,c in enumerate(s):
            cnt_s[c]+=1
            while cnt_s>=cnt_t:#涵盖
                if  right-left<ans_right-ans_left:  #找到最小的涵盖聚类
                    ans_left,ans_right=left,right
                cnt_s[s[left]]-=1 #左端点字母移除字符串
                left+=1
        return "" if ans_left<0 else s[ans_left:ans_right+1]
#77. 组合
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
# 你可以按 任何顺序 返回答案。
#方法一、枚举下一个数选那个
class Solution:
    def combine(self,n:int,k:int)->List[List[int]]:
        ans=[]
        path=[]
        def dfs(i:int)->None:
            d=k-len(path) #还要选d个数
            if d==0:
                ans.append(path.copy())
                return
            #枚举的数不能太小，否则后面没有数可以选
            for j in range(i,d-1,-1):
                path.append(j)
                dfs(j-1)
                path.pop() #恢复现场
        dfs(n)
        return ans
#方法二：选或不选
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i: int) -> None:
            d = k - len(path)  # 还要选 d 个数
            if d == 0:  # 选好了
                ans.append(path.copy())
                return

            # 不选 i
            if i > d:
                dfs(i - 1)

            # 选 i
            path.append(i)
            dfs(i - 1)
            path.pop()  # 恢复现场

        dfs(n)  # 从 i=n 开始倒着枚举
        return ans
#78. 子集
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
#方法一：选或不选（输入的视角）
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []

        def dfs(i: int) -> None:
            if i == n:  # 子集构造完毕
                ans.append(path.copy())  # 复制 path，也可以写 path[:]
                return
                
            # 不选 nums[i]
            dfs(i + 1)
            
            # 选 nums[i]
            path.append(nums[i])
            dfs(i + 1)
            path.pop()  # 恢复现场

        dfs(0)
        return ans
#方法二：枚举选哪个（答案的视角）
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []

        def dfs(i: int) -> None:
            ans.append(path.copy())  # 复制 path
            for j in range(i, n):  # 枚举选择的数字
                path.append(nums[j])
                dfs(j + 1)
                path.pop()  # 恢复现场

        dfs(0)
        return ans
#79. 单词搜索
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:  # 匹配失败
                return False
            if k == len(word) - 1:  # 匹配成功！
                return True
            board[i][j] = ''  # 标记访问过
            for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):  # 相邻格子
                if 0 <= x < m and 0 <= y < n and dfs(x, y, k + 1):
                    return True  # 搜到了！
            board[i][j] = word[k]  # 恢复现场
            return False  # 没搜到
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))
#80. 删除有序数组中的重复项 II
# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
# 说明：
# 为什么返回数值是整数，但输出的答案是数组呢？
# 请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
# 你可以想象内部操作如下:
# // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
# int len = removeDuplicates(nums);
# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        for i in range(len(nums)):
            if k<2 or nums[i]!=nums[k-2]:
                nums[k]=nums[i]
                k+=1
        return k       
        
            