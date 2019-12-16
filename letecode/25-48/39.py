#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-09-17 09:33
"""
"""给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def combinationSum(self, candidates, target: int):
        res = []
        candidates = sorted(candidates)

        def trackback(temp, tar):
            # print(candidates,temp,tar)
            if tar in candidates:
                t = sorted(temp + [tar])
                if t not in res:
                    res.append(t)
            for i, v in enumerate(candidates):
                if temp and temp[-1] > v:
                    continue
                if v > tar:
                    break
                trackback(temp + [v], tar - v)
            return

        trackback([], target)
        return res


if __name__ == '__main__':
    candidates = [2, 3, 7]
    target = 18
    sol = Solution()
    print(sol.combinationSum(candidates, target))
