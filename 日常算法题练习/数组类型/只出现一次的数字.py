'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1

'''


class Solution:
    def singleNumber(self, nums: list) -> int:
        from collections import Counter
        datas = Counter(nums)
        print(datas)
        for each in datas:
            # 此时的each指的是key值
            if datas[each] == 1: return each


print(Solution().singleNumber([4, 4, 5]))
print(Solution().singleNumber([5, 4, 5]))

# 或者return 2 * sum(set(nums)) - sum(nums)
