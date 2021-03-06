#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/30 下午4:17
"""
"""216. 组合总和 III
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]"""


class Solution:
    def combinationSum3(self, k: int, n: int):
        def find(k, n, num, li):
            # print(k, n, num, li)
            if k == 0 and n == 0:
                res.append(li)
                return
            for i in range(num, 10):
                if i <= n:
                    find(k - 1, n - i, i + 1, li + [i])

        res = []
        find(k, n, 1, [])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum3(k=3, n=17))
