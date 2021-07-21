#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/3/8 下午4:35
"""
"""483. 最小好进制
对于给定的整数 n, 如果n的k（k>=2）进制数的所有数位全为1，则称 k（k>=2）是 n 的一个好进制。

以字符串的形式给出 n, 以字符串的形式返回 n 的最小好进制。

示例 1：

输入："13"
输出："3"
解释：13 的 3 进制是 111。
示例 2：

输入："4681"
输出："8"
解释：4681 的 8 进制是 11111。
示例 3：

输入："1000000000000000000"
输出："999999999999999999"
解释：1000000000000000000 的 999999999999999999 进制是 11。
 
提示：

n的取值范围是 [3, 10^18]。
输入总是有效且没有前导 0。"""


class Solution:
    def smallestGoodBase(self, n: str) -> str:
        import math
        num = int(n)
        for x in range(2, num):
            k = math.log(num * (x - 1) + 1, x)
            if int(k) == k:
                return str(x)

    def smallestGoodBase2(self, n: str) -> str:
        num = int(n)
        for k in range(len(bin(num)) - 2, 0, -1):
            left = 2
            right = num - 1
            while left <= right:
                # print(left, right)
                mid = (right + left) // 2
                val = (mid ** k - 1) // (mid - 1)
                if val > num:
                    right = mid - 1
                elif val < num:
                    left = mid + 1
                if val == num:
                    return str(mid)


if __name__ == '__main__':
    sol = Solution()
    # print(sol.smallestGoodBase2('1000000000000000000'))
    print(sol.smallestGoodBase2('1000000000000000000'))
