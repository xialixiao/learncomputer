# #257. 二叉树的所有路径
# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
# 叶子节点 是指没有子节点的节点。
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def dfs(node: Optional[TreeNode], path: str) -> None:
            if node is None:
                return
            path += str(node.val)
            if node.left is None and node.right is None:  # 叶子节点
                ans.append(path)
                return
            path += "->"
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return ans
#258. 各位相加
#给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。
class Solution:
    def addDigits(self, num: int) -> int:
        return (num-1)%9+1 if num else 0
#260. 只出现一次的数字 III
# 给你一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。
# 你必须设计并实现线性时间复杂度的算法且仅使用常量额外空间来解决此问题。
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        #1.利用哈希表
        ant=Counter(nums)
        ans=[]
        for i,j in ant.items():
            if j==1:
                ans.append(i)
        return ans



 
