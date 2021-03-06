#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-01-08 10:08
"""
"""给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int):
        def generator(start, end):
            if start > end:
                return [None]
            res = []
            for i in range(start, end + 1):
                left = generator(start, i - 1)
                right = generator(i + 1, end)
                for l in left:
                    for r in right:
                        c = TreeNode(i)
                        c.left = l
                        c.right = r
                        res.append(c)
            return res

        return generator(1, n)
