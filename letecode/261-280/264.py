#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/8/4 下午4:42
"""
"""264. 丑数 II
编写一个程序，找出第 n 个丑数。

丑数就是质因数只包含 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。"""


class Solution:

    def nthUglyNumber(self, n: int) -> int:
        def isUgly(num: int) -> bool:
            if num < 1:
                return False
            if num == 1:
                return True
            while num % 2 == 0:
                num /= 2
            while num % 3 == 0:
                num /= 3
            while num % 5 == 0:
                num /= 5
            return num == 1

        count = 0
        i = 1
        while count < n:
            if isUgly(i):
                count += 1
                # print(i)
            i += 1
        return i - 1

    def nthUglyNumber2(self, n: int) -> int:
        num = [1]
        p2, p3, p5 = 0, 0, 0
        for i in range(1, n):
            temp = min(num[p2] * 2, num[p3] * 3, num[p5] * 5)
            num.append(temp)
            if temp == num[p2] * 2:
                p2 += 1
            if temp == num[p3] * 3:
                p3 += 1
            if temp == num[p5] * 5:
                p5 += 1
        return num[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.nthUglyNumber(722))
    print(sol.nthUglyNumber2(722))
