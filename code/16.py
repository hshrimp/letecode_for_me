#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-08-20 09:39
"""
"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        close = float('inf')
        temp = 0
        for k in range(len(nums)-2):
            i = k + 1
            e = len(nums)-1
            while i < e:
                num = nums[k] + nums[i] + nums[e]
                count = num - target
                if count == 0:
                    return num
                if abs(count) < close:
                    close = abs(count)
                    temp = num
                if count > 0:
                    e -= 1
                if count < 0:
                    i += 1
        return temp

    def threeSumClosest2(self, nums, target):
        d = {}
        p = target / 3.0
        new = []
        for num in nums:
            num = num - p
            d[num] = d.get(num, 0) + 1
            new.append(num)
        if d[p] >= 3:
            return 0

        neg = [x for x in nums if x <= 0]
        pos = [x for x in nums if x > 0]
        for i in neg:
            for j in pos:
                pass


if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSumClosest([1, 2, 4, 8, 16, 32, 64, 128], 82))
