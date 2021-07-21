#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/2/25 14:06
"""
"""面试题07. 重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
 

限制：

0 <= 节点个数 <= 5000

注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        def helper(start, end):
            nonlocal preid
            if start == end:
                return
            val = preorder[preid]
            r = TreeNode(val)
            preid += 1
            i = val2id.get(val)
            r.left = helper(start, i)
            r.right = helper(i + 1, end)
            return r

        preid = 0
        val2id = {val: id for id, val in enumerate(inorder)}
        return helper(0, len(inorder))
