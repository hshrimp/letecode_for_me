#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-11-13 10:06
"""
"""给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""
from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        def check(temp):
            for i in count_t:
                if i not in temp:
                    return False
                else:
                    num = temp.count(i)
                    if num < count_t[i]:
                        return False
            return True

        start = len(t)
        length = len(s)
        count_t = {}
        for i in t:
            if i not in count_t:
                count_t[i] = 1
            else:
                count_t[i] += 1
        while start <= length:
            for i in range(length - start + 1):
                if i != 0 and s[i + start - 1] not in count_t:
                    continue
                temp = s[i:i + start]
                if i != 0 and temp.count(s[i + start - 1]) != count_t[s[i + start - 1]]:
                    continue
                # print(temp)
                if check(temp):
                    return temp
            start += 1
        return ''

    def minWindow2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        start = len(t)
        length = len(s)
        count_t = Counter(t)
        while start <= length:
            for i in range(length - start + 1):
                temp = s[i:i + start]
                if not (count_t - Counter(temp)):
                    return temp
            start += 1
        return ''


if __name__ == '__main__':
    sol = Solution()
    S = "aaaaaaaaaaaabbbbbcdd"
    T = "abcdd"
    print(sol.minWindow(S, T))
