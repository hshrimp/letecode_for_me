#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/27 下午2:07
"""
"""363. 矩形区域不超过 K 的最大数值和
给定一个非空二维矩阵 matrix 和一个整数 k，找到这个矩阵内部不大于 k 的最大矩形和。

示例:

输入: matrix = [[1,0,1],[0,-2,3]], k = 2
输出: 2 
解释: 矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
说明：

矩阵内的矩形区域面积必须大于 0。
如果行数远大于列数，你将如何解答呢？"""

import bisect


class Solution:
    def maxSumSubmatrix(self, matrix, k: int) -> int:
        row, col = len(matrix), len(matrix[0])
        res = float('-inf')
        for left in range(col):
            sums = [0] * row
            for right in range(left, col):
                for j in range(row):
                    sums[j] += matrix[j][right]
                print(sums)
                lst = [0]
                cur = 0
                """
                我们这里需要找到的是最大的矩形和，但是有一个条件，那就是不大于k。
                比如我们要求sums(i,j)=sums(0,j)-sums(0,i-1)那么我们可以把sums(i,j)=k且不大于k，
                sums(0,j)-sums(0,i-1)<=k,可以写成sums(0,j)-k<=sums(0,i-1)，我们可以看这个式子是否成立。
                所以当我们累加和第一个值之后loc = bisect.bisect_left(lst,cur-k)可以看成sums(0,j)-k<=sums(0,i-1),
                接下来进行一个if判断，如果成立那么cur-lst[loc]可以看成sums(0,j)-sums(0,i-1)<=k计算出值,之后进行res最大值计算。
                """
                for num in sums:
                    cur += num
                    index = bisect.bisect_left(lst, cur - k)
                    if index < len(lst):
                        res = max(cur - lst[index], res)
                    bisect.insort(lst, cur)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSumSubmatrix(matrix=[[1, 0, 1], [0, -2, 3]], k=2))
