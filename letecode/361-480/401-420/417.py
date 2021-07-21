#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/12/8 下午5:04
"""
"""417. 太平洋大西洋水流问题
给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。

规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。

请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。

提示：

输出坐标的顺序不重要
m 和 n 都小于150
 
示例：

给定下面的 5x5 矩阵:

  太平洋 ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * 大西洋

返回:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元)."""


class Solution:
    def pacificAtlantic(self, matrix):
        def search(i, j, res):
            res.add((i, j))
            for x, y in dir:
                if 0 <= i + x < row and 0 <= j + y < col and matrix[i][j] <= matrix[i + x][j + y] and (
                        i + x, j + y) not in res:
                    search(i + x, j + y, res)

        if not matrix or not matrix[0]:
            return []
        row, col = len(matrix), len(matrix[0])
        # 太平洋
        pacific = set()
        # 大西洋
        atlantic = set()
        dir = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        for i in range(row):
            search(i, 0, pacific)
            search(i, col - 1, atlantic)
        for j in range(col):
            search(0, j, pacific)
            search(row - 1, j, atlantic)

        return pacific & atlantic


if __name__ == '__main__':
    sol = Solution()
    m = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    m = [[10, 10, 10],
         [10, 1, 10],
         [10, 10, 10]]
    m = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]

    print(sol.pacificAtlantic(m))
