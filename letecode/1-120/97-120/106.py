#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-01-17 16:14
"""
"""根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        if not inorder or not postorder:
            return None
        root = postorder[-1]
        res = TreeNode(root)
        i = inorder.index(root)
        res.left = self.buildTree(inorder[:i], postorder[:i])
        res.right = self.buildTree(inorder[i + 1:], postorder[i:len(postorder) - 1])
        return res
