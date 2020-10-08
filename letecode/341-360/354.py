#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/25 上午10:38
"""
"""354. 俄罗斯套娃信封问题
给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，
这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

说明:
不允许旋转信封。

示例:

输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出: 3 
解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。"""


class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        if not envelopes:
            return 0
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        length = len(envelopes)
        dp = [1] * length
        for i in range(1, length):
            dp[i] = max(
                [dp[j] for j in range(i) if envelopes[i][1] > envelopes[j][1]], default=0) + 1
        return max(dp)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxEnvelopes([[4, 5], [4, 6], [6, 7], [2, 3], [1, 1], [4, 7], [4, 2]]))
