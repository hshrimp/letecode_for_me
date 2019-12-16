#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-09-19 10:48
"""
"""给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输入: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wildcard-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        while '**' in p:
            p = p.replace('**', '*')

        def trackback(s, p):
            # print(s, p)
            if '*' not in p and len(p) < len(s):
                return False
            if not s:
                if not p or p == '*' * len(p):
                    return True
                else:
                    return False
            if s and not p:
                return False
            if p[0] == '*':
                # if len(p) > 1 and p[1] == '?':
                #     return trackback(s[1:], p[2:])
                if len(p) > 1 and p[1] != '?':
                    temp = 0
                    while s and p[1:]:
                        if p[1] in s:
                            index = s.index(p[1])
                            temp += trackback(s[index + 1:], p[2:])
                            s = s[index + 1:]
                            # p = p[2:]
                        else:
                            break
                    if temp:
                        return True
                    else:
                        return False
                return trackback(s[1:], p) or trackback(s, p[1:])
            elif p[0] == '?':
                return trackback(s[1:], p[1:])
            else:
                if s[0] != p[0]:
                    return False
                else:
                    return trackback(s[1:], p[1:])

        return trackback(s, p)

    def isMatch2(self, s: str, p: str) -> bool:
        ## 动态规划
        sn = len(s)
        pn = len(p)
        dp = [[False] * (pn + 1) for _ in range(sn+1)]
        dp[0][0] = True
        for i in range(pn):
            if p[i] == '*':
                dp[0][i + 1] = dp[0][i]
            else:
                break
        for i in range(1, sn + 1):
            for j in range(1, pn + 1):
                # print(i, j)
                if (s[i - 1] == p[j - 1] or p[j - 1] == '?') and dp[i - 1][j - 1]:
                    dp[i][j] = True
                elif p[j - 1] == '*' and (dp[i - 1][j] or dp[i][j - 1]):
                    dp[i][j] = True
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    s = "abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbbaaabbabbabb"
    p = "***b**a*a*b***b*a*b*bbb**baa*bba**b**bb***b*a*aab*a**"
    # s = "abefcdgiescdfimde"
    # p = "ab*cd?i*de"
    # s = 'hi'
    # p = '*?'
    # print(sol.isMatch(s, p))
    s = "adceb"
    p = "*a*b"
    s = 'aa'
    p = 'a'
    print(sol.isMatch2(s, p))
