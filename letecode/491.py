#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/2/20 上午10:57
"""
"""491. 递增子序列
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:

输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
说明:

给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。"""


class Solution:
    def findSubsequences(self, nums):
        if not nums:
            return []
        visited = {(nums[0],)}
        res = [[nums[0]]]
        for num in nums[1:]:
            for i in range(len(res)):
                if num >= res[i][-1] and tuple(res[i] + [num]) not in visited:
                    res.append(res[i] + [num])
                    visited.add(tuple(res[i] + [num]))
            res.append([num])
            visited.add(tuple([num]))
        return [li for li in res if len(li) > 1]

    def findSubsequences2(self, nums):
        if not nums:
            return []
        visited = {(nums[0],)}
        for num in nums[1:]:
            visited.update({cur + (num,) for cur in visited if cur[-1] <= num})
            visited.add((num,))
        return [list(cur) for cur in visited if len(cur) > 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findSubsequences([4, 6, 7, 7]))
    print(sol.findSubsequences2([4, 6, 7, 7]))
