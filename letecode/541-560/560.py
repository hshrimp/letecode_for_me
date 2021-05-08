#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/4/25 下午3:22
"""
"""560. 和为K的子数组
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。"""


class Solution:
    def subarraySum(self, nums, k: int) -> int:
        s = []
        res = 0
        begin = 0
        for n in nums:
            for i in range(begin, len(s)):
                s[i] += n
                if s[i] == k:
                    res += 1
            s.append(n)
            if n == k:
                res += 1
            print(s)

        return res

    def subarraySum2(self, nums, k: int) -> int:
        from collections import defaultdict
        s = defaultdict(int)
        res = 0
        for n in nums:
            temp = defaultdict(int)
            for key in s.keys():
                temp[key + n] += s[key]
            temp[n] += 1
            res += temp.get(k, 0)
            s = temp
            print(temp)
        return res

    def subarraySum3(self, nums, k: int) -> int:
        from collections import defaultdict
        s = defaultdict(int)
        s[0] = 1
        res = count = 0
        for n in nums:
            count += n
            if count - k in s:
                res += s[count - k]
            s[count] += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.subarraySum([28, 54, 7, -70, 22, 65, -6], 100))
    # print(sol.subarraySum2([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0))
    print(sol.subarraySum3([1, 1, 1], 2))
