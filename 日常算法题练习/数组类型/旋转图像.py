'''给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
'''


class Solution:
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        pos1, pos2 = 0, len(matrix) - 1
        while pos1 < pos2:
            add = 0
            while add < pos2 - pos1:
                # 左上角为0块，右上角为1块，右下角为2块，左下角为3块
                temp = matrix[pos2 - add][pos1]
                matrix[pos2 - add][pos1] = matrix[pos2][pos2 - add]
                # 3 = 2
                matrix[pos2][pos2 - add] = matrix[pos1 + add][pos2]
                # 2 = 1
                matrix[pos1 + add][pos2] = matrix[pos1][pos1 + add]
                # 1 = 0
                matrix[pos1][pos1 + add] = temp
                # 0 = temp
                add = add + 1
            pos1 = pos1 + 1
            pos2 = pos2 - 1
        return matrix


print(Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# 思路：按内外层循环两层
# 首先内层循环更改，即是4个点互换位置，先存储起最后一个点的内容，然后依次根据偏移量add来互换位置
# 内层循环更换完成，即最外层已经旋转了一圈，此时再往下一个内层循环走，所以pos1=pos1+1，横坐标+1
# post2=pos2-1 ,纵坐标-1，当pos1==pos2的时候，即只有一个格子，此时不继续旋转了
# 所以循环条件是pos1<pos2  或者pos1!=pos2
