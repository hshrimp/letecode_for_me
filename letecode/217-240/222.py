#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/30 下午8:37
"""
"""222. 完全二叉树的节点个数
给出一个完全二叉树，求出该树的节点个数。

说明：

完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，
并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

示例:

输入: 
    1
   / \
  2   3
 / \  /
4  5 6

输出: 6"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def find(r):
            if not r:
                nonlocal count
                count += 1
                find(r.left)
                find(r.right)

        count = 0
        find(root)
        return count

    def countNodes2(self, root):
        def helper(_root):

            if _root is None:
                return 0

            return helper(_root.left) + 1

        left_depth = helper(root.left)
        right_depth = helper(root.right)

        if left_depth == right_depth:
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            return (1 << right_depth) + self.countNodes(root.left)
