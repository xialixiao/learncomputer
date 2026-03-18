#131. 分割回文串
#给你一个字符串 s，请你将 s 分割成一些 子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
#输入的视角
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []

        # 考虑 i 后面的逗号怎么选
        # start 表示当前这段回文子串的开始位置
        def dfs(i: int, start: int) -> None:
            if i == n:  # s 分割完毕
                ans.append(path.copy())  # 复制 path
                return

            # 不分割，不选 i 和 i+1 之间的逗号
            if i < n - 1:  # i=n-1 时只能分割
                # 考虑 i+1 后面的逗号怎么选
                dfs(i + 1, start)

            # 分割，选 i 和 i+1 之间的逗号（把 s[i] 作为子串的最后一个字符）
            t = s[start: i + 1]
            if t == t[::-1]:  # 判断是否回文
                path.append(t)
                # 考虑 i+1 后面的逗号怎么选
                # start=i+1 表示下一个子串从 i+1 开始
                dfs(i + 1, i + 1)
                path.pop()  # 恢复现场

        dfs(0, 0)
        return ans
#答案的视角
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []

        # 考虑 s[i:] 怎么分割
        def dfs(i: int) -> None:
            if i == n:  # s 分割完毕
                ans.append(path.copy())  # 复制 path
                return
            for j in range(i, n):  # 枚举子串的结束位置
                t = s[i: j + 1]  # 分割出子串 t
                if t == t[::-1]:  # 判断 t 是不是回文串
                    path.append(t)
                    # 考虑剩余的 s[j+1:] 怎么分割
                    dfs(j + 1)
                    path.pop()  # 恢复现场

        dfs(0)
        return ans
#132. 分割回文串 II
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文串。
# 返回符合要求的 最少分割次数 。
class Solution:
    def minCut(self, s: str) -> int:
        # 返回 s[l:r+1] 是否为回文串
        @cache  # 缓存装饰器，避免重复计算 is_palindrome（一行代码实现记忆化）
        def is_palindrome(l: int, r: int) -> bool:
            if l >= r:
                return True
            return s[l] == s[r] and is_palindrome(l + 1, r - 1)

        @cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(r: int) -> int:
            if is_palindrome(0, r):  # 已是回文串，无需分割
                return 0
            res = inf
            for l in range(1, r + 1):  # 枚举分割位置
                if is_palindrome(l, r):
                    res = min(res, dfs(l - 1) + 1)  # 在 l-1 和 l 之间切一刀
            return res

        return dfs(len(s) - 1)
#133. 克隆图
# 给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。
# 图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
# 测试用例格式：
# 简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（val = 1），第二个节点值为 2（val = 2），以此类推。该图在测试用例中使用邻接列表表示。
# 邻接列表 是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。
# 给定节点将始终是图中的第一个节点（值为 1）。你必须将 给定节点的拷贝 作为对克隆图的引用返回。
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
#1.偷懒做法
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return copy.deepcopy(node)
#广搜
from typing import Optional
class Solution:
        
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None    # 空节点不拷贝
        clone_nodes = {node.val: Node(node.val)}  # 存储每一个拷贝过的节点，并克隆起点节点
        queue = [node]     # 用于广度优先搜索的队列，且起点节点入队
        while queue:
            cur = queue.pop(0)     # 从队列中获取一个待处理的节点
            clone_node = clone_nodes[cur.val]   # 待处理的节点一定是克隆好了的，直接获取其克隆节点
            for neighbor in cur.neighbors:
                # 处理当前节点的邻接节点
                if neighbor.val not in clone_nodes:
                    clone_nodes[neighbor.val] = Node(neighbor.val)  # 如果邻接节点未拷贝，则拷贝
                    queue.append(neighbor)      # 未拷贝的节点说明还没有处理，加入队列等待处理
                clone_node.neighbors.append(clone_nodes[neighbor.val])  # 将邻接节点的拷贝节点加入当前节点的拷贝节点的邻接列表
        return clone_nodes[node.val]    # 返回起点节点的克隆节点
#深搜
from typing import Optional
class Solution:
    def __init__(self):
        self.clone_nodes = {}  # 存储每一个克隆过的节点
        
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None    # 空节点不克隆
        if node.val in self.clone_nodes:
            return self.clone_nodes[node.val]    # 克隆了的节点不重复克隆
        
        clone_node = Node(node.val)    # 创建一个克隆后的节点
        self.clone_nodes[node.val] = clone_node       # 存储克隆节点
        for neighbor in node.neighbors:
            # 克隆节点 克隆 被克隆节点的邻接列表
            clone_node.neighbors.append(self.cloneGraph(neighbor))
        return clone_node
# 134. 加油站
# 在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
# 给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一 的。
class Solution:
    def canCompleteCircuit(self,gas:List[int],cost:List[int])->int:
        ans=min_s=s=0
        for i,(g,c) in enumerate(zip(gas,cost)):
            s+=g-c
            if s<min_s:
                min_s=s
                ans=i+1
        return -1 if s<0 else ans
#135. 分发糖果
# n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
# 你需要按照以下要求，给这些孩子分发糖果：
# 每个孩子至少分配到 1 个糖果。
# 相邻两个孩子中，评分更高的那个会获得更多的糖果。
# 请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。
class Solution:
    def candy(self, ratings: List[int]) -> int:
        left=[1 for _ in range(len(ratings))]
        right=left[:]
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:left[i]=left[i-1]+1
        count=left[-1]
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:right[i]=right[i+1]+1
            count+=max(left[i],right[i])
        return count
#136. 只出现一次的数字
# 给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。
#使用哈希
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_n=Counter(nums)
        for key,value in count_n.items():
            if value==1:
                return key
#137. 只出现一次的数字 II        
# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
# 你必须设计并实现线性时间复杂度的算法且使用常数级空间来解决此问题。
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones
#138. 随机链表的复制  
# 给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。
# 构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。
# 例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。
# 返回复制链表的头节点。
# 用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
# val：一个表示 Node.val 的整数。
# random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
# 你的代码 只 接受原链表的头节点 head 作为传入参数。
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        # 复制所有节点，插入原节点的后面
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next, None)
            cur = cur.next.next

        # 连接所有复制的节点的random指针
        cur = head
        copyHead = head.next
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        # 断开原链表与复制链表之间的连接
        cur = head
        cur_ = copyHead
        while cur and cur_:
            cur.next = cur_.next
            cur = cur.next
            if cur:
                cur_.next = cur.next
            cur_ = cur_.next
        return copyHead
#139. 单词拆分
# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。
# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        @cache
        def dfs(i):
            if i == n: return True
            for j in range(i+1, n+1):
                if s[i:j] in wordDict and dfs(j):
                    return True
            return False
        return dfs(0)
#140. 单词拆分 II
# 给定一个字符串 s 和一个字符串字典 wordDict ，在字符串 s 中增加空格来构建一个句子，使得句子中所有的单词都在词典中。以任意顺序 返回所有这些可能的句子。
# 注意：词典中的同一个单词可能在分段中被重复使用多次。
class Solution:
    # 超时
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        #
        wordDict = set(wordDict)

        def dfs(wordDict,temp,pos):
            #
            if pos == len(s):
                res.append(" ".join(temp))
                return
            for i in range(pos,len(s)+1):
                if s[pos:i] in wordDict:
                    temp.append(s[pos:i])
                    dfs(wordDict,temp,i)
                    temp.pop() 
            #
                       
            
        dfs(wordDict,[],0)
        return res