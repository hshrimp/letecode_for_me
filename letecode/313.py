#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/3 下午4:08
"""
"""313. 超级丑数
编写一段程序来查找第 n 个超级丑数。

超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。

示例:

输入: n = 12, primes = [2,7,13,19]
输出: 32 
解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
说明:

1 是任何给定 primes 的超级丑数。
 给定 primes 中的数字以升序排列。
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000 。
第 n 个超级丑数确保在 32 位有符整数范围内。"""


class Solution:
    def nthSuperUglyNumber(self, n: int, primes) -> int:
        res = [1]
        length = len(primes)
        point = [0] * length
        for i in range(1, n):
            temp = [res[point[j]] * primes[j] for j in range(length)]
            print(point, temp)
            print(res)
            while min(temp) == res[-1]:
                index = temp.index(res[-1])
                point[index] += 1
                temp[index] = res[point[index]] * primes[index]
            res.append(min(temp))
            print(res[-1])
            index = temp.index(res[-1])
            point[index] += 1
        return res[-1]

    def nthSuperUglyNumber2(self, n: int, primes) -> int:
        res = [1]
        length = len(primes)
        point = [0] * length
        temp = [res[point[j]] * primes[j] for j in range(length)]
        for i in range(1, n):
            while min(temp) == res[-1]:
                index = temp.index(res[-1])
                point[index] += 1
                temp[index] = res[point[index]] * primes[index]
            res.append(min(temp))
            index = temp.index(res[-1])
            point[index] += 1
            temp[index] = res[point[index]] * primes[index]
        return res[-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.nthSuperUglyNumber(45, [2, 3, 7, 13, 17, 23, 31, 41, 43, 47]))
    print(sol.nthSuperUglyNumber2(45, [2, 3, 7, 13, 17, 23, 31, 41, 43, 47]))
