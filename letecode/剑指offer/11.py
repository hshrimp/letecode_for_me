#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/2/25 16:44
"""
"""面试题11. 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/"""


class Solution:
    def minArray(self, numbers) -> int:
        for i in range(1, len(numbers)):
            if numbers[i] < numbers[i - 1]:
                return numbers[i]
        else:
            return numbers[0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minArray([2,3,4,0, 1]))
