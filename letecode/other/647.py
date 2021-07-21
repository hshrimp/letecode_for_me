#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-12-10 11:14
"""
"""给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
注意:

输入的字符串长度不会超过1000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindromic-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        if not l:
            return 0
        temp = set((i, i + 1) for i, c in enumerate(s))
        res = l
        while temp:
            t = set()
            for i, j in temp:
                if i > 0 and s[i - 1] * (j - i) == s[i:j]:
                    t.add((i - 1, j))
                elif j < l and s[j] * (j - i) == s[i:j]:
                    t.add((i, j + 1))
                else:
                    if i > 0 and j < l and s[i - 1] == s[j]:
                        t.add((i - 1, j + 1))
            res += len(t)
            temp = t
        print(res)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.countSubstrings("xxx"))
