#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/1/3 下午2:01
"""
"""440. 字典序的第K小数字
给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。

注意：1 ≤ k ≤ n ≤ 109。

示例 :

输入:
n: 13   k: 2

输出:
10

解释:
字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。"""


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        target = {str(i) for i in range(1, n + 1)}
        target = sorted(target)
        return target[k - 1]

    def findKthNumber2(self, n: int, k: int) -> int:
        def find(count):
            step = 0
            count2 = count + 1
            while count <= n:
                step += min(count2, n + 1) - count
                count *= 10
                count2 *= 10
            return step

        cur = 1
        k -= 1
        while k > 0:
            steps = find(cur)
            if steps <= k:
                cur += 1
                k -= steps
            elif steps > k:
                cur *= 10
                k -= 1
        return cur


if __name__ == '__main__':
    sol = Solution()
    print(sol.findKthNumber(n=13, k=2))
    print(sol.findKthNumber2(n=13, k=2))
