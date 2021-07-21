#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/12/11 下午2:44
"""
"""421. 数组中两个数的最大异或值
给定一个非空数组，数组中元素为 a0, a1, a2, … , an-1，其中 0 ≤ ai < 231 。

找到 ai 和aj 最大的异或 (XOR) 运算结果，其中0 ≤ i,  j < n 。

你能在O(n)的时间解决这个问题吗？

示例:

输入: [3, 10, 5, 25, 2, 8]

输出: 28

解释: 最大的结果是 5 ^ 25 = 28."""


class Solution:
    def findMaximumXOR(self, nums) -> int:
        res = float('-inf')
        length = len(nums)
        for i in range(length - 1):
            for j in range(i, length):
                res = max(res, nums[i] ^ nums[j])
        return res if res != float('-inf') else 0

    def findMaximumXOR2(self, nums) -> int:
        l = len(bin(max(nums))) - 2
        nums = [[n >> i & 1 for i in range(l)][::-1] for n in nums]
        trie = {}
        res = 0
        for num in nums:
            cur = trie
            search_trie = trie
            cur_res = 0
            for c in num:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
                ops = 1 - c
                if ops in search_trie:
                    cur_res = (cur_res << 1) | 1
                    search_trie = search_trie[ops]
                else:
                    cur_res = cur_res << 1
                    search_trie = search_trie[c]
            res = max(res, cur_res)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaximumXOR([3, 10, 5, 25, 2, 8]))
    print(sol.findMaximumXOR2([3, 10, 5, 25, 2, 8]))
