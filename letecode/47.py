#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-09-29 10:23
"""
"""给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def permuteUnique(self, nums):
        all = []
        nums = sorted(nums)

        def run(li1, li2):
            if len(li2) == 1:
                if li1 + li2 not in all:
                    all.append(li1 + li2)
                return
            for i, n in enumerate(li2):
                if i > 0 and n == li2[i - 1]:
                    continue
                run(li1 + [n], li2[0:i] + li2[i + 1:])

        run([], nums)
        return all


if __name__ == '__main__':
    sol = Solution()
    print(sol.permuteUnique([1, 2, 1]))
