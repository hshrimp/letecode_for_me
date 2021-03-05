#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/3/3 下午8:02
"""
"""479. 最大回文数乘积
你需要找到由两个 n 位数的乘积组成的最大回文数。

由于结果会很大，你只需返回最大回文数 mod 1337得到的结果。

示例:

输入: 2

输出: 987

解释: 99 x 91 = 9009, 9009 % 1337 = 987

说明:

n 的取值范围为 [1,8]。"""


class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        max_num = 10 ** n - 1
        min_num = 10 ** (n - 1)
        for num in range(max_num, min_num, -1):
            num = str(num)
            target = int(num + num[::-1])
            cur = max_num
            while cur ** 2 > target:
                if target % cur == 0:
                    # print(target)
                    return target % 1337
                cur -= 1

    def largestPalindrome2(self, n: int) -> int:
        if n == 1:
            return 9
        a = 2
        while a < 10 ** n:
            upper = 10 ** n - a
            lower = int(str(upper)[::-1])
            if a ** 2 - 4 * lower > 0 and (a ** 2 - 4 * lower) ** 0.5 == int((a ** 2 - 4 * lower) ** 0.5):
                return (upper * 10 ** n + lower) % 1337
            a += 1


if __name__ == '__main__':
    sol = Solution()
    for i in range(7, 0, -1):
        print(sol.largestPalindrome(i))
        print(sol.largestPalindrome2(i))
