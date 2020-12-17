#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/11/26 上午11:07
"""
"""404. 左叶子之和
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def func(r, left):
            if r.left:
                func(r.left, True)
            if r.right:
                func(r.right, False)
            if not r.left and not r.right and left:
                nonlocal count
                count += r.val

        if not root:
            return 0
        count = 0
        func(root, False)
        return count
