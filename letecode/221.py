#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-12-02 10:27
"""
"""在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        area = 0
        matrix = [[int(t) for t in i] for i in matrix]
        h = len(matrix)
        l = len(matrix[0])
        for i in range(h):
            for j in range(l):
                if matrix[i][j] == 0:
                    continue
                length = min(h - i, l - j)
                if length ** 2 < area:
                    break
                for k in range(1, length + 1):
                    temp = sum([sum(t[j:j + k]) for t in matrix[i:i + k]])
                    if temp != k ** 2:
                        break
                    elif area < temp:
                        area = temp
        return area

    def maximalSquare2(self, matrix):
        h = len(matrix)
        l = len(matrix[0]) if h>0 else 0
        dp = [[0] * (l + 1)] * (h + 1)
        length = 0
        for i in range(1, h):
            for j in range(1, l):
                if matrix[i - 1][j - 1] == '0':
                    continue
                dp[i][j] = min([dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]]) + 1
                length = max(length, dp[i][j])
            print(dp)

        return length ** 2


if __name__ == '__main__':
    sol = Solution()
    m = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(sol.maximalSquare2(m))
