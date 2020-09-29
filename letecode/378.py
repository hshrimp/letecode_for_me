#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/28 下午8:19
"""
"""378. 有序矩阵中第K小的元素
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

示例：

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。

提示：
你可以假设 k 的值永远是有效的，1 ≤ k ≤ n2 。"""

import bisect

import heapq


class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        n = len(matrix)
        hp = [[matrix[i][0], i, 0] for i in range(n)]
        heapq.heapify(hp)
        for j in range(k - 1):
            num, i, col = heapq.heappop(hp)
            if col < n - 1:
                heapq.heappush(hp, [matrix[i][col + 1], i, col + 1])
        return heapq.heappop(hp)[0]

    def kthSmallest2(self, matrix, k: int) -> int:
        def check(mid):
            num = 0
            i, j = n - 1, 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (right + left) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    sol = Solution()
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 14, 15]
    ]
    k = 8
    # matrix = [[1, 3, 5], [6, 7, 12], [11, 14, 14]]
    # k = 6
    # matrix = [[-5]]
    # k = 1
    print(sol.kthSmallest(matrix, k))
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 14, 15]
    ]
    k = 8
    print(sol.kthSmallest2(matrix, k))
