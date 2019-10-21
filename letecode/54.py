#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-10-09 10:10
"""
"""给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def spiralOrder(self, matrix):
        res = []
        while sum(len(li) for li in matrix) > 0:
            res.extend(list(matrix[0]))
            del matrix[0]
            for li in matrix:
                res.append(li[-1])
                del li[-1]
            if sum(len(li) for li in matrix) > 0:
                res.extend(list(matrix[-1][::-1]))
                del matrix[-1]
            if sum(len(li) for li in matrix) > 0:
                for li in matrix[::-1]:
                    res.append(li[0])
                    del li[0]
        return res

    def spiralOrder2(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(map(list, zip(*matrix)))[::-1]
        return res


if __name__ == '__main__':
    sol = Solution()
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    # m = [
    #     [4],
    #     [8],
    #     [12]
    # ]
    # print(sol.spiralOrder(m))
    print(sol.spiralOrder2(m))
