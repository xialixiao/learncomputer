#241. 为运算表达式设计优先级
# 给你一个由数字和运算符组成的字符串 expression ，按不同优先级组合数字和运算符，计算并返回所有可能组合的结果。你可以 按任意顺序 返回答案。
# 生成的测试用例满足其对应输出值符合 32 位整数范围，不同结果的数量不超过 104 。
class Solution:
    def diffWaysToCompute(self, cs: str) -> List[int]:        
        def dfs(l: int, r: int) -> List[int]:
            ans = []
            for i in range(l, r + 1):
                if '0' <= cs[i] <= '9': continue
                l1, l2 = dfs(l, i - 1), dfs(i + 1, r)
                for a, b in product(l1, l2):
                    cur = 0
                    if cs[i] == '+':
                        cur = a + b
                    elif cs[i] == '-':
                        cur = a - b
                    else:
                        cur = a * b
                    ans.append(cur)
            if not ans:
                cur = 0
                for i in range(l, r + 1):
                    cur = cur * 10 + (ord(cs[i]) - ord('0'))
                ans.append(cur)
            return ans
        return dfs(0, len(cs) - 1)
#242. 有效的字母异位词
#给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的 字母异位词。
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)
        

