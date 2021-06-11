#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/5/10 下午3:03
"""
"""587. 安装栅栏
在一个二维的花园中，有一些用 (x, y) 坐标表示的树。由于安装费用十分昂贵，你的任务是先用最短的绳子围起所有的树。
只有当所有的树都被绳子包围时，花园才能围好栅栏。你需要找到正好位于栅栏边界上的树的坐标。

示例 1:

输入: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
输出: [[1,1],[2,0],[4,2],[3,3],[2,4]]
解释:

示例 2:

输入: [[1,2],[2,2],[4,2]]
输出: [[1,2],[2,2],[4,2]]
解释:

即使树都在一条直线上，你也需要先用绳子包围它们。
 

注意:

所有的树应当被围在一起。你不能剪断绳子来包围树或者把树分成一组以上。
输入的整数在 0 到 100 之间。
花园至少有一棵树。
所有树的坐标都是不同的。
输入的点没有顺序。输出顺序也没有要求。"""


class Solution:
    def outerTrees(self, trees):
        def cross(begin, mid, end):
            return (mid[0] - begin[0]) * (end[1] - mid[1]) - (mid[1] - begin[1]) * (end[0] - mid[0])

        def isbetween(begin, mid, end):
            a = begin[0] <= mid[0] <= end[0] or begin[0] >= mid[0] >= end[0]
            b = begin[1] <= mid[1] <= end[1] or begin[1] >= mid[1] >= end[1]
            return a and b

        if len(trees) < 3:
            return trees
        trees.sort()
        m = set()
        p = 0
        q = 1
        res = []
        while q != 0:
            res.append(trees[p])
            m.add(p)
            q = (p + 1) % len(trees)
            for r in range(len(trees)):
                if cross(trees[p], trees[q], trees[r]) < 0:
                    q = r

            for r in range(len(trees)):
                if r != p and r != q and cross(trees[p], trees[q], trees[r]) == 0 and isbetween(trees[p], trees[r],
                                                                                                trees[
                                                                                                    q]) and r not in m:
                    res.append(trees[r])
                    m.add(r)
            p = q
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.outerTrees(
        [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]))
