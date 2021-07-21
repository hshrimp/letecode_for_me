#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/16 下午4:55
"""
"""338. 比特位计数
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例 2:

输入: 5
输出: [0,1,1,2,1,2]
进阶:

给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
"""


class Solution:
    def countBits(self, num: int):
        res = []
        for i in range(num + 1):
            s = bin(i)
            res.append(s.count('1'))
        return res

    def countBits2(self, num: int):
        res = [0] * (num + 1)
        for i in range(num + 1):
            if i % 2 == 0:
                res[i] = res[i // 2]
            else:
                res[i] = res[i - 1] + 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.countBits(5))
    print(sol.countBits2(5))
