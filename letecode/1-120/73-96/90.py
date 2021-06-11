#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-11-28 10:36
"""
"""给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        nums.sort()
        res = [[]]
        i = 2
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        temp_res = [[n] for n in d]
        res.extend(temp_res)
        while i <= len(nums):
            temp = []
            for r in temp_res:
                for n in nums:
                    if n >= r[-1] and r.count(n) < d[n] and r + [n] not in temp:
                        temp.append(list(r) + [n])
            res.extend(temp)
            temp_res = temp
            i += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.subsetsWithDup([1, 2, 3]))
