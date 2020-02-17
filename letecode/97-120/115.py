#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/2/14 11:13
"""
"""给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

示例 1:

输入: S = "rabbbit", T = "rabbit"
输出: 3
解释:

如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
示例 2:

输入: S = "babgbag", T = "bag"
输出: 5
解释:

如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。 
(上箭头符号 ^ 表示选取的字母)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distinct-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        res = 0
        l = len(t)

        def helper(s, t, l):
            if not t:
                nonlocal res
                res += 1
                return
            else:
                while t[0] in s and len(s) >= l:
                    index = s.index(t[0])
                    s = s[index + 1:]
                    helper(s, t[1:], l - 1)

        helper(s, t, l)
        return res

    def numDistinct2(self, s: str, t: str) -> int:
        sl = len(s)
        tl = len(t)
        if sl < tl or not sl:
            return 0
        dp = [[0] * sl for _ in range(tl)]
        if s[0] == t[0]:
            dp[0][0] = 1
        for i in range(1, sl):
            if s[i] == t[0]:
                dp[0][i] = dp[0][i - 1] + 1
            else:
                dp[0][i] = dp[0][i - 1]
        for i in range(1, tl):
            for j in range(i, sl):
                if t[i] == s[j]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    s = "babgbag"
    t = "bag"
    print(s, t, sol.numDistinct(s, t))
    print(s, t, sol.numDistinct2(s, t))
