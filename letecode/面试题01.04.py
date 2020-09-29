#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/23 下午8:31
"""
"""面试题 01.04. 回文排列
给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。

回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。

回文串不一定是字典当中的单词。

示例1：

输入："tactcoa"
输出：true（排列有"tacocat"、"atcocta"，等等）"""


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        from collections import defaultdict
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        flag = 0
        for k, v in d.items():
            if v > 0 and v % 2 != 0:
                if not flag:
                    flag = 1
                else:
                    return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.canPermutePalindrome('tactcoa'))
