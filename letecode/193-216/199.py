#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/15 上午11:02
"""
"""199. 二叉树的右视图
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode):
        def get(r, level):
            if not r:
                return
            else:
                if len(res) <= level:
                    res.append([r.val])
                else:
                    res[level].append(r.val)
                get(r.left, level + 1)
                get(r.right, level + 1)

        res = []
        get(root, 0)
        return [li[-1] for li in res]

    def rightSideView2(self, root: TreeNode):
        def get(r, level):
            if not r:
                return
            else:
                if len(res) <= level:
                    res.append(r.val)
                else:
                    res[level] = r.val
                get(r.left, level + 1)
                get(r.right, level + 1)

        res = []
        get(root, 0)
        return res

    def rightSideView3(self, root: TreeNode):
        def get(r, level):
            if not r:
                return
            else:
                if len(res) <= level:
                    res.append(r.val)
                get(r.right, level + 1)
                get(r.left, level + 1)

        res = []
        get(root, 0)
        return res
