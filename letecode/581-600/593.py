#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/5/18 下午4:00
"""
"""593. 有效的正方形
给定二维空间中四点的坐标，返回四点是否可以构造一个正方形。

一个点的坐标（x，y）由一个有两个整数的整数数组表示。

示例:

输入: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
输出: True
 

注意:

所有输入整数都在 [-10000，10000] 范围内。
一个有效的正方形有四个等长的正长和四个等角（90度角）。
输入点没有顺序。"""


class Solution:
    def validSquare(self, p1, p2, p3, p4) -> bool:
        if p1 == p2 == p3 == p4:
            return False
        points = sorted([p1, p2, p3, p4])

        def compute_len(a, b):
            return ((a[1] - b[1]) ** 2 + (a[0] - b[0]) ** 2)

        def cross(a, b, c):
            return abs((b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]))

        length = compute_len(points[0], points[1])
        print(length, compute_len(points[0], points[2]), compute_len(points[3], points[
            1]), compute_len(points[3], points[2]), length ** 2, cross(*points[:3]))
        return length == compute_len(points[0], points[2]) == compute_len(points[3], points[
            1]) == compute_len(points[3], points[2]) and length == cross(*points[:3])


if __name__ == '__main__':
    sol = Solution()
    print(sol.validSquare([0, 0]
                          [0, 0]
                          [0, 0]
                          [0, 0]))
