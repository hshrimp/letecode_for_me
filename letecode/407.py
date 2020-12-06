#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/12/1 上午10:31
"""
"""407. 接雨水 II
给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。

示例：

给出如下 3x6 的高度图:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

返回 4 。

如上图所示，这是下雨前的高度图[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] 的状态。

下雨后，雨水将会被存储在这些方块中。总的接雨水量是4。

提示：

1 <= m, n <= 110
0 <= heightMap[i][j] <= 20000"""

from heapq import heappush, heappop


class Solution:
    def trapRainWater(self, heightMap) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        row = len(heightMap)
        col = len(heightMap[0])
        if row < 3 or col < 3:
            return 0
        heap = []
        visited = set()
        for i in range(col):
            heappush(heap, [heightMap[0][i], 0, i])
            heappush(heap, [heightMap[-1][i], row - 1, i])
        for i in range(1, row - 1):
            heappush(heap, [heightMap[i][0], i, 0])
            heappush(heap, [heightMap[i][-1], i, col - 1])
        max_ = float('-inf')
        res = 0
        while heap:
            h, i, j = heappop(heap)
            max_ = max(max_, h)
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                temp_x = x + i
                temp_y = y + j
                if 0 < temp_x < row - 1 and 0 < temp_y < col - 1 and (temp_x, temp_y) not in visited:
                    visited.add((temp_x, temp_y))
                    if heightMap[temp_x][temp_y] < max_:
                        res += max_ - heightMap[temp_x][temp_y]
                    heappush(heap, [heightMap[temp_x][temp_y], temp_x, temp_y])
        return res


if __name__ == '__main__':
    sol = Solution()
    hm = [
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1]
    ]
    # hm = [
    #     [12, 13, 1, 12],
    #     [13, 4, 13, 12],
    #     [13, 8, 10, 12],
    #     [12, 13, 12, 12],
    #     [13, 13, 13, 13]
    # ]

    print(sol.trapRainWater(hm))
