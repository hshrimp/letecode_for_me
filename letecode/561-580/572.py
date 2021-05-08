#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/5/7 下午5:30
"""
"""572. 另一个树的子树
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。
s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

示例 1:
给定的树 s:

     3
    / \
   4   5
  / \
 1   2
给定的树 t：

   4 
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

示例 2:
给定的树 s：

     3
    / \
   4   5
  / \
 1   2
    /
   0
给定的树 t：

   4
  / \
 1   2
返回 false。"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def equal(r1, r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2:
                return False
            if r1.val == r2.val and equal(r1.left, r2.left) and equal(r1.right, r2.right):
                return True
            return False

        if root:
            return equal(root, subRoot) | self.isSubtree(root.left, subRoot) | self.isSubtree(root.right, subRoot)
        else:
            return equal(root, subRoot)
