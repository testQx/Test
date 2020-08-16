'''假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a = 1
        b = 2
        for i in range(3, n + 1):
            # t = b
            # b = a + b
            # a = t
            b, a = a + b, b
        return b

        # a = Solution()
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # else:
        #     return a.climbStairs(n - 1) + a.climbStairs(n - 2)


print(Solution().climbStairs(3))
# 解题思路：递归处理
#                                                                                                         c=3 a=2 b=3 ,下次c=5
# 斐波那契列算法：前一个值+后一个值=第三个值，1，1，2，3，5，8.....利用该规律 例如 a,b,c=1,2,3  下一次  a,b,c=2,3,5  c=a+b a=b b=c


# [1]  -> 1
# [1,2] -> 1,1   2
# [1,2,3]-> 1,1,1  1,2   2,1
# [1,2,3,4]->  1,1,1,1  1,2,1  1,1,2  2,1,1  2,2
