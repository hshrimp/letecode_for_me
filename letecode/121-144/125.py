# !/usr/bin/python
# -*-coding:utf-8-*-
# Author: wushaohong

"""125. 验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        if not s[0].isalnum():
            return self.isPalindrome(s[1:])
        if not s[-1].isalnum():
            return self.isPalindrome(s[:-1])
        if s[0].lower() == s[-1].lower():
            return self.isPalindrome(s[1:-1])
        else:
            return False

    def isPalindrome2(self, s: str) -> bool:
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        return s == s[::-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))
