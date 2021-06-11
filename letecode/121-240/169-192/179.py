#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/9 下午5:47
"""
"""179. 最大数
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。"""


class Solution:
    def largestNumber(self, nums) -> str:
        def find_max(temp):
            nonlocal res
            temp_res = list(res)
            for i in range(len(res) + 1):
                s1 = ''.join(temp_res)
                s2 = ''.join(res[:i] + [temp] + res[i:])
                if s2 > s1:
                    temp_res = res[:i] + [temp] + res[i:]
            res = temp_res

        length = len(nums)
        if length == 0:
            return ''
        if length == 1:
            return str(nums[0])
        if length == nums.count(0):
            return '0'
        res = [str(nums[0])]
        for i in range(1, len(nums)):
            temp = str(nums[i])
            find_max(temp)
        return ''.join(res)

    def largestNumber2(self, nums) -> str:
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return 0 if largest_num[0] == '0' else largest_num


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestNumber([3, 30, 34, 5, 9]))
    print(sol.largestNumber2([3, 30, 34, 5, 9]))
