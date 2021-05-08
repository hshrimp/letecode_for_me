#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/4/29 下午8:51
"""
"""567. 字符串的排列
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的 子串 。

示例 1：

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
示例 2：

输入: s1= "ab" s2 = "eidboaoo"
输出: False
 

提示：

输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间"""

from itertools import permutations


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for v in permutations(s1):
            if ''.join(v) in s2:
                return True
        return False

    def checkInclusion2(self, s1: str, s2: str) -> bool:
        s1_set = set(s1)
        length = len(s1)
        per = set()
        for v in permutations(s1):
            per.add(''.join(v))
        for i, c in enumerate(s2[:len(s2) - length + 1]):
            if c in s1_set:
                if s2[i:i + length] in per:
                    return True
        return False

    def checkInclusion3(self, s1: str, s2: str) -> bool:
        from collections import Counter
        length1 = len(s1)
        length2 = len(s2)
        target = Counter(s1)
        temp = Counter(s2[:length1])
        if target == temp:
            return True
        for i in range(length1, length2):
            temp[s2[i - length1]] -= 1
            if temp[s2[i - length1]] == 0:
                temp.pop(s2[i - length1])
            temp[s2[i]] += 1
            if target == temp:
                return True
        return False

    def checkInclusion4(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        d = defaultdict(int)
        for c in s1:
            d[c] -= 1
        left, right = 0, 0
        length = len(s1)
        while right < len(s2) and left < len(s2):
            d[s2[right]] += 1
            while d[s2[right]] > 0:
                d[s2[left]] -= 1
                left += 1
            if right - left + 1 == length:
                return True
            right += 1
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.checkInclusion(s1="ab", s2="eidbaooo"))
    print(sol.checkInclusion2(s1="a", s2="da"))
    print(sol.checkInclusion3(s1="ab", s2="eidbaooo"))
    print(sol.checkInclusion4(s1="ab", s2="eidbaooo"))
