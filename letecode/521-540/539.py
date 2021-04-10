#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/4/8 下午5:42
"""
"""539. 最小时间差
给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。

示例 1：

输入：timePoints = ["23:59","00:00"]
输出：1
示例 2：

输入：timePoints = ["00:00","23:59","00:00"]
输出：0
 

提示：

2 <= timePoints <= 2 * 104
timePoints[i] 格式为 "HH:MM"
"""


class Solution:
    def findMinDifference(self, timePoints) -> int:
        for i in range(len(timePoints)):
            hours, minute = timePoints[i].split(':')
            timePoints[i] = int(hours) * 60 + int(minute)
        timePoints.sort()
        res = 60 * 24 - timePoints[-1] + timePoints[0]
        for i in range(len(timePoints) - 1):
            res = min(res, timePoints[i + 1] - timePoints[i])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMinDifference(timePoints=["00:00", "23:59"]))
