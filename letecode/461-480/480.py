#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/2/28 上午11:17
"""
"""480. 滑动窗口中位数
中位数是有序序列最中间的那个数。如果序列的长度是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。

例如：

[2,3,4]，中位数是 3
[2,3]，中位数是 (2 + 3) / 2 = 2.5
给你一个数组 nums，有一个长度为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。
你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。

示例：

给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。

窗口位置                      中位数
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7      -1
 1  3 [-1  -3  5] 3  6  7      -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
 因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。

提示：

你可以假设 k 始终有效，即：k 始终小于等于输入的非空数组的元素个数。
与真实值误差在 10 ^ -5 以内的答案将被视作正确答案。"""


class Solution:
    def medianSlidingWindow(self, nums, k: int):
        import bisect
        res = []
        seq = sorted(nums[:k])
        if k % 2 == 0:
            point2 = k // 2
            point1 = point2 - 1
            res.append((seq[point1] + seq[point2]) / 2)
            for i in range(1, len(nums) - k + 1):
                seq.remove(nums[i - 1])
                bisect.insort(seq, nums[i + k - 1])
                res.append((seq[point1] + seq[point2]) / 2)
            return res
        if k % 2 != 0:
            point = k // 2
            res.append(seq[point])
            for i in range(1, len(nums) - k + 1):
                print(seq, nums[i - 1], i)
                seq.remove(nums[i - 1])
                bisect.insort(seq, nums[i + k - 1])
                res.append(seq[point])
            return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.medianSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
