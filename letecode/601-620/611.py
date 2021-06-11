#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-10-11 10:34
"""
"""给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

示例 1:

输入: [2,2,3,4]
输出: 3
解释:
有效的组合是: 
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3
注意:

数组长度不超过1000。
数组里整数的范围为 [0, 1000]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-triangle-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def triangleNumber(self, nums) -> int:
        res = 0
        nums.sort()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] > nums[k]:
                        res += 1
                    else:
                        break
        return res

    def triangleNumber2(self, nums) -> int:
        def find(li, left, right, num):
            while left < right:
                mid = left + (right - left) // 2
                if li[mid] >= num:
                    right = mid
                else:
                    left = mid + 1
            if nums[left] < num:
                return -1
            return left

        res = 0
        nums.sort()
        size = len(nums)
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                k = find(nums, j + 1, size - 1, nums[i] + nums[j])
                if k == -1:
                    # 说明子区间 [j + 1, size - 1] 全部的数都可以构成三角形
                    # 其中的数的个数为 size - 1 - (j + 1) + 1
                    res += (size - j - 1)
                else:
                    # 说明子区间 [j + 1, k) 全部的数可以构成三角形，注意：这里 k 取不到
                    # 其中的数的个数为 k - (j + 1)
                    res += (k - j - 1)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.triangleNumber([2, 2, 3, 4]))
    print(sol.triangleNumber2([2, 2, 3, 4]))
