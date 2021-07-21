#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/3/2 14:58
"""
"""面试题21. 调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。
 
提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10000"""


class Solution:
    def exchange(self, nums):
        l = len(nums) - 1
        i = 0
        while i < l:
            while i < l:
                if nums[i] % 2 == 0:
                    break
                else:
                    i += 1
            while i < l:
                if nums[l] % 2 != 0:
                    break
                else:
                    l -= 1
            if i < l:
                nums[i], nums[l] = nums[l], nums[i]
                i += 1
                l -= 1
        return nums


if __name__ == '__main__':
    sol = Solution()
    print(sol.exchange([1, 2, 3, 4]))
