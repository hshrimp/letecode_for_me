#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-10-30 10:06
"""
"""给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i, line in enumerate(grid):
            for j, v in enumerate(line):
                if i == 0 and j != 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0 and i != 0:
                    grid[i][j] += grid[i - 1][j]
                elif i != 0 and j != 0:
                    grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    grid = \
        [
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]
    print(sol.minPathSum(grid))
