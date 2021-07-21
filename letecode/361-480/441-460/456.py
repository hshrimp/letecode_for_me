#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/1/6 下午3:10
"""
"""456. 132模式
给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < aj。
设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。

注意：n 的值小于15000。

示例1:

输入: [1, 2, 3, 4]

输出: False

解释: 序列中不存在132模式的子序列。
示例 2:

输入: [3, 1, 4, 2]

输出: True

解释: 序列中有 1 个132模式的子序列： [1, 4, 2].
示例 3:

输入: [-1, 3, 2, 0]

输出: True

解释: 序列中有 3 个132模式的的子序列: [-1, 3, 2], [-1, 3, 0] 和 [-1, 2, 0]."""


class Solution:
    def find132pattern(self, nums) -> bool:
        if not nums:
            return False
        length = len(nums)
        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                if nums[j] > nums[i]:
                    for k in range(j + 1, length):
                        if nums[i] < nums[k] < nums[j]:
                            return True
        return False

    def find132pattern2(self, nums) -> bool:
        if not nums:
            return False
        length = len(nums)
        for i in range(length - 2):
            j = i + 1
            while j < length:
                if nums[j] > nums[i]:
                    for k in range(j + 1, length):
                        if nums[k] > nums[j]:
                            j = k
                        else:
                            if nums[i] < nums[k] < nums[j]:
                                return True
                j += 1
        return False

    def find132pattern3(self, nums) -> bool:
        if not nums:
            return False
        length = len(nums)
        temp = set()
        left = 0
        for i in range(length - 2):
            if i != 0 and nums[i] >= nums[left]:
                continue
            left = i
            for j in range(length - 1, i + 1, -1):
                if nums[i] < nums[j]:
                    temp.add((i, j))
        for i, j in temp:
            if max(nums[i + 1:j]) > nums[j]:
                return True
        return False

    def find132pattern4(self, nums) -> bool:
        length = len(nums)
        if length < 3:
            return False
        mi = [nums[0]]
        for i in range(1, length):
            mi.append(min(mi[-1], nums[i]))
        stack = []
        for i in range(length - 1, 0, -1):
            if nums[i] > mi[i]:
                while stack and stack[-1] <= mi[i]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.find132pattern([-1, 3, 2, 0]))
    print(sol.find132pattern2([-1, 3, 2, 0]))
    print(sol.find132pattern3([-1, 3, 2, 0]))
    print(sol.find132pattern4([-1, 3, 2, 0]))
