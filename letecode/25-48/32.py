#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-09-09 09:52
"""
"""给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        length, mark, left, right, res = len(s), 0, 0, len(s) - 1, 0
        for i in range(length):
            pre_mark = mark
            mark = max(0, mark + (1 if s[i] == '(' else -1))
            if mark == 0:
                if pre_mark > 0:
                    res = max(res, i - left + 1)
                else:
                    left = i + 1
        mark = 0
        for j in range(length - 1, -1, -1):
            pre_mark = mark
            mark = max(0, mark + (1 if s[j] == ')' else -1))
            if mark == 0:
                if pre_mark > 0:
                    res = max(res, right - j + 1)
                else:
                    right = j - 1
        return res

    def longestValidParentheses2(self, s: str) -> int:
        length, mark1, mark2, left, right, res = len(s), 0, 0, 0, len(s) - 1, 0
        for i in range(length):
            pre_mark1 = mark1
            pre_mark2 = mark2
            mark1 = max(0, mark1 + (1 if s[i] == '(' else -1))
            if mark1 == 0:
                if pre_mark1 > 0:
                    res = max(res, i - left + 1)
                else:
                    left = i + 1
            mark2 = max(0, mark2 + (1 if s[length - 1 - i] == ')' else -1))
            if mark2 == 0:
                if pre_mark2 > 0:
                    res = max(res, right - (length - 1 - i) + 1)
                else:
                    right = length - 1 - i - 1
        # mark = 0
        # for j in range(length - 1, -1, -1):
        #     pre_mark = mark
        #     mark = max(0, mark + (1 if s[j] == ')' else -1))
        #     if mark == 0:
        #         if pre_mark > 0:
        #             res = max(res, right - j + 1)
        #         else:
        #             right = j - 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestValidParentheses(")()()"))
    print(sol.longestValidParentheses2(")()())"))
