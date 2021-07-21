#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-04-07 14:51
"""
"""面试题41. 数据流中的中位数
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
那么中位数就是所有数值排序之后中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例 1：

输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]
示例 2：

输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]

限制：

最多会对 addNum、findMedia进行 50000 次调用。
注意：本题与主站 295 题相同：https://leetcode-cn.com/problems/find-median-from-data-stream/"""


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.length = 0

    def find(self, num, start, end):
        if start + 1 == end:
            if self.nums[start] > num:
                self.nums.insert(start, num)
            else:
                self.nums.insert(end, num)
            return
        i = (end - start) // 2 + start
        if self.nums[i] < num:
            self.find(num, i, end)
        else:
            self.find(num, start, i)

    def addNum(self, num: int) -> None:
        if not self.nums:
            self.nums.append(num)
            self.length = 1
        else:
            self.find(num, 0, self.length)
            self.length += 1

    def findMedian(self) -> float:
        if self.length % 2 == 0:
            i = self.length // 2
            return (self.nums[i] + self.nums[i - 1]) / 2
        else:
            return self.nums[self.length // 2]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

    # Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
