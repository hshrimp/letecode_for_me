#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-01-17 11:22
"""
"""根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        def helper(start=0, end=len(inorder)):
            nonlocal preid
            if start == end:
                return None
            val = preorder[preid]
            preid += 1
            root = TreeNode(val)
            i = val2id[val]
            root.left = helper(start, i)
            root.right = helper(i + 1, end)
            return root

        preid = 0
        val2id = {val: id for id, val in enumerate(inorder)}
        return helper()
