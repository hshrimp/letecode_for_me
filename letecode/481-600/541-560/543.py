#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/3/29 下午3:04
"""
"""543. 二叉树的直径
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \     
      4   5    
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

 
注意：两结点之间的路径长度是以它们之间边的数目表示。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def find(r):
            if not r:
                return 0, 0
            if not r.left and not r.right:
                return 1, 1
            left, left_all = find(r.left)
            right, right_all = find(r.right)
            cur_all = left + right + 1
            return max(left, right) + 1, max(left_all, right_all, cur_all)

        return max(find(root)) - 1
