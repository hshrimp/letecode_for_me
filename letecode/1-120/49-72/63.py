#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-10-24 10:02
"""
"""一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            else:
                dp[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            else:
                dp[0][j] = 1
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[j][i] == 1:
                    dp[j][i] = 0
                else:
                    dp[j][i] = dp[j - 1][i] + dp[j][i - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    matrix = [[0], [1]]
    print(sol.uniquePathsWithObstacles(matrix))
