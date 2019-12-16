#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-09-10 10:18
"""
"""假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def search(self, nums, target: int) -> int:
        res = -1
        try:
            res = nums.index(target)
        except:
            pass
        return res

    def search2(self, nums, target: int) -> int:
        if target == nums[0]:
            return 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                p = i
                break
        if target > nums[0]:
            for i in range(1, len(nums[:p])):
                if target == nums[i]:
                    return i
                if target < nums[i]:
                    return -1
        if target < nums[0]:
            for i in range(len(nums[p:])):
                if target == nums[p + i]:
                    return p + i
                if target < nums[p + i]:
                    return -1
        return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 8
    sol = Solution()
    print(sol.search(nums, target))
    print(sol.search2(nums, target))
