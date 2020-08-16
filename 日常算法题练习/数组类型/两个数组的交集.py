'''给定两个数组，编写一个函数来计算它们的交集。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]

'''


class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        '''双指针'''
        nums1.sort()
        nums2.sort()

        length1, length2 = len(nums1), len(nums2)
        intersection = list()
        index1 = index2 = 0
        while index1 < length1 and index2 < length2:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                intersection.append(nums1[index1])
                index1 += 1
                index2 += 1

        return intersection
        # 双指针，因为已经是有序的，同样下标时，若nums1小，则nums1上的指针继续移动，或者另一个nums1的指针继续移动；当相等时，则添加到新列表中，此时两个指针都继续移动

        '''hash散列表'''
        # 思路：将两个数进行排序，后给两个指针同时从0开始出发，while中是控制移动长度，
        # 当num1中第一个值小于num2中的第一个值，则小的数index继续+1移动；当两个值相等，且加入到list中，则两个index都移动一次

        # from collections import Counter
        # c1 = Counter(nums1)
        # ans = []
        # for n in nums2:
        #     if n in c1 and c1[n] > 0:
        #         ans.append(n)
        #         c1[n] -= 1
        # return ans
        # 思路：通过hash，创建一个m的散列表，记录较短列表每次出现的值的次数，
        # 然后在长列表中依次对比，当发现这个值是hash散列表中有的，则添加进list中，且hash散列表中的计数-1

        '''hash散列表的原始过程'''
        # 以下是可以转换为hash，原本思路：
        # dct1 = defaultdict(int)
        # for i in nums1:
        #     dct1[i] += 1
        # print(dct1)
        # dct2 = defaultdict(int)
        # for i in nums2:
        #     dct2[i] += 1
        # print(dct2)
        # print(set(dct1) & set(dct2))
        # dct3 = {i: max(dct1[i], dct2[i]) for i in set(dct1) & set(dct2)}
        # print(dct3)
        # return sum([[key] * val for key, val in dct3.items()], [])


print(Solution().intersect([1, 1], [2, 1, 3]))
