#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/7/20 下午5:10
"""
"""645. 错误的集合
集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，
导致集合 丢失了一个数字 并且 有一个数字重复 。

给定一个数组 nums 代表了集合 S 发生错误后的结果。

请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

示例 1：

输入：nums = [1,2,2,4]
输出：[2,3]
示例 2：

输入：nums = [1,1]
输出：[1,2]
 

提示：

2 <= nums.length <= 10**4
1 <= nums[i] <= 10**4"""


class Solution:
    def findErrorNums(self, nums):
        length = len(nums)
        r1 = sum(range(1, length + 1))
        r2 = sum(nums)
        nums = set(nums)
        for x in range(1, length + 1):
            if x not in nums:
                break
        return [r2 - r1 + x, x]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findErrorNums([1, 1]))
