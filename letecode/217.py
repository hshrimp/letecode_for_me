#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/21 下午4:25
"""
"""217. 存在重复元素
给定一个整数数组，判断是否存在重复元素。

如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true"""


class Solution:
    def containsDuplicate(self, nums) -> bool:
        d = set()
        for num in nums:
            if num in d:
                return True
            else:
                d.add(num)
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.containsDuplicate([1,2,3,4]))
