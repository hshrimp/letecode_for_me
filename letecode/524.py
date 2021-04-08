#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/3/31 下午3:43
"""
"""524. 通过删除字母匹配到字典里最长单词
给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。
如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。

示例 1:

输入:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

输出: 
"apple"
示例 2:

输入:
s = "abpcplea", d = ["a","b","c"]

输出: 
"a"
说明:

所有输入的字符串只包含小写字母。
字典的大小不会超过 1000。
所有输入的字符串长度不会超过 1000。"""


class Solution:
    def findLongestWord(self, s: str, dictionary) -> str:
        def contains(string, target):
            i, j = 0, 0
            length = len(string)
            target_l = len(target)
            while j < target_l:
                while i < length and string[i] != target[j]:
                    i += 1
                if i >= length:
                    return False
                i += 1
                j += 1
            return True

        from collections import defaultdict
        d = defaultdict(list)
        for cur in dictionary:
            d[len(cur)].append(cur)
        d = sorted(d.items(), key=lambda x: x[0], reverse=True)
        length = len(s)
        for l, li in d:
            if l <= length:
                li.sort()
                for cur in li:
                    if contains(s, cur):
                        return cur
        return ''


if __name__ == '__main__':
    sol = Solution()
    print(sol.findLongestWord(s="abpcplea", dictionary=["b", 'a', "c"]))
