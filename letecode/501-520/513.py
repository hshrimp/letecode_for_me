#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/3/6 下午2:42
"""
"""513. 找树左下角的值
给定一个二叉树，在树的最后一行找到最左边的值。

示例 1:

输入:

    2
   / \
  1   3

输出:
1
 
示例 2:

输入:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

输出:
7

注意: 您可以假设树（即给定的根节点）不为 NULL。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        res = [root.val, 0]

        def find(r, level):
            if not r:
                return
            if not r.left and not r.right and level > res[1]:
                res[0] = r.val
                res[1] = level
            find(r.left, level + 1)
            find(r.right, level + 1)

        find(root, 0)
        return res[0]
