#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-11-11 10:36
"""
"""给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-colors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c0 = 0
        c2 = len(nums) - 1
        i = 0
        while i <= c2:
            # print(nums, c0, c2, i)
            if nums[i] == 0:
                nums[i], nums[c0] = nums[c0], nums[i]
                c0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[c2] = nums[c2], nums[i]
                c2 -= 1
            else:
                i += 1
        return nums


if __name__ == '__main__':
    sol = Solution()
    s = [2, 0, 2, 1, 1, 0]
    print(sol.sortColors(s))
