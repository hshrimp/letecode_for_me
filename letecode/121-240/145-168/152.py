#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-06-04 14:27
"""
"""152. 乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。"""


class Solution:
    def maxProduct(self, nums) -> int:
        m = nums[0]
        length = len(nums)
        for i in range(length):
            temp = 1
            for j in range(i, length):
                temp *= nums[j]
                m = max(m, temp)
        return m

    def maxProduct2(self, nums) -> int:
        temp = [1]
        m = nums[0]
        for i in range(len(nums)):
            temp = [count * nums[i] for count in temp] + [nums[i]]
            m = max(temp + [m])
        return m

    def maxProduct3(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if 0 in nums:
            index = nums.index(0)
            return max(self.maxProduct3(nums[:index]), 0, self.maxProduct3(nums[index + 1:]))
        count = nums[0]
        for i in nums[1:]:
            count *= i
        if count >= 0:
            return count
        else:
            left = 1
            right = 1
            for i in nums:
                left *= i
                if left < 0:
                    break
            for i in nums[::-1]:
                right *= i
                if right < 0:
                    break
            return count // max(left, right)

    def maxProduct4(self, nums) -> int:
        max1, min1 = nums[0], nums[0]
        res = 0
        for i in range(1, len(nums)):
            max1, min1 = max(max1 * nums[i], max(min1 * nums[i], nums[i])), min(min1 * nums[i],
                                                                                min(max1 * nums[i], nums[i]))
            res = max(res, max1)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProduct([2, 3, -2, 4]))
    print(sol.maxProduct2([2, 3, -2, 4]))
    print(sol.maxProduct3([2, 0]))
    print(sol.maxProduct4([-4, -3, -2]))
