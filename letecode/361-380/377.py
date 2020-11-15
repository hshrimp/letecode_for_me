#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/28 下午5:04
"""
"""377. 组合总和 Ⅳ
给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。

示例:

nums = [1, 2, 3]
target = 4

所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

请注意，顺序不同的序列被视作不同的组合。

因此输出为 7。
进阶：
如果给定的数组中含有负数会怎么样？
问题会产生什么变化？
我们需要在题目中添加什么限制来允许负数的出现？

"""


class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        def find(li, tar):
            if tar == 0:
                if li not in res:
                    res.append(li)
                return
            for n in nums:
                if tar >= n:
                    find(li + [n], tar - n)

        res = []
        find([], target)
        return len(res)

    def combinationSum42(self, nums, target: int) -> int:
        dp = [0] * (target + 1)
        for n in nums:
            dp[n] = 1
        for i in range(1, target + 1):
            for n in nums:
                if i - n > 0:
                    dp[i] += dp[i - n]
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]
    target = 4
    print(sol.combinationSum4(nums, target))
    print(sol.combinationSum42(nums, target))
