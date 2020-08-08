#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/8/4 下午3:17
"""
"""257. 二叉树的所有路径
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode):
        def get(root):
            if not root:
                return []
            left = get(root.left)
            right = get(root.right)
            if not left and not right:
                return [[str(root.val)]]
            else:
                return [[str(root.val)] + l for l in left] + [[str(root.val)] + r for r in right]

        res = get(root)
        return ['->'.join(li) for li in res]
