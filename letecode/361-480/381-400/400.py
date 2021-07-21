#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/11/20 下午2:19
"""
"""400. 第N个数字
在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。

注意:
n 是正数且在32位整数范围内 ( n < 231)。

示例 1:

输入:
3

输出:
3
示例 2:

输入:
11

输出:
0

说明:
第11个数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是0，它是10的一部分。"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        s = ''.join([str(i) for i in range(1, n + 1)])
        return int(s[n - 1])

    def findNthDigit2(self, n: int) -> int:
        def deep(last_num, bit):
            count = bit * int('9' + (bit - 1) * '0')
            # print(count)
            if last_num >= count:
                return deep(last_num - count, bit + 1)
            else:
                num, last = divmod(last_num, bit)
                if last:
                    cur = 10 ** (bit - 1) + num
                    return int(str(cur)[last - 1])
                else:
                    cur = 10 ** (bit - 1) + num - 1
                    return cur % 10

        return deep(n, 1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findNthDigit(2511))
    print(sol.findNthDigit2(2511))
