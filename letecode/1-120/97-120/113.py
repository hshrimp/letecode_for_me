#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/2/14 11:10
"""
"""给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum1: int):
        if not root:
            return []
        res = []

        def helper(r, li):
            n = sum(li)
            if not r.left and not r.right:
                if n == sum1:
                    res.append(li)
                return
            if r.left:
                helper(r.left, li + [r.left.val])
            if r.right:
                helper(r.right, li + [r.right.val])

        helper(root, [root.val])
        return res