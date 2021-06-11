#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-09-29 10:06
"""
"""给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def permute(self, nums):
        all = []

        def run(li1, li2):
            if len(li2) == 1:
                all.append(li1 + li2)
                return
            for i, n in enumerate(li2):
                run(li1 + [n], li2[0:i] + li2[i + 1:])

        run([], nums)
        return all


if __name__ == '__main__':
    sol = Solution()
    print(sol.permute([1, 2, 3]))
