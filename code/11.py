#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-08-15 10:02
"""
"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxArea(self, height) -> int:
        if len(height) < 2:
            return 0
        max_water = 0
        length = len(height)
        for i in range(length):
            for j in range(i + 1, length):
                m = min(height[i], height[j])
                water = (j - i) * m
                if max_water < water:
                    max_water = water
        return max_water

    def maxArea2(self, height) -> int:
        i, j, max_water = 0, len(height) - 1, 0
        while i < j:
            water = (j - i) * min(height[i], height[j])
            if water > max_water:
                max_water = water
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_water


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxArea2([1, 8, 6, 2, 5, 4, 8, 3, 7]))
