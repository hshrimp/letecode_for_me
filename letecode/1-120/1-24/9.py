#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-12-16 10:06
"""
"""判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False

    def isPalindrome2(self, x):
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        last = x
        half = 0
        while last > half:
            last, temp_half = divmod(last, 10)
            if last == half:
                return True
            half = half * 10 + temp_half
        if last == half:
            return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome(1221))
    print(sol.isPalindrome2(1221))
