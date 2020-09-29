#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/28 下午3:04
"""
"""376. 摆动序列
如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。
例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，
第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。

示例 1:

输入: [1,7,4,9,2,5]
输出: 6 
解释: 整个序列均为摆动序列。
示例 2:

输入: [1,17,5,10,13,15,10,5,16,8]
输出: 7
解释: 这个序列包含几个长度为 7 摆动序列，其中一个可为[1,17,10,13,10,16,8]。
示例 3:

输入: [1,2,3,4,5,6,7,8,9]
输出: 2
进阶:
你能否用 O(n) 时间复杂度完成此题?"""


class Solution:
    def wiggleMaxLength(self, nums) -> int:
        length = len(nums)
        if length <= 1:
            return length
        dp = [[0, 0] for _ in range(length)]
        dp[0][0] = 1
        for i in range(1, length):
            m = 0
            flag = 0
            for j in range(i):
                if nums[i] > nums[j] and dp[j][1] in [0, -1]:
                    m = max(m, dp[j][0] + 1)
                    flag = 1
                if nums[i] < nums[j] and dp[j][1] in [0, 1]:
                    m = max(m, dp[j][0] + 1)
                    flag = -1
                if nums[i] == nums[j]:
                    m = max(m, dp[j][0])
                    flag = dp[j][1]

            dp[i] = [m, flag]
        print(dp)
        return dp[-1][0]

    def wiggleMaxLength2(self, nums) -> int:
        length = len(nums)
        if length <= 1:
            return length
        up = [0] * length
        down = [0] * length
        up[0], down[0] = 1, 1
        for i in range(1, length):
            if nums[i] > nums[i - 1]:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            if nums[i] < nums[i - 1]:
                down[i] = up[i - 1] + 1
                up[i] = up[i - 1]
            if nums[i] == nums[i - 1]:
                down[i] = down[i - 1]
                up[i] = up[i - 1]
        return max(up[-1], down[-1])

    def wiggleMaxLength3(self, nums) -> int:
        length = len(nums)
        if length <= 1:
            return length
        up = 1
        down = 1
        for i in range(1, length):
            if nums[i] > nums[i - 1]:
                up = down + 1
            if nums[i] < nums[i - 1]:
                down = up + 1
        return max(up, down)

    def wiggleMaxLength4(self, nums) -> int:
        length = len(nums)
        if length <= 1:
            return length
        diff = nums[1] - nums[0]
        res = 1 if diff == 0 else 2
        for i in range(2, length):
            if (nums[i] > nums[i - 1] and diff <= 0) or (nums[i] < nums[i - 1] and diff >= 0):
                diff = nums[i] - nums[i - 1]
                res += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.wiggleMaxLength([0, 0]))
    print(sol.wiggleMaxLength2([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))
    print(sol.wiggleMaxLength3([1, 1, 7, 4, 9, 2, 5]))
    print(sol.wiggleMaxLength4([1, 1, 7, 4, 9, 2, 5]))
