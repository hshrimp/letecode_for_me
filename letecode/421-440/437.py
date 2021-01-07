#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/12/28 下午8:44
"""
"""437. 路径总和 III
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(r, li):
            if not r:
                return 0
            count = 0
            li = [val + r.val for val in li]
            li.append(r.val)
            for v in li:
                if v == sum:
                    count += 1
            return count + dfs(r.left, li) + dfs(r.right, li)

        return dfs(root, [])
