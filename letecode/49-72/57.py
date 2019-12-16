#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-10-18 10:12
"""
"""给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1:

输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]
示例 2:

输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-interval
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        if len(intervals) < 2:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        i = 1
        while i < len(intervals):
            if intervals[i - 1][-1] >= intervals[i][0]:
                intervals[i - 1][-1] = max(intervals[i][-1], intervals[i - 1][-1])
                intervals.pop(i)
            else:
                i += 1
        return intervals


if __name__ == '__main__':
    sol = Solution()
    print(sol.insert([[1, 3], [3, 6], [8, 10], [15, 18]], [4, 7]))
