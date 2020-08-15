'''给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
输入: s = "anagram", t = "nagaram"
输出: true

输入: s = "rat", t = "car"
输出: false
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        b = {}
        for i in s:
            a[i] = s.count(i)
        for i in t:
            b[i] = t.count(i)
        return a == b


if __name__ == '__main__':
    print(Solution().isAnagram("anagram", "nagaram"))
    print(Solution().isAnagram("rat", "cat"))
