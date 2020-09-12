#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/1 下午5:19
"""
"""306. 累加数
累加数是一个字符串，组成它的数字可以形成累加序列。

一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。

给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。

说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。

示例 1:

输入: "112358"
输出: true 
解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
示例 2:

输入: "199100199"
输出: true 
解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
进阶:
你如何处理一个溢出的过大的整数输入?"""


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def check(first, second, last):
            first_len = len(first)
            second_len = len(second)
            if first[0] == '0' and first_len > 1:
                return False
            if second[0] == '0' and second_len > 1:
                return False

            length = max(first_len, second_len)
            if length > len(last):
                return False
            else:
                return True

        def track(first, second, last):
            print(first, second, last)
            if check(first, second, last):
                temp = str(int(first) + int(second))
                if temp == last:
                    res[0] = True
                    return
                len_temp = len(temp)
                if temp == last[:len_temp]:
                    track(second, temp, last[len_temp:])

        num_len = len(num)
        res = [False]
        for i in range(1, num_len - 1):
            for j in range(i + 1, num_len):
                track(num[:i], num[i:j], num[j:])
        return res[0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.isAdditiveNumber("1203"))
