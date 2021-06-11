#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-11-12 10:00
"""
"""给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        if k > n:
            return res
        nums = [i for i in range(1, n + 1)]

        def track(last, li, temp_k):
            if temp_k == 0:
                res.append(li)
            for i in last:
                if i > li[-1] and temp_k <= n - li[-1]:
                    temp_last = list(last)
                    temp_last.remove(i)
                    temp_li = list(li)
                    temp_li.append(i)
                    track(temp_last, temp_li, temp_k - 1)

        for i in nums:
            temp_nums = list(nums)
            temp_nums.remove(i)
            track(temp_nums, [i], k - 1)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.combine(4, 2))
