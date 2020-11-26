#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/29 下午5:33
"""
"""384. 打乱数组
打乱一个没有重复元素的数组。

示例:

// 以数字集合 1, 2 和 3 初始化数组。
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
solution.shuffle();

// 重设数组到它的初始状态[1,2,3]。
solution.reset();

// 随机返回数组[1,2,3]打乱后的结果。
solution.shuffle();"""

import random
from itertools import permutations


class Solution:

    def __init__(self, nums):
        self.nums = nums
        self.status = []
        for li in permutations(self.nums):
            self.status.append(list(li))
        self.length = len(self.status)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        index = random.randint(0, self.length - 1)
        return self.status[index]


class Solution2:

    def __init__(self, nums):
        self.nums = nums
        self.status = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.status)
        return self.status

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
