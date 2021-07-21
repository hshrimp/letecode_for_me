#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-10-24 10:29
"""
"""在二维网格 grid 上，有 4 种类型的方格：

1 表示起始方格。且只有一个起始方格。
2 表示结束方格，且只有一个结束方格。
0 表示我们可以走过的空方格。
-1 表示我们无法跨越的障碍。
返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目，每一个无障碍方格都要通过一次。

示例 1：

输入：[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
输出：2
解释：我们有以下两条路径：
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
示例 2：

输入：[[1,0,0,0],[0,0,0,0],[0,0,0,2]]
输出：4
解释：我们有以下四条路径： 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
示例 3：

输入：[[0,1],[2,0]]
输出：0
解释：
没有一条路能完全穿过每一个空的方格一次。
请注意，起始和结束方格可以位于网格中的任意位置。
 
提示：

1 <= grid.length * grid[0].length <= 20

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = []
        count = 0
        height = len(grid)
        n = len(grid[0])
        for i in range(height):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 0:
                    count += 1
                elif grid[i][j] == 2:
                    end = (i, j)

        def trackback(matrix, num, point):
            if num == 0:
                if end in [(point[0] - 1, point[1]), (point[0] + 1, point[1]), (point[0], point[1] - 1),
                           (point[0], point[1] + 1)]:
                    res.append(1)
                return
            p, q = point
            li = [(p - 1, q), (p, q - 1), (p, q + 1), (p + 1, q)]
            for p, q in li:
                if 0 <= p < height and 0 <= q < n:
                    if matrix[p][q] == 0:
                        temp = list(list(l) for l in matrix)
                        temp[p][q] = -2
                        trackback(temp, num - 1, (p, q))

        trackback(grid, count, start)
        return sum(res)


if __name__ == '__main__':
    sol = Solution()
    grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
    print(sol.uniquePathsIII(grid))
