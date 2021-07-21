#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/7/15 下午2:41
"""
"""633. 平方数之和
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a^2 + b^2 = c 。

 
示例 1：

输入：c = 5
输出：true
解释：1 * 1 + 2 * 2 = 5
示例 2：

输入：c = 3
输出：false
示例 3：

输入：c = 4
输出：true
示例 4：

输入：c = 2
输出：true
示例 5：

输入：c = 1
输出：true
 

提示：

0 <= c <= 2^31 - 1
"""


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        import math
        for i in range(int(math.sqrt(c)), -1, -1):
            last = c - i ** 2
            squt_last = math.sqrt(last)
            if int(squt_last) == squt_last:
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.judgeSquareSum(6))
