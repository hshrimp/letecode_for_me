#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-11-22 10:16
"""
"""给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

示例:

输入: [2,1,5,6,2,3]
输出: 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        p = 1
        res = heights[0]
        while p <= len(heights):
            for j in range(len(heights) - p + 1):
                m = min(heights[j:j + p]) * p
                if m > res:
                    res = m
            p += 1
        return res

    def largestRectangleArea2(self, heights):
        heights = [0] + heights + [0]
        stack = []
        res = 0
        for i in range(len(heights)):
            print(stack, i)
            while stack and heights[stack[-1]] > heights[i]:
                t = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[t])
            stack.append(i)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestRectangleArea2([1, 2, 1, 5, 6, 2, 3]))
