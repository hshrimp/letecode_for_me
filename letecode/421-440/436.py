#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/12/28 下午8:06
"""
"""436. 寻找右区间
给定一组区间，对于每一个区间 i，检查是否存在一个区间 j，它的起始点大于或等于区间 i 的终点，这可以称为 j 在 i 的“右侧”。

对于任何区间，你需要存储的满足条件的区间 j 的最小索引，这意味着区间 j 有最小的起始点可以使其成为“右侧”区间。如果区间 j 不存在，
则将区间 i 存储为 -1。最后，你需要输出一个值为存储的区间值的数组。

注意:

你可以假设区间的终点总是大于它的起始点。
你可以假定这些区间都不具有相同的起始点。
示例 1:

输入: [ [1,2] ]
输出: [-1]

解释:集合中只有一个区间，所以输出-1。
示例 2:

输入: [ [3,4], [2,3], [1,2] ]
输出: [-1, 0, 1]

解释:对于[3,4]，没有满足条件的“右侧”区间。
对于[2,3]，区间[3,4]具有最小的“右”起点;
对于[1,2]，区间[2,3]具有最小的“右”起点。
示例 3:

输入: [ [1,4], [2,3], [3,4] ]
输出: [-1, 2, -1]

解释:对于区间[1,4]和[3,4]，没有满足条件的“右侧”区间。
对于[2,3]，区间[3,4]有最小的“右”起点。
"""

from collections import defaultdict


class Solution:
    def findRightInterval(self, intervals):
        left_map = defaultdict(list)
        for i, val in enumerate(intervals):
            left_map[val[0]].append(i)
        res = []
        left = sorted(left_map.items(), key=lambda x: x[0])
        for val in intervals:
            if val[1] in left_map:
                res.append(left_map[val[1]][0])
                continue
            for a, b in left:
                if a > val[1]:
                    res.append(b[0])
                    break
            else:
                res.append(-1)
        return res

    def findRightInterval2(self, intervals):
        def find_(val_, left_, right_):
            if val_ > left[right_][0]:
                return
            while left_ < right_ - 1:
                mid = left_ + (right_ - left_) // 2
                if left[mid][0] > val_:
                    right_ = mid
                elif left[mid][0] < val_:
                    left_ = mid
            return right_

        left_map = defaultdict(list)
        for i, val in enumerate(intervals):
            left_map[val[0]].append(i)
        res = []
        left = sorted(left_map.items(), key=lambda x: x[0])
        length = len(left)
        for val in intervals:
            if val[1] in left_map:
                res.append(left_map[val[1]][0])
                continue
            find = find_(val[1], 0, length - 1)
            if find:
                res.append(left[find][1][0])
            else:
                res.append(-1)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRightInterval([[1, 4], [2, 3], [3, 4]]))
    print(sol.findRightInterval2([[4, 5], [2, 3], [1, 2]]))
