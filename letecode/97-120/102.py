#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-01-15 10:31
"""
"""给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        res = []

        def helper(r, n):
            if not r:
                return
            if len(res) > n:
                res[n].append(r.val)
            else:
                res.append([r.val])
            helper(r.left, n + 1)
            helper(r.right, n + 1)

        helper(root, 0)
        return res
