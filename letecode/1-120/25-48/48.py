#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-09-30 10:23
"""
"""给定一个 n × n 的二维矩阵表示一个图像。

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
示例 2:

给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-image
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = list(matrix)
        for i, v in enumerate(matrix):
            matrix[i] = [k[i] for k in m[::-1]]
        return matrix

    def rotate2(self, matrix) -> None:
        length = len(matrix[0])
        count = length // 2
        length -= 1
        for i in range(count):
            for j in range(i, length - i):
                matrix[j][length - i], matrix[length - i][length - j], matrix[length - j][i], matrix[i][j] = \
                    matrix[i][j], matrix[j][length - i], matrix[length - i][length - j], matrix[length - j][i]
        return matrix


if __name__ == '__main__':
    sol = Solution()
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    print(sol.rotate2(matrix))
    print(sol.rotate(matrix))
