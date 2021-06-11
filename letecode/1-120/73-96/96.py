#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-01-07 11:15
"""
"""给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    d = {0: 1, 1: 1, 2: 2}

    def numTrees(self, n: int) -> int:
        if n in self.d:
            return self.d[n]
        res = 0
        for i in range(1, n + 1):
            if i - 1 in self.d:
                left = self.d[i - 1]
            else:
                left = self.numTrees(i - 1)
                self.d[i - 1] = left
            if n - i in self.d:
                right = self.d[n - i]
            else:
                right = self.numTrees(n - i)
                self.d[n - i] = right
            res += left * right
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.numTrees(5))
