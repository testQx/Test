class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = {}
        for i in s:
            a[i] = s.count(i)
        print(a)

if __name__ == '__main__':
    Solution().firstUniqChar("loveleetcode")