#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-06-10 15:43
"""
"""149. 直线上最多的点数
给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。

示例 1:

输入: [[1,1],[2,2],[3,3]]
输出: 3
解释:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
示例 2:

输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出: 4
解释:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6"""


class Solution:
    def maxPoints(self, points) -> int:
        from fractions import Fraction
        def get_slope(i, j):
            if points[j][0] - points[i][0]:
                slope = Fraction(points[j][1] - points[i][1], points[j][0] - points[i][0])
                b = points[j][1] - slope * points[j][0]
            else:
                slope = str(points[j][0])
                b = 0
            return tuple((slope, b))

        duplicate = {}
        last = []
        for point in points:
            if point not in last:
                last.append(point)
            else:
                index = last.index(point)
                if index in duplicate:
                    duplicate[index] += 1
                else:
                    duplicate[index] = 1
        points = last
        length = len(points)
        if length == 0:
            return 0
        if length == 1:
            return 1 + duplicate[0] if duplicate else 1
        slope2points = {get_slope(0, 1): {0, 1}}

        for i in range(2, length):
            for j in range(i):
                slope = get_slope(i, j)
                if slope not in slope2points:
                    slope2points[slope] = {j, i}
                else:
                    slope2points[slope].add(i)
        res = 0
        for k, v in slope2points.items():
            num = len(v)
            for i in v:
                if i in duplicate:
                    num += duplicate[i]
            res = max(res, num)
        return res


if __name__ == '__main__':
    sol = Solution()
    li = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    li = [[1, 1], [2, 2], [3, 3]]
    li = [[1, 1], [1, 1], [0, 0], [3, 4], [4, 5], [5, 6], [7, 8], [8, 9]]
    li = [[1, 1], [1, 1], [2, 3]]
    # li = [[0, 0], [94911151, 94911150], [94911152, 94911151]]

    print(sol.maxPoints(li))
