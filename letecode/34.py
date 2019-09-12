#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-09-11 09:54
"""
"""给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def searchRange(self, nums, target: int):
        if not nums:
            return [-1, -1]
        s, e = -1, -1
        p = len(nums) // 2
        point = p
        temp = list(nums)
        while len(nums) > 0 and p > 0:
            if target == nums[p]:
                s, e = point, point
                while s >= 0 and target == temp[s]:
                    s -= 1
                s += 1
                while e < len(temp) and target == temp[e]:
                    e += 1
                e -= 1
                break
            if target > nums[p]:
                nums = nums[p:]
                p = len(nums) // 2
                point += p
            if target < nums[p]:
                nums = nums[:p]
                p = len(nums) // 2
                point -= p + 1
                if len(nums) % 2 == 0:
                    point += 1
        if p == 0 and len(nums) == 1:
            if target == nums[0]:
                return [point, point]
        return [s, e]


if __name__ == '__main__':
    nums = [1, 1, 3, 4, 5, 5, 5, 5, 5]
    target = 3
    sol = Solution()
    print(sol.searchRange(nums, target))
