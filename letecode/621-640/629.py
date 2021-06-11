#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/5/27 下午5:09
"""
"""629. K个逆序对数组
给出两个整数 n 和 k，找出所有包含从 1 到 n 的数字，且恰好拥有 k 个逆序对的不同的数组的个数。

逆序对的定义如下：对于数组的第i个和第 j个元素，如果满i < j且 a[i] > a[j]，则其为一个逆序对；否则不是。

由于答案可能很大，只需要返回 答案 mod 109 + 7 的值。

示例 1:

输入: n = 3, k = 0
输出: 1
解释: 
只有数组 [1,2,3] 包含了从1到3的整数并且正好拥有 0 个逆序对。
示例 2:

输入: n = 3, k = 1
输出: 2
解释: 
数组 [1,3,2] 和 [2,1,3] 都有 1 个逆序对。
说明:

 n 的范围是 [1, 1000] 并且 k 的范围是 [0, 1000]。"""


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        from itertools import permutations
        import bisect
        nums = [i for i in range(1, n + 1)]
        li = permutations(nums)
        res = 0
        for cur in li:
            seq = []
            cur_count = 0
            for i, num in enumerate(cur):
                index = bisect.bisect_right(seq, num)
                cur_count += len(seq) - index
                if cur_count > k:
                    break
                seq.insert(index, num)
            if cur_count == k:
                res += 1
        return res % (10 ** 9 + 7)

    def kInversePairs2(self, n: int, k: int) -> int:
        if k == 0:
            return 1
        d = {key: 0 for key in range(k + 1)}
        d[0] = 1
        # 序列的长度从1到z增加
        for i in range(2, n + 1):
            # print(d)
            temp = dict(d)
            # 新增加的这个最大的数字所能产生的逆序对数量
            for j in range(1, i):
                # print(j, d)
                # 对于之前序列所能产生的逆序对的影响
                for key in range(k - 1, -1, -1):
                    if key + j <= k:
                        temp[key + j] += d[key]
            d = temp
            d[k] = d[k] % (10 ** 9 + 7)
        return d[k]

    def kInversePairs3(self, n: int, k: int) -> int:
        if k == 0:
            return 1
        d = {0: 1}
        # 序列的长度从1到z增加
        for i in range(2, n + 1):
            # print(d)
            temp = dict(d)
            # 新增加的这个最大的数字所能产生的逆序对数量
            for j in range(1, i):
                # print(j, d)
                # 对于之前序列所能产生的逆序对的影响
                for key in range(len(d) - 1, -1, -1):
                    if key + j <= k:
                        if key + j not in temp:
                            temp[key + j] = 0
                        temp[key + j] += d[key]
                        temp[key + j] %= 10 ** 9 + 7
            d = temp
            # d[k] = d[k] % (10 ** 9 + 7)
        return d[k] if k in d else 0

    def kInversePairs4(self, n: int, k: int) -> int:
        if k == 0:
            return 1
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        for i in range(n + 1):
            dp[0][i] = 1
        for i in range(1, k + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                if i >= j:
                    dp[i][j] -= dp[i - j][j - 1]
        print(dp)
        return dp[-1][-1] % (10 ** 9 + 7)


if __name__ == '__main__':
    sol = Solution()
    n = 1000
    k = 30
    # print(sol.kInversePairs(n, k))
    print(sol.kInversePairs2(n, k))
    print(sol.kInversePairs3(n, k))
    print(sol.kInversePairs4(n, k))
