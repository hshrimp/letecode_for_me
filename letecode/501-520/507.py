#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/3/6 上午10:56
"""
"""507. 完美数
对于一个 正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。

给定一个 整数 n， 如果是完美数，返回 true，否则返回 false

示例 1：

输入：28
输出：True
解释：28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, 和 14 是 28 的所有正因子。
示例 2：

输入：num = 6
输出：true
示例 3：

输入：num = 496
输出：true
示例 4：

输入：num = 8128
输出：true
示例 5：

输入：num = 2
输出：false
 
提示：

1 <= num <= 108"""


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        count = 0
        for i in range(1, num // 2 + 1):
            if num % i == 0:
                count += i
        return count == num

    def checkPerfectNumber2(self, num: int) -> bool:
        if num == 1:
            return False
        count = 0
        s = set()
        for i in range(int(num ** 0.5) + 1, 1, -1):
            if i in s:
                continue
            if num % i == 0:
                count += i
                cur = num / i
                count += cur
                s.update({i, cur})
            if count + 1 > num:
                return False
        return count + 1 == num


if __name__ == '__main__':
    sol = Solution()
    print(sol.checkPerfectNumber(2096128))
    print(sol.checkPerfectNumber2(28))
