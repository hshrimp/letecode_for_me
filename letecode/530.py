#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/3/29 下午2:50
"""
"""530. 二叉搜索树的最小绝对差
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

示例：

输入：

   1
    \
     3
    /
   2

输出：
1

解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
 

提示：

树中至少有 2 个节点。
本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def mid(r, pre):
            if not r:
                return pre
            pre = mid(r.left, pre)
            res[0] = min(res[0], r.val - pre)
            pre = r.val
            pre = mid(r.right, pre)
            return pre

        res = [float('inf')]
        mid(root, -float('inf'))
        return res[0]
