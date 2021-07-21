#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/4/23 下午4:04
"""
"""554. 砖墙
你的面前有一堵矩形的、由多行砖块组成的砖墙。 这些砖块高度相同但是宽度不同。你现在要画一条自顶向下的、穿过最少砖块的垂线。

砖墙由行的列表表示。 每一行都是一个代表从左至右每块砖的宽度的整数列表。

如果你画的线只是从砖块的边缘经过，就不算穿过这块砖。你需要找出怎样画才能使这条线穿过的砖块数量最少，并且返回穿过的砖块数量。

你不能沿着墙的两个垂直边缘之一画线，这样显然是没有穿过一块砖的。

示例：

输入: [[1,2,2,1],
      [3,1,2],
      [1,3,2],
      [2,4],
      [3,1,2],
      [1,3,1,1]]

输出: 2

解释: 

提示：

每一行砖块的宽度之和应该相等，并且不能超过 INT_MAX。
每一行砖块的数量在 [1,10,000] 范围内， 墙的高度在 [1,10,000] 范围内， 总的砖块数量不超过 20,000。"""


class Solution:
    def leastBricks(self, wall) -> int:
        res = 10000
        row = len(wall)
        col = 0
        for i in range(row):
            for j in range(1, len(wall[i])):
                wall[i][j] += wall[i][j - 1]
            if not col:
                col = wall[i][-1]
                if col == 1:
                    return row
            wall[i] = set(wall[i])
        for i in range(1, col):
            count = 0
            for j in range(row):
                if i not in wall[j]:
                    count += 1
            res = min(res, count)
        return res

    def leastBricks2(self, wall) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        row = len(wall)
        col = 0
        for i in range(row):
            temp = 0
            for j in range(len(wall[i]) - 1):
                temp += wall[i][j]
                d[temp] += 1
            if not col:
                col = temp + wall[i][-1]
                if col == 1:
                    return row
        return row - max(d.values())


if __name__ == '__main__':
    sol = Solution()
    m = [[1, 2, 2, 1],
         [3, 1, 2],
         [1, 3, 2],
         [2, 4],
         [3, 1, 2],
         [1, 3, 1, 1]]
    print(sol.leastBricks2(m))
    print(sol.leastBricks(m))
