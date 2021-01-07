#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/1/6 下午2:40
"""
"""454. 四数相加 II
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

例如:

输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0"""


class Solution:
    def fourSumCount(self, A, B, C, D) -> int:
        res = 0
        if not A:
            return 0
        from collections import defaultdict
        ab = defaultdict(int)
        for a in A:
            for b in B:
                ab[a + b] += 1
        cd = defaultdict(int)
        for c in C:
            for d in D:
                cd[-(c + d)] += 1
        for k, v in ab.items():
            if k in cd:
                res += v * cd[k]
        return res

    def fourSumCount2(self, A, B, C, D) -> int:
        res = 0
        if not A:
            return 0
        from collections import defaultdict
        ab = defaultdict(int)
        for a in A:
            for b in B:
                ab[a + b] += 1
        for c in C:
            for d in D:
                if -(c + d) in ab:
                    res += ab[-(c + d)]
        return res


if __name__ == '__main__':
    sol = Solution()
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(sol.fourSumCount(A, B, C, D))
