#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/1/5 下午6:32
"""
"""447. 回旋镖的数量
给定平面上 n 对 互不相同 的点 points ，其中 points[i] = [xi, yi] 。回旋镖 是由点 (i, j, k) 表示的元组 ，
其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

返回平面上所有回旋镖的数量。
 
示例 1：

输入：points = [[0,0],[1,0],[2,0]]
输出：2
解释：两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
示例 2：

输入：points = [[1,1],[2,2],[3,3]]
输出：2
示例 3：

输入：points = [[1,1]]
输出：0
 
提示：

n == points.length
1 <= n <= 500
points[i].length == 2
-104 <= xi, yi <= 104
所有点都 互不相同"""


class Solution:
    def numberOfBoomerangs(self, points) -> int:
        def compute_distance(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        from collections import defaultdict
        length = len(points)
        map_count = [defaultdict(int) for _ in range(length)]
        for i in range(length - 1):
            for j in range(i + 1, length):
                distance = compute_distance(points[i], points[j])
                map_count[i][distance] += 1
                map_count[j][distance] += 1
        res = 0
        for d in map_count:
            for val in d.values():
                if val > 1:
                    res += val * (val - 1)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]))
