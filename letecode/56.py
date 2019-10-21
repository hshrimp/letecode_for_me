#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-10-18 09:54
"""
"""给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def merge(self, intervals):
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
    print(sol.merge([[1, 3], [3, 6], [8, 10], [15, 18]]))
