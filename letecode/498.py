#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/2/28 上午11:47
"""
"""498. 对角线遍历
给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。

示例:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

输出:  [1,2,4,7,5,3,6,8,9]

解释:

说明:

给定矩阵中的元素总数不会超过 100000 。"""


class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        row, col = len(matrix), len(matrix[0])
        res = []
        for i in range(row + col - 1):
            cur = []
            if i < col:
                x = 0
                y = i
            else:
                x = i - col + 1
                y = col - 1
            while x < row and y >= 0:
                cur.append(matrix[x][y])
                x += 1
                y -= 1
            if i % 2 == 0:
                cur.reverse()
            # print(cur)
            res.extend(cur)
        return res


if __name__ == '__main__':
    sol = Solution()
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(sol.findDiagonalOrder(m))
