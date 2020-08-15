'''给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
s = "leetcode"
返回 0

s = "loveleetcode"
返回 2
'''


class Solution:
    def firstUniqChar(self, s: str) -> int:

        for i in range(len(s)):
            if s[i] not in s[i + 1:len(s)]:
                return i
        return -1


if __name__ == '__main__':
    print(Solution().firstUniqChar("leetcode"))

# 解题思路：先取得下标；如果第一位，不在后面的字符串里面，说明他是第一个不重复的值

#进阶，如果需要输出所有不重复的值
# a=[]
# for i in range(len(s)):
#     if s[i] not in s[i + 1:len(s)]:
#         a.append(i)
# return -1