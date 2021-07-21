#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/29 下午6:21
"""
"""345. 反转字符串中的元音字母
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1：

输入："hello"
输出："holle"
示例 2：

输入："leetcode"
输出："leotcede"
 
提示：

元音字母不包含字母 "y" 。
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        yu = set('aeiouAEIOU')
        # s=list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            while s[i] not in yu and i < j:
                i += 1
            while s[j] not in yu and i < j:
                j -= 1
            if i >= j:
                break
            s = s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]
            i += 1
            j -= 1
        return s


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseVowels('leetcode'))
