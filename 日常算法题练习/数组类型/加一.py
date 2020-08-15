'''
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

'''


class Solution:
    def plusOne(self, digits: list) -> list:
        digits.reverse()
        digits.append(0)
        digits[0] += 1
        for i in range(len(digits) - 1):
            if digits[i] == 10:
                digits[i] -= 10
                digits[i + 1] += 1
        digits.reverse()
        return digits if digits[0] != 0 else digits[1:]
        # for index, i in enumerate(digits[::-1]):
        #     print(index, i)
        # a = [i * 10 ** index for index, i in enumerate(digits[::-1])]
        # print(a)
        # num = sum(a) + 1
        # for x in str(num):
        #     print(x)
        # return [int(x) for x in str(num)]


print(Solution().plusOne([4, 3, 2, 1]))
# 思路，先进行翻转，且最开始的位数不会以0开头，