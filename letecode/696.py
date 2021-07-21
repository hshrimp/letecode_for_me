#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/7/21
"""
"""696. 计数二进制子串
给定一个字符串 s，计算具有相同数量 0 和 1 的非空（连续）子字符串的数量，并且这些子字符串中的所有 0 和所有 1 都是连续的。

重复出现的子串要计算它们出现的次数。

示例 1 :

输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

请注意，一些重复出现的子串要计算它们出现的次数。

另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
示例 2 :

输入: "10101"
输出: 4
解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
 

提示：

s.length 在1到50,000之间。
s 只包含“0”或“1”字符。
"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        length = len(s)
        if length < 2:
            return 0
        count = 0
        for i in range(length - 1):
            l, r = i, i + 1
            if s[l] != s[r]:
                lf, rf = s[l], s[r]
                while l >= 0 and r < length:
                    if s[l] == lf and s[r] == rf:
                        print(l, r, s[l:r + 1])
                        count += 1
                    else:
                        break
                    l -= 1
                    r += 1
        return count

    def countBinarySubstrings2(self, s: str) -> int:
        length = len(s)
        if length < 2:
            return 0
        count = 0

        l, r = 0, 1
        lf = s[l]
        rf = s[r]
        while r < length:
            if l >= 0:
                if r - l == 1:
                    if s[l] != s[r]:
                        lf = s[l]
                        rf = s[r]
                    else:
                        l, r = r, r + 1
                        continue
                if s[l] == lf and s[r] == rf:
                    print(l, r, s[l:r + 1])
                    count += 1
                    l -= 1
                    r += 1
                else:
                    l = r - 1
            else:
                l = r - 1
        return count

    def countBinarySubstrings3(self, s: str) -> int:
        res = 0
        count = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] != s[l]:
                res += min(count, r - l)
                count = r - l
                l = r
            r += 1
        return res + min(count, r - l)


if __name__ == '__main__':
    sol = Solution()
    # print(sol.countBinarySubstrings("00110011"))
    print(sol.countBinarySubstrings2("00110011"))
    print(sol.countBinarySubstrings3("00110011"))
