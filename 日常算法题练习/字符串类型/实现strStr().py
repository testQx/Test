'''实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)

        # for i in range(0, len(haystack) - len(needle) + 1):
        for i in range(0, len(haystack) - 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


if __name__ == '__main__':
    print(Solution().strStr("aab2325bac", "325"))
# 解题思路，根据较短的部分，来将长字符串切割，将较短部分长度当为一个整理，长度减去之后+1为循环次数
# haystack[i:i + len(needle)] 用来表示有多少种较短部分长度的组合方式
