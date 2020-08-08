#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/8/3 下午4:32
"""
"""239. 滑动窗口最大值
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

进阶：

你能在线性时间复杂度内解决此题吗？

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

提示：

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length"""


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        res = []
        for i in range(len(nums) - k + 1):
            res.append(max(nums[i:i + k]))
        return res

    def maxSlidingWindow2(self, nums, k: int):
        res = [max(nums[:k])]
        index = nums.index(res[0])
        for i in range(1, len(nums) - k + 1):
            if i > index:
                res.append(max(nums[i:i + k]))
                index = i + nums[i:i + k].index(res[-1])
            else:
                if nums[i + k - 1] >= nums[index]:
                    res.append(nums[i + k - 1])
                    index = i + k - 1
                else:
                    res.append(nums[index])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
    print(sol.maxSlidingWindow2(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
