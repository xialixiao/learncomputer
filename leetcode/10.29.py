#292. Nim 游戏
# 你和你的朋友，两个人一起玩 Nim 游戏：
# 桌子上有一堆石头。
# 你们轮流进行自己的回合， 你作为先手 。
# 每一回合，轮到的人拿掉 1 - 3 块石头。
# 拿掉最后一块石头的人就是获胜者。
# 假设你们每一步都是最优解。请编写一个函数，来判断你是否可以在给定石头数量为 n 的情况下赢得游戏。如果可以赢，返回 true；否则，返回 false 。
class Solution:
    def canWinNim(self,n:int)->bool:
        return n%4!=0
#295. 数据流的中位数
# 中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。
# 例如 arr = [2,3,4] 的中位数是 3 。
# 例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
# 实现 MedianFinder 类:
# MedianFinder() 初始化 MedianFinder 对象。
# void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
# double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。
class MedianFinder:
    def __init__(self):
        self.A=[] #小顶堆
        self.B=[] #大顶堆
    def addNum(self,num:int)->None:
        if len(self.A)!=len(self.B):
            heappush(self.A,num)
            heappush(self.B,-heappop(self.A))
        else:
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))
    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0
#297. 二叉树的序列化与反序列化
# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
# 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
# 提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
class Codec:
    def serialize(self, root):
        if not root: return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else: res.append("null")
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        if data == "[]": return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root
#299. 猜数字游戏
# 你在和朋友一起玩 猜数字（Bulls and Cows）游戏，该游戏规则如下：
# 写出一个秘密数字，并请朋友猜这个数字是多少。朋友每猜测一次，你就会给他一个包含下述信息的提示：
# 猜测数字中有多少位属于数字和确切位置都猜对了（称为 "Bulls"，公牛），
# 有多少位属于数字猜对了但是位置不对（称为 "Cows"，奶牛）。也就是说，这次猜测中有多少位非公牛数字可以通过重新排列转换成公牛数字。
# 给你一个秘密数字 secret 和朋友猜测的数字 guess ，请你返回对朋友这次猜测的提示。
# 提示的格式为 "xAyB" ，x 是公牛个数， y 是奶牛个数，A 表示公牛，B 表示奶牛。
# 请注意秘密数字和朋友猜测的数字都可能含有重复数字。
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = 0
        cnt_s = Counter()
        cnt_g = Counter()
        for x, y in zip(secret, guess):
            if x == y:
                a += 1
            else:
                cnt_s[x] += 1
                cnt_g[y] += 1
        b = (cnt_s & cnt_g).total()
        return f"{a}A{b}B"

#300. 最长递增子序列
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
class Solution:
    def lengthOfLIS(self,nums:List[int])->int:
        f=[0]*len(nums)
        for i,x in enumerate(nums):
            for j,y in enumerate(nums[:i]):
                if x>j:
                    f[i]=max(f[i],f[j])
            f[i]+=1
        return max(f)