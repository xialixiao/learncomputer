#187. 重复的DNA序列
# DNA序列 由一系列核苷酸组成，缩写为 'A', 'C', 'G' 和 'T'.。
# *例如，"ACGAATTCCG" 是一个 DNA序列 。
# 在研究 DNA 时，识别 DNA 中的重复序列非常有用。
# 给定一个表示 DNA序列 的字符串 s ，返回所有在 DNA 分子中出现不止一次的 长度为 10 的序列(子字符串)。你可以按 任意顺序 返回答案。
#1.利用哈希表
#定义一个哈希表 cnt，用于存储所有长度为 10 的子字符串出现的次数。
#遍历字符串 s 的所有长度为 10 的子字符串，对于当前子字符串 t，我们更新其在哈希表中对应的计数。如果 t 的计数为 2，我们就将它加入答案。
#遍历结束后，返回答案数组即可。
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        cnt=Counter()
        ans=[]
        for i in range(len(s)-10+1):
            t=s[i:i+10]
            cnt[t]+=1
            if cnt[t]==2:
                ans.append(t)
        return ans
#188. 买卖股票的最佳时机 IV    
# 给你一个整数数组 prices 和一个整数 k ，其中 prices[i] 是某支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        f=[[-inf]*2 for _ in range(k+2)]
        for j in range(1,k+2):
            f[j][0]=0
        for p in prices:
            for j in range(k+1,0,-1):
                f[j][0]=max(f[j][0],f[j][1]+p)
                f[j][1]=max(f[j][1],f[j-1][0]-p)
        return f[-1][0]
#189. 轮转数组      
#给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 第一种:这种利用了一个新的数组，采用的deepcopy，不是简单的复制
        #时间复杂度O(n),空间复杂度O(n)
        n=len(nums)
        ans=deepcopy(nums)
        for i in range(n):
            nums[(i+k)%n]=ans[i]
 #浅拷贝和深拷贝的区别是：浅拷贝只是将原对象在内存中引用地址拷贝过来了。让新的对象指向这个地址。而深拷贝是将这个对象的所有内容遍历拷贝过来了，相当于跟原来没关系了，所以如果你这时候修改原来对象的值跟他没关系了，不会随之更改。
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #第二种：时间复杂度O(n),空间复杂度O(1)
        #把一个子数组反转两次，子数组的元素顺序不变。
        #注：请勿使用切片，会产生额外空间
        def  reverse(i:int,j:int)->None:
            while i<j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        n=len(nums)
        k%=n
        reverse(0,n-1) 
        reverse(0,k-1)
        reverse(k,n-1)   #一种思想的解法
#190. 颠倒二进制位       
#颠倒给定的 32 位有符号整数的二进制位。
class Solution:
    def reverseBits(self, n: int) -> int:
        #1.循环做法
        res=0
        for i in range(32):
            #1.res每次右移一位
            #2.n&1进行与操作，选出最后一维。
            #3.随后进行或操作，除了0与0才是0，其他都是1
            res=(res<<1) | (n&1)
            n>>=1
        return res

        

