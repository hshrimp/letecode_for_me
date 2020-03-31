#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/2/17 15:26
"""
"""给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def minimumTotal(self, triangle) -> int:
        seq = triangle[-1]
        for li in triangle[::-1][1:]:
            for i in range(len(li)):
                seq[i] = min(seq[i] + li[i], seq[i + 1] + li[i])
        return seq[0]


if __name__ == '__main__':
    sol = Solution()
    t = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(sol.minimumTotal(t))