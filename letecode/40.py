#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-09-17 10:48
"""
"""给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def combinationSum2(self, candidates, target: int):
        res = []
        candidates = sorted(candidates)

        def trackback(temp, tar, can):
            # print(candidates,temp,tar)
            if not can:
                return
            if tar in can:
                t = sorted(temp + [tar])
                if t not in res:
                    res.append(t)
            for i, v in enumerate(can):
                if temp and temp[-1] > v:
                    continue
                if v > tar:
                    break
                temp_can = list(can)
                temp_can.remove(v)
                trackback(temp + [v], tar - v, temp_can)
            return

        trackback([], target, candidates)
        return res


if __name__ == '__main__':
    candidates = [2, 3, 7, 8]
    target = 18
    sol = Solution()
    print(sol.combinationSum2(candidates, target))
