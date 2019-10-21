#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-10-21 10:37
"""
"""给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        l, r, b, t = 0, n - 1, n - 1, 0
        res = [[0] * n for _ in range(n)]
        i, nums = 1, n ** 2
        while i <= nums:
            for j in range(l, r + 1):
                res[t][j] = i
                i += 1
            t += 1
            for j in range(t, b + 1):
                res[j][r] = i
                i += 1
            r -= 1
            for j in range(r, l - 1, -1):
                res[b][j] = i
                i += 1
            b -= 1
            for j in range(b, t - 1, -1):
                res[j][l] = i
                i += 1
            l += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.generateMatrix(1))
