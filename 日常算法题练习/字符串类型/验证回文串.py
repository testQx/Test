'''给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
输入: "A man, a plan, a canal: Panama"
输出: true
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ', '').replace(',', '').replace(':', '')
        return s.lower() == s[::-1].lower()


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
