#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/2/17 15:19
"""
"""118杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。"""

class Solution:
    def generate(self, numRows: int):
        res = [[1], [1, 1]]
        for i in range(2, numRows):
            li = []
            for j in range(len(res[i-1]) - 1):
                li.append(res[i-1][j] + res[i-1][j + 1])
            res.append([1]+li + [1])

        return res[:numRows]