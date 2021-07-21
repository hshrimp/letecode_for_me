#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/7/15 下午5:29
"""
"""637. 二叉树的层平均值
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

示例 1：

输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
 

提示：

节点值的范围在32位有符号整数范围内。"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode):
        res = []

        def travel(r, level):
            if not r:
                return
            if len(res) < level + 1:
                res.append([r.val, 1])
            else:
                res[level][0] += r.val
                res[level][1] += 1
            travel(r.left, level + 1)
            travel(r.right, level + 1)

        travel(root, 0)
        return [val / num for val, num in res]
