#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-05-27 10:34
"""
"""974. 和可被 K 整除的子数组
给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。

示例：

输入：A = [4,5,0,-2,-3,1], K = 5
输出：7
解释：
有 7 个子数组满足其元素之和可被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 
提示：

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000"""


class Solution:
    def subarraysDivByK(self, A, K: int) -> int:
        res = 0
        length = len(A)
        for i in range(length):
            dp = 0
            for j in range(i, length):
                dp += A[j]
                if dp % K == 0:
                    res += 1
        return res

    def subarraysDivByK2(self, A, K: int) -> int:
        """
        sum(i,j) = sum(j)-sum(i-1)
        sum(i,j)%K=0 --> (sum(j)-sum(i-1))%K=0 --> sum(j)%K = sum(i-1)%K
        :param A:
        :param K:
        :return:
        """
        res = 0
        length = len(A)
        d = {0: 1}
        total = 0
        for i in range(length):
            total += A[i]
            last = total % K
            num = d.get(last, 0)
            res += num
            d[last] = num + 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.subarraysDivByK2(A=[4, 5, 0, -2, -3, 1], K=5))
