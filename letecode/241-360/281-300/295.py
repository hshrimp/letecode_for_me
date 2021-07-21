#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/8/11 下午2:49
"""
"""295. 数据流的中位数
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
进阶:

如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？"""


class MedianFinder2:
    # 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.seq = [0] * 101
        self.left = None
        self.right = None
        self.left_deep = None
        self.right_deep = None

    def addNum(self, num: int) -> None:
        self.seq[num] += 1
        if not self.left:
            self.left = self.right = num
            self.left_deep = self.right_deep = 1
        else:  # 数组非空
            if self.left == self.right and self.left_deep == self.right_deep:
                if num < self.left:
                    if self.left_deep > 1:
                        self.left_deep -= 1
                    else:
                        for i in range(self.left - 1, -1, -1):
                            if self.seq[i] > 0:
                                self.left = i
                                self.left_deep = self.seq[i]
                                break
                elif num == self.left:
                    self.right_deep += 1
                else:  # num>self.left=self.right
                    if self.right_deep < self.seq[self.right]:
                        self.left_deep += 1
                    else:
                        for i in range(self.right + 1, 101):
                            if self.seq[i] > 0:
                                self.right = i
                                self.right_deep = 1
                                break
            elif self.left == self.right and self.left_deep != self.right_deep:
                if num < self.left:
                    self.right_deep -= 1
                else:
                    self.left_deep += 1
            else:  # left<right
                if num < self.left:
                    self.right, self.right_deep = self.left, self.left_deep
                elif num == self.left:
                    self.left_deep += 1
                    self.right, self.right_deep = self.left, self.left_deep
                else:
                    self.left, self.left_deep = self.right, self.right_deep

    def findMedian(self) -> float:
        if self.left == self.right:
            return self.left
        else:
            return (self.left + self.right) / 2


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.seq = []
        self.length = 0

    def addNum(self, num: int) -> None:
        if not self.seq:
            self.seq.append(num)
        else:
            for i, n in enumerate(self.seq):
                if num < n:
                    self.seq.insert(i, num)
                    break
            else:
                self.seq.append(num)
        self.length += 1

    def findMedian(self) -> float:
        m1 = self.length / 2
        m2 = self.length // 2
        if m1 == m2:
            return (self.seq[m2] + self.seq[m2 - 1]) / 2
        else:
            return self.seq[m2]


import heapq


class MedianFinder11:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        self.count = 0

    def addNum(self, num: int) -> None:
        self.count += 1
        heapq.heappush(self.max_heap, (-num, num))
        _, max_heap_top = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, max_heap_top)
        if self.count & 1:
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, (-min_heap_top, min_heap_top))

    def findMedian(self) -> float:
        if self.count & 1:
            return self.max_heap[0][1]
        else:
            return (self.max_heap[0][1] + self.min_heap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
