#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-09-18 09:35
"""
"""给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
说明:

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-missing-positive
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def firstMissingPositive(self, nums) -> int:
        for i in range(1, len(nums) + 1):
            if i not in nums:
                return i


if __name__ == '__main__':
    sol = Solution()
    print(sol.firstMissingPositive([3, 4, -1, 1, 2]))
