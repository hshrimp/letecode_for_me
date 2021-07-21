#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/12/7 下午5:50
"""
"""413. 等差数列划分
如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，以下数列为等差数列:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
以下数列不是等差数列。

1, 1, 2, 5, 7
 
数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。

如果满足以下条件，则称子数组(P, Q)为等差数组：

元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。

函数要返回数组 A 中所有为等差数组的子数组个数。

示例:

A = [1, 2, 3, 4]

返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。"""


class Solution:
    def numberOfArithmeticSlices(self, A) -> int:
        def check(p, q):
            if q - p < 2:
                return 0
            if q - p == 2:
                if A[q] - A[q - 1] == A[q - 1] - A[p]:
                    visited[(p, q)] = A[q - 1] - A[p]
                    return 1
                else:
                    return 0
            else:
                if (p, q - 1) in visited and (p + 1, q) in visited and visited[(p, q - 1)] == visited[(p + 1, q)]:
                    visited[(p, q)] = visited[(p + 1, q)]
                    return 1
                else:
                    return 0

        visited = {}
        res = 0
        length = len(A)
        for l in range(2, length):
            for i in range(length - l):
                res += check(i, i + l)
        return res

    def numberOfArithmeticSlices2(self, A) -> int:
        length = len(A)
        if length < 3:
            return 0
        res = 0
        count = 0
        gap = A[1] - A[0]
        left = 0
        for i in range(2, length):
            if A[i] - A[i - 1] == gap:
                count += i - left - 1
            else:
                res += count
                count = 0
                gap = A[i] - A[i - 1]
                left = i - 1
        res += count
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfArithmeticSlices([1, 2, 3, 4, 6, 8, 9, 10]))
    print(sol.numberOfArithmeticSlices2([1, 2, 3, 4, 6, 8, 9, 10]))
