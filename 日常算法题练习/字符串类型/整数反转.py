'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
输入: 123
输出: 321

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
'''


class Solution:
    def reverse(self, x: int) -> int:
        a = f"{x}"
        b = []
        for i in a:
            b.append(i)
        b.reverse()
        x = int((''.join(b).replace(",", '')))
        if x >= -2 ** 31 and x <= 2 ** 31 - 1:
            return x
        return 0


if __name__ == '__main__':
    print(Solution().reverse(123523213))
# 解题思路：
# 将int转换为字符串，再放入到列表中，利用列表的反转函数
# 列表再次转为字符串，替换掉","之后再转为int


#也可以转为字符串，通过切片方式，直接将字符串反转
#x=f'{x}'[::-1]