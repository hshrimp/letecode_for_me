#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/11/17 下午5:40
"""
"""391. 完美矩形
我们有 N 个与坐标轴对齐的矩形, 其中 N > 0, 判断它们是否能精确地覆盖一个矩形区域。

每个矩形用左下角的点和右上角的点的坐标来表示。例如， 一个单位正方形可以表示为 [1,1,2,2]。 
( 左下角的点的坐标为 (1, 1) 以及右上角的点的坐标为 (2, 2) )。

示例 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

返回 true。5个矩形一起可以精确地覆盖一个矩形区域。
 
示例 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

返回 false。两个矩形之间有间隔，无法覆盖成一个矩形。
 
示例 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

返回 false。图形顶端留有间隔，无法覆盖成一个矩形。
 
示例 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

返回 false。因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。"""


class Solution:
    def isRectangleCover(self, rectangles) -> bool:
        def check_cover(a, b):
            if a[0] >= b[2] or a[1] >= b[3] or a[2] <= b[0] or a[3] <= b[1]:
                return False
            else:
                return True

        length = len(rectangles)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if check_cover(rectangles[i], rectangles[j]):
                    return False
        min_p = min([[a[0], a[1]] for a in rectangles])
        max_p = max([[a[2], a[3]] for a in rectangles])
        count = 0
        for rec in rectangles:
            count += (rec[3] - rec[1]) * (rec[2] - rec[0])
        return (max_p[1] - min_p[1]) * (max_p[0] - min_p[0]) == count

    def isRectangleCover2(self, rectangles) -> bool:
        def check_cover(a, b):
            if a[0] < b[2] and a[1] < b[3] and a[2] > b[0] and a[3] > b[1]:
                return True
            else:
                return False

        length = len(rectangles)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if check_cover(rectangles[i], rectangles[j]):
                    return False
        min_p = min([[a[0], a[1]] for a in rectangles])
        max_p = max([[a[2], a[3]] for a in rectangles])
        count = 0
        for rec in rectangles:
            count += (rec[3] - rec[1]) * (rec[2] - rec[0])
        return (max_p[1] - min_p[1]) * (max_p[0] - min_p[0]) == count

    def isRectangleCover3(self, rectangles) -> bool:
        visited = set()
        count = 0
        for rec in rectangles:
            count += (rec[3] - rec[1]) * (rec[2] - rec[0])
            for tup in [(rec[0], rec[1]), (rec[2], rec[3]), (rec[0], rec[3]), (rec[2], rec[1])]:
                if tup in visited:
                    visited.remove(tup)
                else:
                    visited.add(tup)

        if len(visited) != 4:
            return False
        visited = sorted(visited)
        return count == (visited[3][0] - visited[0][0]) * (visited[3][1] - visited[0][1])


if __name__ == '__main__':
    sol = Solution()
    rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]

    print(sol.isRectangleCover(rectangles))
    print(sol.isRectangleCover2(rectangles))
    print(sol.isRectangleCover3(rectangles))
