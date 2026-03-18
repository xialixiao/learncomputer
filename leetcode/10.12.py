#121. 买卖股票的最佳时机
# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
class Solution:
    def maxProfit(self,prices:List[int])->int:
        ans=0
        min_price=prices[0]
        for p in prices:
            ans=max(ans,p-min_price)
            min_price=min(min_price,p)
        return ans
#122. 买卖股票的最佳时机 II
# 给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。
# 在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。然而，你可以在 同一天 多次买卖该股票，但要确保你持有的股票不超过一股。
# 返回 你能获得的 最大 利润 。
#1.贪心
class Solution:
    def maxProfit(self,prices:List[int])->int:
        profit=0
        for i in range(1,len(prices)):
            tmp=prices[i]-prices[i-1]
            if tmp>0:profit+=tmp
        return profit
#2.递归搜索+保存计算结构=记忆化搜索
class Solution:
    def maxProfit(self,prices:List[int])->int:
        n=len(prices)
        @cahce
        def dfs(i:int,hold:bool)->bool:
            if i<0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i-1,True),dfs(i-1,False)-prices[i])
            return max(dfs(i-1,False),dfs(i-1,True)+prices[i])
        return dfs(n-1,False)
#1:1翻译成堆
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f = [[0] * 2 for _ in range(n + 1)]
        f[0][1] = -inf
        for i, p in enumerate(prices):
            f[i + 1][0] = max(f[i][0], f[i][1] + p)
            f[i + 1][1] = max(f[i][1], f[i][0] - p)
        return f[n][0]
#空间优化
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f0, f1 = 0, -inf
        for p in prices:
            f0, f1 = max(f0, f1 + p), max(f1, f0 - p)
        return f0
#123. 买卖股票的最佳时机 III
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k=2
        f=[[-inf]*2 for _ in range(k+2)]
        for j in range(1,k+2):
            f[j][0]=0
        for p in prices:
            for j in range(k+1,0,-1):
                f[j][0]=max(f[j][0],f[j][1]+p)
                f[j][1]=max(f[j][1],f[j-1][0]-p)
        return f[-1][0]
#124. 二叉树中的最大路径和
# 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
# 路径和 是路径中各节点值的总和。
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。
class Solution:
    def maxPathSum(self,root:Optional[TreeNode])->int:
        ans=-inf
        def dfs(node:Optional[TreeNode])->int:
            if node is None:
                return 0
            l_val=dfs(node.left)
            r_val=dfs(node.right)
            nonlocal ans
            ans=max(ans,l_val+r_val+node.val)  # 两条链拼成路径
            return max(max(l_val,r_val)+node.val,0) # 当前子树最大链和（注意这里和 0 取最大值了）
        dfs(root)
        return ans
#125. 验证回文串
# 如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。
# 字母和数字都属于字母数字字符。
# 给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。
class Solution:
    def isPalindrome(self,s:str)->bool:
        i,j=0,len(s)-1
        while i<j:
            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            elif s[i].lower()==s[j].lower():
                i+=1
                j-=1
            else:
                return False
        return True
#126. 单词接龙 II*****
# 按字典 wordList 完成从单词 beginWord 到单词 endWord 转化，一个表示此过程的 转换序列 是形式上像 beginWord -> s1 -> s2 -> ... -> sk 这样的单词序列，并满足：
# 每对相邻的单词之间仅有单个字母不同。
# 转换过程中的每个单词 si（1 <= i <= k）必须是字典 wordList 中的单词。注意，beginWord 不必是字典 wordList 中的单词。
# sk == endWord
# 给你两个单词 beginWord 和 endWord ，以及一个字典 wordList 。请你找出并返回所有从 beginWord 到 endWord 的 最短转换序列 ，如果不存在这样的转换序列，返回一个空列表。每个序列都应该以单词列表 [beginWord, s1, s2, ..., sk] 的形式返回。
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        wordList.append(beginWord)    
        match_words,n=defaultdict(list),len(beginWord)
        for word in wordList:
            for i in range(n):
                directions=word[:i]+'_'+word[i+1:]
                match_words[directions].append(word)
        q=deque([(beginWord,1)])
        visited={beginWord:1}
        prewords=defaultdict(list)
        while q:
            cur_word,level=q.popleft()
            for i in range(n):
                directions=cur_word[:i]+'_'+cur_word[i+1:]
                for next_word in match_words[directions]:
                    if next_word not in visited:
                        visited[next_word]=level+1
                        q.append((next_word,level+1))
                    if visited[next_word]==level+1:
                        prewords[next_word].append(cur_word)
            if endWord in visited and visited[endWord]==level:
                break
        res=[]
        def dfs(path,word):
            if word==beginWord:
                res.append([word]+path[:])
                return
            for pre in prewords[word]:
                path=[word]+path
                dfs(path,pre)
                path=path[1:]
        dfs([],endWord)
        return res
#127. 单词接龙*****
# 字典 wordList 中从单词 beginWord 到 endWord 的 转换序列 是一个按下述规格形成的序列 beginWord -> s1 -> s2 -> ... -> sk：
# 每一对相邻的单词只差一个字母。
#  对于 1 <= i <= k 时，每个 si 都在 wordList 中。注意， beginWord 不需要在 wordList 中。
# sk == endWord
# 给你两个单词 beginWord 和 endWord 和一个字典 wordList ，返回 从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。如果不存在这样的转换序列，返回 0 。
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 更新给定队列 queue_，其对应的访问哈希表为 visited，并根据另一个哈希表判断当前单词是否在另一个方向已经搜索过了
        def update(queue: deque, visited: Dict[str, int], visited_other: Dict[str, int]) -> int:
            m = len(queue)
            # 类似树的层序遍历，当前队列中存储的节点都是与搜索起点距离相同的一层节点
            while m > 0: 
                curr_word = queue.popleft()     # 获取队首单词信息
                cnt = visited[curr_word] + 1      # 单词数递增
                # 枚举当前字符串的每一位，尝试以每一种字符可能替换得到新单词
                for i in range(n):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        next_word = curr_word[:i] + ch + curr_word[i+1:] # 替换当前位的字符
                        if next_word in visited_other:
                            #当前单词在另一个方向已经搜索过了，那么搜索到起点到终点的最短路径
                            return 1 + cnt + visited_other[next_word]
                        # 否则继续搜索
                        if next_word not in visited and next_word in words_lib:
                            # next_word这个单词没有处理过且在库里，是一个可转移的节点
                            visited[next_word] = cnt
                            queue.append(next_word)
                m -= 1
            return -1

        if len(beginWord) != len(endWord): return 0     # 起点终点字符串长度不一致，不可转换
        n = len(beginWord)     # 获取起点字符串长度
        # 使用哈希表构建单词库，以快速判断单词是否合法
        words_lib = set(wordList)
        if endWord not in words_lib: return 0   # 终点字符串不在单词库中，不可转换
        
        # 广度优先搜索搜索最短路径
        visited_front = {beginWord: 0}      # 记录从起点开始搜索过的单词和到达这个单词经历的单词数（不包含这个单词）;初始标记起点字符串已搜索，且单词数为0
        queue_front = deque()               # 正向广度优先搜索使用的队列，存储待搜索的单词
        queue_front.append(beginWord)       # 初始起点字符串单词入队

        visited_back = {endWord: 0}         # 记录从终点开始搜索过的单词;初始标记终点节点已搜索，且单词数为0
        queue_back = deque()                # 反向广度优先搜索使用的队列，存储待搜索的单词
        queue_back.append(endWord)          # 初始终点字符串单词入队

        while queue_front and queue_back:
            # 只要一个队列为空，说明有一个方向搜索完了还没找到最短路径，即不存在转换序列
            # 选出队列规模更少的进行搜索，减小搜索规模
            if len(queue_front) < len(queue_back):
                res = update(queue_front, visited_front, visited_back)
            else:
                res = update(queue_back, visited_back, visited_front)
            # 一旦找到最短路径，立即返回          
            if res != -1:
                return res
        return 0
#128. 最长连续序列
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
class Solution:
    def longestConsecutive(self,nums:List[int])->int:
        if len(nums)<=1:
            return len(nums)
        st=set(nums)
        st_d=list(st)
        st_d.sort()
        ans=1
        count=1
        i=1
        while i<len(st_d):
            if st_d[i]==st_d[i-1]+1:
                count+=1
                ans=max(count,ans)
            else:
                count=1
            i+=1
        return ans
#129. 求根节点到叶节点数字之和
# 给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
# 每条从根节点到叶节点的路径都代表一个数字：
# 例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
# 计算从根节点到叶节点生成的 所有数字之和 。
# 叶节点 是指没有子节点的节点。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #1.没有返回值
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(node:Optional[TreeNode],x:int)->None:
            if node is None:
                return
            x=x*10+node.val
            if node.left is None and node.right is None:
                nonlocal ans
                ans+=x
                return 
            dfs(node.left,x)
            dfs(node.right,x)
        dfs(root,0)
        return ans  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #2.有返回值
    def sumNumbers(self, root: Optional[TreeNode], x=0) -> int:
        if root is None:
            return 0
        x=x*10+root.val
        if root.left is None and root.right is None:
            return x
        return self.sumNumbers(root.left,x)+self.sumNumbers(root.right,x)
#130. 被围绕的区域
# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' 组成，捕获 所有 被围绕的区域：
# 连接：一个单元格与水平或垂直方向上相邻的单元格连接。
# 区域：连接所有 'O' 的单元格来形成一个区域。
# 围绕：如果您可以用 'X' 单元格 连接这个区域，并且区域中没有任何单元格位于 board 边缘，则该区域被 'X' 单元格围绕。
# 通过 原地 将输入矩阵中的所有 'O' 替换为 'X' 来 捕获被围绕的区域。你不需要返回任何值。
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #DFS
        m,n=len(board),len(board[0])
        #寻找边缘数据，把边缘数据给修改
        def dfs(i:int,j:int)->None:
            board[i][j]='F'  #将与边界相连的O标记为F
            for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0<=x<m and 0<=y<n and board[x][y]=='O':
                    dfs(x,y)
        for i in range(m):
            step=1 if i==0 or i==m-1 else n-1
            for j in range(0,n,step):
                if board[i][j]=='O':
                    dfs(i,j)
        #边缘数据修正，把中间数据修改
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':  # 将没有被标记的O修改为X
                    board[i][j]='X'
                elif board[i][j]=='F':  # 将与边界相连的O（已经被标记为F）修改回O
                    board[i][j]='O'
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #BFS
        m,n=len(board),len(board[0])
        q = deque()
        for i in range(m):
            step = 1 if i == 0 or i == m-1 else n-1 
            for j in range(0, n, step):
                if board[i][j] == 'O':
                    q.append((i, j))
        while q:
            i, j = q.popleft()
            board[i][j] = 'Y'
            for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                    q.append((x, y))
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Y':
                    board[i][j] = 'O'
            
        
      
    


 
