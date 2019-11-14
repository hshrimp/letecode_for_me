#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-11-12 10:37
"""
"""给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums = sorted(nums)

        def track(last, li, k):
            if len(li) == k:
                res.append(li)
                return
            for i in last:
                temp_last = list(last)
                temp_last.remove(i)
                if li and i > li[-1]:
                    temp_li = list(li)
                    temp_li.append(i)
                    track(temp_last, temp_li, k)
                elif not li:
                    track(temp_last, [i], k)

        for i in range(1, len(nums) + 1):
            track(nums, [], i)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.subsets([1, 2, 3]))
