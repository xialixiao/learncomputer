#201. 数字范围按位与
#给你两个整数 left 和 right ，表示区间 [left, right] ，返回此区间内所有数字 按位与 的结果（包含 left 、right 端点）。
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        #求公共部分，cnt记录有多少位不一样
        cnt=0
        while left!=right:
            cnt+=1
            left>>=1
            right>>=1
        return left<<cnt 
#202. 快乐数
# 编写一个算法来判断一个数 n 是不是快乐数。
# 「快乐数」 定义为：
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果这个过程 结果为 1，那么这个数就是快乐数。
# 如果 n 是 快乐数 就返回 true ；不是，则返回 false 。
class Solution:
    def isHappy(self, n: int) -> bool:
        a=[]
        s=0
        while(True):
            for i in str(n):
                s+=int(i)**2
            n=s
            s=0
            if (n==1):
                return True
            #可能陷入循环
            if n in a:
                return False
            a.append(n)  
#203. 移除链表元素
#给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = dummy = ListNode(next=head)
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next  # 删除下一个节点
            else:
                cur = cur.next  # 继续向后遍历链表
        return dummy.next 
#204. 计数质数
#给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。
class Solution:
    def countPrimes(self, n: int) -> int:
        #1.暴力枚举，会超时
        count=0
        for i in range(2,n):
            sq=isqrt(i)
            prime=True
            for j in range(2,sq+1):
                if i % j==0:
                    prime=False
                    break
            count+=prime
        return count 
class Solution:
    def countPrimes(self, n: int) -> int:
        #埃氏筛
        if n<2:
            return 0
        isPrime=[1]*n
        isPrime[0]=isPrime[1]=0 #0和1不是质数
        #埃氏筛，把不大于根号 n 的所有质数的倍数剔除
        for i in range(2,isqrt(n)+1):
            if isPrime[i]:
                isPrime[i*i:n:i]=[0]*((n-1-i*i)//i+1)  # 指定步长参数，进行列表切片赋值，之所以从 i 的平方开始，是因为小于 i 的平方的倍数部分，在它之前就已经被排除掉了。
        return sum(isPrime) 
#205. 同构字符串
# 给定两个字符串 s 和 t ，判断它们是否是同构的。
# 如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
# 每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s))==len(set(t))==len(set(zip(s,t)))
#206. 反转链表
#给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
def reverseList(self, head: ListNode) -> ListNode:
    # 1. 递归终止条件
    if head is None or head.next is None:
        return head
    
    p = self.reverseList(head.next)
    head.next.next = head
    head.next = None

    return p
# 头插法的意思是，把一个节点 node 指向链表头节点（node.next 更新为链表头节点），那么 node 就插在了链表的左侧，新链表的头节点为 node。
# 对于链表 1→2→3，结合代码来说，顺序为：
# 第一轮循环结束后，得到链表 1。
# 第二轮循环结束后，得到链表 2→1。
# 第三轮循环结束后，得到链表 3→2→1。
# 注：代码每轮循环结束后，pre 表示最新得到的链表。

#迭代法（头插法）
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        #pre要一直指在最前面的数据
        while cur:
            nxt = cur.next
            cur.next = pre  # 把 cur 插在 pre 链表的前面（头插法）
            pre = cur
            cur = nxt
        return pre
#207. 课程表
# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
#已绕晕
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            g[b].append(a)

        colors = [0] * numCourses
        def dfs(x: int) -> bool:
            colors[x] = 1  # x 正在访问中
            for y in g[x]:
                if colors[y] == 1 or colors[y] == 0 and dfs(y):
                    return True  # 找到了环
            colors[x] = 2  # x 完全访问完毕
            return False  # 没有找到环

        for i, c in enumerate(colors):
            if c == 0 and dfs(i):
                return False  # 有环
        return True  # 没有环
#接下来利用拓扑排序的思想，也就是寻找入度=0的点，作为开头，往下走。
#BFS
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        # 每个节点的入度
        indegrees = [0] * numCourses
        
        # 邻接表
        graph = [[] for _ in range(numCourses)]
        
        # 填充初始邻接表和入度值
        for a, b in prerequisites:
            # 添加从课程 b 到课程 a 的有向边
            graph[b].append(a)
            # 课程 a 的入度加1
            indegrees[a] += 1
        
        # 使用队列进行拓扑排序
        queue = deque()
        
        # 首先找到所有头部节点（入度为 0 的节点）
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        
        # 执行拓扑排序
        while queue:
            # 当前节点
            cur = queue.popleft()
            # 获取当前节点的后继节点
            targets = graph[cur]
            
            # 遍历所有的后继节点，减少他们的入度
            for next_course in targets:
                # 减少入度
                indegrees[next_course] -= 1
                # 如果后继节点的入度为0，加入队列
                if indegrees[next_course] == 0:
                    queue.append(next_course)
        
        # 检查所有节点的入度是否都为0
        # 若存在入度不为0的节点，说明图中存在环，无法完成所有课程
        return all(degree == 0 for degree in indegrees)    
#DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i, adjacency, flags):
            if flags[i] == -1: return True
            if flags[i] == 1: return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags): return False
            flags[i] = -1
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags): return False
        return True
# #208. 实现 Trie (前缀树)
# Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补全和拼写检查。

# 请你实现 Trie 类：

# Trie() 初始化前缀树对象。
# void insert(String word) 向前缀树中插入字符串 word 。
# boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
# boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
class Trie:

    def __init__(self):
        """
        初始化前缀树。
        使用两个字典来存储单词和前缀。
        - words: 存储所有完整的单词。
        - prefix: 存储所有单词的前缀。
        """
        self.words = defaultdict(int)
        self.prefix = defaultdict(int)

    
    def insert(self, word: str) -> None:
        # 向前缀树中插入一个单词。
        self.words[word] = 1
        # 生成该单词的所有前缀并存入 prefix 字典
        for i in range(len(word)):
            s = word[0:i]
            self.prefix[s] = 1

    def search(self, word: str) -> bool:
        # 检查一个完整的单词是否存在于前缀树中。
        if word in self.words:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        # 检查是否有单词以前缀 prefix 开头。
        # 前缀可能是一个完整的单词，也可能是一个不完全的前缀
        if prefix in self.words or prefix in self.prefix:
            return True
        return False

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

#体现了树的思想。
class Node(object):
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False
        
class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current = self.root
        for w in word:
            current = current.children[w]
        current.isword = True

    def search(self, word):
        current = self.root
        for w in word:
            current = current.children.get(w)
            if current == None:
                return False
        return current.isword

    def startsWith(self, prefix):
        current = self.root
        for w in prefix:
            current = current.children.get(w)
            if current == None:
                return False
        return True
#209. 长度最小的子数组
# 给定一个含有 n 个正整数的数组和一个正整数 target 。

# 找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        tmp=left=0
        res=inf
        ans=0
        for right,i in enumerate(nums):
            ans+=i
            while ans>=target:
                res=min(right-left+1,res)
                ans-=nums[left]
                left+=1
        if res==inf:
            return 0
        return res   
# #210. 课程表 II
# 现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。

# 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。
# 返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        indeg = [0] * numCourses
        for a, b in prerequisites:
            g[b].append(a)
            indeg[a] += 1
        ans = []
        q = deque(i for i, x in enumerate(indeg) if x == 0)
        while q:
            i = q.popleft()
            ans.append(i)
            for j in g[i]:
                indeg[j] -= 1
                if indeg[j] == 0:
                    q.append(j)
        return ans if len(ans) == numCourses else []

