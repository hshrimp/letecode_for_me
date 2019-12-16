#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-09-18 09:49
"""
"""给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def trap(self, height) -> int:
        length = len(height)
        if length < 3:
            return 0
        count = 0
        i, k = 0, 2
        while k < length:
            while i + 1 < length - 3 and height[i] < height[i + 1]:
                i += 1
                k = i + 2
            while k + 1 < length and height[k] < height[i] and height[k + 1] > height[k]:
                k += 1
            count += min(height[i], height[k]) * (k - i - 1) - sum(height[i + 1: k])
        return count

    def trap2(self, height):
        left = 0
        right = len(height) - 1
        ans = 0
        left_max = 0
        right_max = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += (left_max - height[left])
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += (right_max - height[right])
                right -= 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.trap2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
