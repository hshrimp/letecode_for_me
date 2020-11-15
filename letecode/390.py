#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/10/17 下午2:18
"""
"""390. 消除游戏
给定一个从1 到 n 排序的整数列表。
首先，从左到右，从第一个数字开始，每隔一个数字进行删除，直到列表的末尾。
第二步，在剩下的数字中，从右到左，从倒数第一个数字开始，每隔一个数字进行删除，直到列表开头。
我们不断重复这两步，从左到右和从右到左交替进行，直到只剩下一个数字。
返回长度为 n 的列表中，最后剩下的数字。

示例：

输入:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

输出:
6"""


class Solution:
    def lastRemaining(self, n: int) -> int:
        li = [i for i in range(1, n + 1)]
        dir = 0
        while len(li) > 1:
            if dir == 0:
                li = li[1::2]
                dir = 1
            else:
                li = li[::-1][1::2][::-1]
                dir = 0
        return li[0]

    def lastRemaining2(self, n: int) -> int:
        if n < 2:
            return 1
        return 2 * (n // 2 + 1 - self.lastRemaining2(n // 2))


if __name__ == '__main__':
    sol = Solution()
    print(sol.lastRemaining(16))
    print(sol.lastRemaining2(16))
