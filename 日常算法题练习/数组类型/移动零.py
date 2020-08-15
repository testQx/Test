'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:


[1,1,0,3,1]
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
'''


class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index1, index2 = 0, 0
        while index2 < len(nums):
            if nums[index2] != 0:
                nums[index1], nums[index2] = nums[index2], nums[index1]
                index1 += 1
                index2 += 1
            else:
                index2 += 1
        return nums

        # count = 0
        # for i in nums:
        #     if i == 0:
        #         count += 1
        # while count > 0:
        #     nums.remove(0)
        #     count -= 1
        #     nums.append(0)
        # return nums


print(Solution().moveZeroes([1, 1, 0, 3, 1]))
# 思路：双指针，两两比较，0就往后挪，非0就往前赋值
# 计数0有多少个，然后全删除，再增加回来
