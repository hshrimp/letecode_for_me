#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-08-26 17:58
"""
"""
给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:

输入: 27
输出: true
示例 2:

输入: 0
输出: false
示例 3:

输入: 9
输出: true
示例 4:

输入: 45
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-three
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return 0 < n == 3 ** round(math.log(n, 3))


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPowerOfThree(81))
