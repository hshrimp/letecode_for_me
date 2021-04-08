#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/3/6 下午2:52
"""
"""519. 随机翻转矩阵
题中给出一个 n_rows 行 n_cols 列的二维矩阵，且所有值被初始化为 0。要求编写一个 flip 函数，均匀随机的将矩阵中的 0 变为 1，
并返回该值的位置下标 [row_id,col_id]；同样编写一个 reset 函数，将所有的值都重新置为 0。
尽量最少调用随机函数 Math.random()，并且优化时间和空间复杂度。

注意:

1 <= n_rows, n_cols <= 10000
0 <= row.id < n_rows 并且 0 <= col.id < n_cols
当矩阵中没有值为 0 时，不可以调用 flip 函数
调用 flip 和 reset 函数的次数加起来不会超过 1000 次
示例 1：

输入: 
["Solution","flip","flip","flip","flip"]
[[2,3],[],[],[],[]]
输出: [null,[0,1],[1,2],[1,0],[1,1]]
示例 2：

输入: 
["Solution","flip","flip","reset","flip"]
[[1,2],[],[],[],[]]
输出: [null,[0,0],[0,1],null,[0,0]]
输入语法解释：

输入包含两个列表：被调用的子程序和他们的参数。Solution 的构造函数有两个参数，分别为 n_rows 和 n_cols。
flip 和 reset 没有参数，参数总会以列表形式给出，哪怕该列表为空"""

import random


class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.matrix = {(i, j) for i in range(n_rows) for j in range(n_cols)}
        self.zero = list(self.matrix)

    def flip(self):
        res = random.choice(self.zero)
        self.zero.remove(res)
        return res

    def reset(self) -> None:
        self.zero = list(self.matrix)


class Solution2:

    def __init__(self, n_rows: int, n_cols: int):
        self.row = n_rows
        self.col = n_cols
        self.one = set()

    def flip(self):
        x = random.randint(0, self.row - 1)
        y = random.randint(0, self.col - 1)
        while (x, y) in self.one:
            x = random.randint(0, self.row - 1)
            y = random.randint(0, self.col - 1)
        self.one.add((x, y))
        return [x, y]

    def reset(self) -> None:
        self.one = set()


class Solution3:

    def __init__(self, n_rows: int, n_cols: int):
        self.row = n_rows
        self.col = n_cols
        self.n = n_rows * n_cols - 1
        self.matrix = [i for i in range(self.n)]
        self.zero = list(self.matrix)
        random.shuffle(self.zero)

    def flip(self):
        index = self.zero.pop()
        return [index // self.row, index % self.col]

    def reset(self) -> None:
        self.zero = list(self.matrix)
        random.shuffle(self.zero)


class Solution4:

    def __init__(self, n_rows: int, n_cols: int):
        self.col = n_cols
        self.n = n_rows * n_cols - 1
        self.one = set()

    def flip(self):
        index = random.randint(0, self.n)
        while index in self.one:
            index = random.randint(0, self.n)
        self.one.add(index)
        return [index // self.col, index % self.col]

    def reset(self) -> None:
        self.one.clear()
# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
