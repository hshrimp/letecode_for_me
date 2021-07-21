#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/3/6 下午2:13
"""
"""508. 出现次数最多的子树元素和
给你一个二叉树的根结点，请你找出出现次数最多的子树元素和。一个结点的「子树元素和」定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。

你需要返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。

示例 1：
输入:

  5
 /  \
2   -3
返回 [2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。

示例 2：
输入：

  5
 /  \
2   -5
返回 [2]，只有 2 出现两次，-5 只出现 1 次。

提示： 假设任意子树元素和均可以用 32 位有符号整数表示。"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findFrequentTreeSum(self, root: TreeNode):
        from collections import defaultdict
        d = defaultdict(int)

        def find(r):
            if not r:
                return 0
            cur = r.val + find(r.left) + find(r.right)
            d[cur] += 1
            return cur

        find(root)
        d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        res = []
        for k, v in d:
            if v != d[0][1]:
                break
            res.append(k)
        return res
