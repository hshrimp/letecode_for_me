#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/24 上午10:25
"""
"""352. 将数据流变为多个不相交区间
给定一个非负整数的数据流输入 a1，a2，…，an，…，将到目前为止看到的数字总结为不相交的区间列表。

例如，假设数据流中的整数为 1，3，7，2，6，…，每次的总结为：

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
 

进阶：
如果有很多合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办?"""

import bisect


class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def addNum(self, val: int) -> None:
        index = bisect.bisect(self.intervals, val)
        if index % 2 == 0:
            if 2 <= index < len(self.intervals) and val == self.intervals[index - 1] + 1 and val == self.intervals[
                index] - 1:
                self.intervals = self.intervals[:index - 1] + self.intervals[index + 1:]
            elif index >= 2 and val == self.intervals[index - 1] + 1:
                self.intervals[index - 1] = val
            elif index < len(self.intervals) and val == self.intervals[index] - 1:
                self.intervals[index] = val
            elif index >= 2 and val == self.intervals[index - 1]:
                return
            else:
                self.intervals.insert(index, val)
                self.intervals.insert(index + 1, val)

    def getIntervals(self):
        return [[self.intervals[i], self.intervals[i + 1]] for i in range(0, len(self.intervals), 2)]

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
