#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/10/13 下午5:01
"""
"""383. 赎金信
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。
如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。)

注意：

你可以假设两个字符串均只含有小写字母。

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true"""

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)
        for k, v in r.items():
            if k not in m:
                return False
            if v > m[k]:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.canConstruct("aac", "aab"))
