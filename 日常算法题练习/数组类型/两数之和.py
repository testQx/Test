'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

 

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        # for i in range(len(nums)):
        #     for j in range(1,len(nums)):
        #         if i !=j:
        #             if nums[i]+nums[j]==target:
        #                 return [i,j]
        for i in range(len(nums)):
            target_1 = target - nums[i]
            if target - nums[i] in nums[i + 1:]:
                nums[i] = ""
                return [i, nums.index(target_1)]


print(Solution().twoSum([2, 5, 5, 15], 10))

# 解题思路：两次循环去寻找符合的条件
# 或者 降低时间复杂度，通过一个值，即确认了另一个值的存在，则再if中可以控制不重复使用同样的数
