#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/7/21
"""
"""653. 两数之和 IV - 输入 BST
给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

示例 1：

输入: root = [5,3,6,2,4,null,7], k = 9
输出: true

示例 2：

输入: root = [5,3,6,2,4,null,7], k = 28
输出: false
示例 3：

输入: root = [2,1,3], k = 4
输出: true
示例 4：

输入: root = [2,1,3], k = 1
输出: false
示例 5：

输入: root = [2,1,3], k = 3
输出: true
 

提示:

二叉树的节点个数的范围是  [1, 10**4].
-10**4 <= Node.val <= 10**4
root 为二叉搜索树
-10**5 <= k <= 10**5
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        visited = set()
        res = [False]

        def travel(r):
            if not r:
                return
            if r.val in visited:
                res[0] = True
                return
            visited.add(k - r.val)
            travel(r.left)
            travel(r.right)

        travel(root)
        return res[0]

    def findTarget2(self, root: TreeNode, k: int) -> bool:
        li = []

        def travel(r):
            if not r:
                return
            travel(r.left)
            li.append(r.val)
            travel(r.right)

        travel(root)
        l = 0
        r = len(li) - 1
        while l < r:
            count = li[l] + li[r]
            if count == k:
                return True
            if count > k:
                r -= 1
            else:
                l += 1
        return False
