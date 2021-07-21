#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/3/12 15:38
"""
"""1071. 字符串的最大公因子
对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。

返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。

示例 1：

输入：str1 = "ABCABC", str2 = "ABC"
输出："ABC"
示例 2：

输入：str1 = "ABABAB", str2 = "ABAB"
输出："AB"
示例 3：

输入：str1 = "LEET", str2 = "CODE"
输出：""
 
提示：

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] 和 str2[i] 为大写英文字母"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        length = min(len1, len2)
        while length:
            print(length)
            p1, q1 = divmod(len1, length)
            p2, q2 = divmod(len2, length)
            if not q1 and not q2:
                ans = str1[:length]
                if str1 == ans * p1 and str2 == ans * p2:
                    return ans
                length -= 1
            while length and (len1 % length or len2 % length):
                print(length, len1 % length, len2 % length)
                length -= 1
        return ""


if __name__ == '__main__':
    sol = Solution()
    print(sol.gcdOfStrings(str1="LEET", str2="CODE"))
