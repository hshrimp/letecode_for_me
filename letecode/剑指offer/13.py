#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/2/26 12:05
"""
"""面试题13. 机器人的运动范围
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。
请问该机器人能够到达多少个格子？

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 1：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20"""


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        res = set()
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def count(num):
            co = 0
            while num >= 10:
                num, p = divmod(num, 10)
                co += p
            co += num
            return co

        def find(i, j):
            if (i, j) in res:
                return
            if k >= count(i) + count(j):
                res.add((i, j))
                for x, y in dir:
                    nx = i + x
                    ny = j + y
                    if 0 <= nx < n and 0 <= ny < m:
                        find(nx, ny)

        find(0, 0)
        return len(res)


if __name__ == '__main__':
    sol = Solution()
    print(sol.movingCount(2, 3, 1))
