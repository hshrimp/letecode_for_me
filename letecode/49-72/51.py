#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-10-08 10:21
"""
"""n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def help(self, ans, i):
        if not ans:
            return True
        length = len(ans)
        n = len(ans[0])
        for li in ans:
            if li[i] is 'Q':
                return False
        p, q = i, i
        while length > 0:
            p -= 1
            q += 1
            if p >= 0:
                if ans[length - 1][p] == 'Q':
                    return False
            if q < n:
                if ans[length - 1][q] == 'Q':
                    return False
            length -= 1
        return True

    def solveNQueens(self, n: int):
        res = []

        def trackback(ans):
            if ans and len(ans) == n:
                res.append(ans)
                return
            li = '.' * n
            for i in range(n):
                temp = list(ans)
                li2 = li[0:i] + 'Q' + li[i + 1:]
                if self.help(temp, i):
                    temp.append(li2)
                    trackback(temp)

        trackback([])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.solveNQueens(4))
