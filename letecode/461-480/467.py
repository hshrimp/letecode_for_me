#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/1/13 上午10:23
"""
"""467. 环绕字符串中唯一的子字符串
把字符串 s 看作是“abcdefghijklmnopqrstuvwxyz”的无限环绕字符串，
所以 s 看起来是这样的："...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....". 

现在我们有了另一个字符串 p 。你需要的是找出 s 中有多少个唯一的 p 的非空子串，
尤其是当你的输入是字符串 p ，你需要输出字符串 s 中 p 的不同的非空子串的数目。 

注意: p 仅由小写的英文字母组成，p 的大小可能超过 10000。

示例 1:

输入: "a"
输出: 1
解释: 字符串 S 中只有一个"a"子字符。
 
示例 2:

输入: "cac"
输出: 2
解释: 字符串 S 中的字符串“cac”只有两个子串“a”、“c”。.
 
示例 3:

输入: "zab"
输出: 6
解释: 在字符串 S 中有六个子串“z”、“a”、“b”、“za”、“ab”、“zab”。."""


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if not p:
            return 0
        d = {c: i for c, i in zip('abcdefghijklmnopqrstuvwxyz', range(1, 27))}
        res = set()
        from functools import lru_cache
        @lru_cache(None)
        def find(_p):
            # print(_p)
            if len(_p) == 1:
                res.add(_p)
                return d[_p]
            if _p[:-1] not in res:
                left = find(_p[:-1])
            else:
                left = d[_p[-2]]
            if _p[1:] not in res:
                find(_p[1:])

            if left:
                # (left+1-1)%26+1 => left%26+1
                if d[_p[-1]] == left % 26 + 1:
                    res.add(_p)
                    return d[_p[-1]]
            return False

        find(p)
        return len(res)

    def findSubstringInWraproundString2(self, p: str) -> int:
        from collections import defaultdict
        dp = defaultdict(int)
        max_l = 1
        dp[p[0]] = 1
        for i in range(1, len(p)):
            if (ord(p[i]) - ord(p[i - 1])) % 26 == 1:
                max_l += 1
            else:
                max_l = 1
            dp[p[i]] = max(dp[p[i]], max_l)
        return sum(dp.values())


if __name__ == '__main__':
    sol = Solution()
    print(sol.findSubstringInWraproundString('zab'))
    print(sol.findSubstringInWraproundString2('zab'))
