#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/3/25 9:33
"""
"""892. 三维形体的表面积
在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。

每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。

请你返回最终形体的表面积。

示例 1：

输入：[[2]]
输出：10
示例 2：

输入：[[1,2],[3,4]]
输出：34
示例 3：

输入：[[1,0],[0,2]]
输出：16
示例 4：

输入：[[1,1,1],[1,0,1],[1,1,1]]
输出：32
示例 5：

输入：[[2,2,2],[2,1,2],[2,2,2]]
输出：46
 
提示：

1 <= N <= 50
0 <= grid[i][j] <= 50"""


class Solution:
    def surfaceArea(self, grid) -> int:
        if not grid:
            return 0
        direction = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        count = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                for d in direction:
                    if 0 <= i + d[0] < n and 0 <= j + d[1] < n:
                        count += grid[i][j] - grid[i + d[0]][j + d[1]] if grid[i][j] > grid[i + d[0]][j + d[1]] else 0
                    else:
                        count += grid[i][j]
                if grid[i][j]:
                    count += 2
        return count

    def surfaceArea2(self, grid) -> int:
        if not grid:
            return 0
        direction = {(1, 0), (0, 1)}
        count = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                for d in direction:
                    if 0 <= i + d[0] < n and 0 <= j + d[1] < n:
                        count += abs(grid[i][j] - grid[i + d[0]][j + d[1]])
                    else:
                        count += grid[i][j]
                if grid[i][j]:
                    count += 2
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.surfaceArea([[1, 0], [0, 2]]))
