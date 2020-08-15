'''编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
'''

class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        public1 =''
        public2=''
        public=''
        for i in range(len(strs) - 1):
            if len(strs[i]) > len(strs[i + 1]):
                for j in range(len(strs[i + 1])):
                    if strs[i][j] == strs[i + 1][j]:
                        public1+=strs[i + 1][j]
            else:
                for j in range(len(strs[i])):
                    if strs[i][j] == strs[i + 1][j]:
                        public2+=strs[i + 1][j]
        if len(public1)>=len(public2):
            for k in range(len(public2)):
                if public1[k]==public2[k]:
                    public+=public1[k]
        else:
            for k in range(len(public1)):
                if public1[k]==public2[k]:
                    public+=public1[k]
        if public ==None:
            return ''
        return public


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))
