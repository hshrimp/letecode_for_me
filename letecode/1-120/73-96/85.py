#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-11-29 10:02
"""
"""给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-rectangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        a, b, c, d = 0, 0, len(matrix), len(matrix[0])
        res = [0]

        def track_back(i, j, k, l):
            if i < k and j < l and (k - i) * (l - j) > max(res):
                print(i, j, k, l)
                for p in range(k - i):
                    if '0' in matrix[i + p][j:l]:
                        break
                else:
                    res[0] = (k - i) * (l - j)
                    return

                track_back(i + 1, j, k, l)
                track_back(i, j + 1, k, l)
                track_back(i, j, k - 1, l)
                track_back(i, j, k, l - 1)

        track_back(a, b, c, d)
        return res[0]

    def maximalRectangle2(self, matrix) -> int:
        if not matrix: return 0

        m = len(matrix)
        n = len(matrix[0])

        left = [0] * n  # initialize left as the leftmost boundary possible
        right = [n] * n  # initialize right as the rightmost boundary possible
        height = [0] * n

        maxarea = 0

        for i in range(m):

            cur_left, cur_right = 0, n
            # update height
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            # update left
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            # update right
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            # update the area
            for j in range(n):
                maxarea = max(maxarea, height[j] * (right[j] - left[j]))

        return maxarea


if __name__ == '__main__':
    sol = Solution()
    m = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(sol.maximalRectangle2(m))
