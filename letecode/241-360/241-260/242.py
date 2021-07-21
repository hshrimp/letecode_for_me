#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/8/4 下午3:03
"""
"""242. 有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for i in s:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        for i in t:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1
        for k, v in d1.items():
            if k not in d2:
                return False
            else:
                if v != d2[k]:
                    return False
                else:
                    d2.pop(k)
        return d2 == {}


if __name__ == '__main__':
    sol = Solution()
    print(sol.isAnagram(s="rat", t="car"))
