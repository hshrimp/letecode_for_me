#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/31 上午10:23
"""
"""223. 矩形面积
在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。

每个矩形由其左下顶点和右上顶点坐标表示，如图所示。

Rectangle Area

示例:

输入: -3, 0, 3, 4, 0, -1, 9, 2
输出: 45
说明: 假设矩形面积不会超出 int 的范围。"""


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        if E < A:
            A, B, C, D, E, F, G, H = E, F, G, H, A, B, C, D
        if E < C <= G:
            x = C - E
        elif G < C:
            x = G - E
        else:
            x = 0
        if F < B:
            A, B, C, D, E, F, G, H = E, F, G, H, A, B, C, D
        if F < D <= H:
            y = D - F
        elif H < D:
            y = H - F
        else:
            y = 0
        return (C - A) * (D - B) + (G - E) * (H - F) - x * y

    def computeArea2(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        x = min(C, G) - max(A, E)
        y = min(D, H) - max(B, F)
        x = x if x > 0 else 0
        y = y if y > 0 else 0
        return (C - A) * (D - B) + (G - E) * (H - F) - x * y


if __name__ == '__main__':
    sol = Solution()
    print(sol.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
