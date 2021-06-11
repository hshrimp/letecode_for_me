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

    def minWindow3(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""
        length = len(s)
        res = ' ' * length
        t_len = len(t)
        left, right = 0, t_len
        t_count = Counter(t)
        while left <= length - t_len:
            while right <= length and t_count - Counter(s[left:right]):
                # print(left, right)
                right += 1
            else:
                while right - left - 1 >= t_len and not t_count - Counter(s[left + 1:right]):
                    left += 1
                    # print(left, right, s[left:right])
                if right - left <= len(res) and not t_count - Counter(s[left:right]):
                    res = s[left:right]
                left += 1
        return res if res != ' ' * length else ''


if __name__ == '__main__':
    sol = Solution()
    S = "A"
    T = "A"
    print(sol.minWindow3(S, T))
