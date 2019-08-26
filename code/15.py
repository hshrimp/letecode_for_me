#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-08-16 09:24
"""
"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def threeSum(self, nums):
        d = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        li = sorted([nums[i], nums[j], nums[k]])
                        if li not in d:
                            d.append(li)
        return d

    def threeSum2(self, nums):
        d = []
        dic = {}
        # nums = sorted(nums)
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        if 0 in dic and dic[0] >= 3:
            d.append([0, 0, 0])
        neg = [k for k in dic if k < 0]
        pos = [k for k in dic if k > 0]
        for n in neg:
            for p in pos:
                num = 0 - n - p
                if num in dic:
                    if num in [n, p] and dic[num] > 1:
                        d.append([n, num, p])
                    if n < num < p:
                        d.append([n, num, p])
        return d

    def threeSum3(self, nums):
        nums_hash = {}
        result = list()
        nums.sort()
        for num in nums:
            nums_hash[num] = nums_hash.get(num, 0) + 1
        if 0 in nums_hash and nums_hash[0] >= 3:
            result.append([0, 0, 0])

        neg = list(filter(lambda x: x < 0, nums_hash))
        pos = list(filter(lambda x: x >= 0, nums_hash))

        for i in neg:
            for j in pos:
                dif = 0 - i - j
                if dif in nums_hash:
                    if dif in (i, j) and nums_hash[dif] >= 2:
                        result.append([i, j, dif])
                    if dif < i or dif > j:
                        result.append([i, j, dif])
        return result


if __name__ == '__main__':
    sol = Solution()
    nums=[-4, -2, -1, 0, 1, 2, -1, -4]
    print(sol.threeSum(nums))
    print(sol.threeSum2(nums))
    print(sol.threeSum3(nums))
