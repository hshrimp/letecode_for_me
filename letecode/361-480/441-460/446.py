#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/1/4 下午3:18
"""
"""446. 等差数列划分 II - 子序列
如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，以下数列为等差数列:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
以下数列不是等差数列。

1, 1, 2, 5, 7
 
数组 A 包含 N 个数，且索引从 0 开始。该数组子序列将划分为整数序列 (P0, P1, ..., Pk)，满足 0 ≤ P0 < P1 < ... < Pk < N。

如果序列 A[P0]，A[P1]，...，A[Pk-1]，A[Pk] 是等差的，那么数组 A 的子序列 (P0，P1，…，PK) 称为等差序列。值得注意的是，这意味着 k ≥ 2。

函数要返回数组 A 中所有等差子序列的个数。

输入包含 N 个整数。每个整数都在 -231 和 231-1 之间，另外 0 ≤ N ≤ 1000。保证输出小于 231-1。

示例：

输入：[2, 4, 6, 8, 10]

输出：7

解释：
所有的等差子序列为：
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]"""


class Solution:
    def numberOfArithmeticSlices(self, A) -> int:
        """
        dp[i][diff]表示以第i个数结束的，等差为diff的弱等差数列以上的数量，弱等差数列是指数列长度为2的等差数列，所以这边是指长度大于等于2的数量
        :param A:
        :return:
        """
        from collections import defaultdict
        dp = [defaultdict(int) for _ in range(len(A))]
        res = 0
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                # 后面这个1表示[A[j],A[i]]组成的弱等差数列
                dp[i][diff] += dp[j][diff] + 1
                # 说明满足长度大于等于3
                if diff in dp[j]:
                    # dp[j][diff]表示以第j个结束的差值为diff的弱等差序列以上的个数，因为可以跟第i个配合成长度大于等于3的等差数列，所以加上
                    res += dp[j][diff]
                print(dp)
        return res


if __name__ == '__main__':
    sol = Solution()
    # print(sol.numberOfArithmeticSlices([0, 1, 2, 2, 2]))
    print(sol.numberOfArithmeticSlices([1, 1, 1, 1, 1, 1]))
    print(sol.numberOfArithmeticSlices([0, 1, 2, 2, 2]))
