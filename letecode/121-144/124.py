# !/usr/bin/python
# -*-coding:utf-8-*-
# Author: wushaohong
"""124. 二叉树中的最大路径和
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
# 方案一：
任意叶子节点到其余叶子结点形成的数组，
对数组求连续子数组的最大和
进一步：
对每个树，分为左边和右边，求左边的数组和右边的数组，然后左右数组两两组合
优化：
左边数组可以先对数组求连续子数组的最大和，不需要左右数组两两组合再去求连续子数组的最大和
再优化：
只需要拿出左边所有组合的求连续子数组的最大和后的最后一个（以最后一个结束的连续子数组的最大和）的最大的数，然后跟右边的数组去组合就行了。
备注：仍然超时。
"""


class Solution:
    res = -float("inf")

    def maxPathSum(self, root: TreeNode) -> int:
        from collections import deque

        def get_li(r, li, dir):
            if dir == 'left':
                li.appendleft(r.val)
                if not r.left and not r.right:
                    left_res.append(li)
                    return
                if r.left:
                    get_li(r.left, deque(li), 'left')
                if r.right:
                    get_li(r.right, deque(li), 'left')
            else:
                li.append(r.val)
                if not r.left and not r.right:
                    right_res.append(li)
                    return
                if r.left:
                    get_li(r.left, deque(li), 'right')
                if r.right:
                    get_li(r.right, deque(li), 'right')

        if not root:
            return 0
        left_res = []
        right_res = []
        if root.left:
            get_li(root.left, deque(), 'left')
            self.maxPathSum(root.left)
        if root.right:
            get_li(root.right, deque(), 'right')
            self.maxPathSum(root.right)
        if not left_res:
            left_res = [deque()]
        if not right_res:
            right_res = [deque()]
        for li1 in left_res:
            li1 += deque([root.val])
            for i in range(1, len(li1)):
                li1[i] += max(li1[i - 1], 0)
        temp = max(max(li1[-1] for li1 in left_res), 0)
        temp_max = max(max(li1) for li1 in left_res)
        self.res = max(temp_max, self.res)
        for li2 in right_res:
            li2t = deque(li2)
            for i in range(len(li2)):
                if i == 0:
                    li2t[0] += temp
                else:
                    li2t[i] += max(li2t[i - 1], 0)
            self.res = max(deque([self.res]) + li2t)
        return self.res


"""
# 方案二：
获取左子树的，通过左子树的根结点的最大值
获取右子树的，通过右子树的根结点的最大值
最后通过左根右组成的数组，求连续子数组的最大和
击败99%+
"""


class Solution2:
    res = -float('inf')

    def maxPathSum(self, root: TreeNode) -> int:
        def get_max(root):
            if not root.left and not root.right:
                return root.val

            if root.left:
                # get_li(root.left, deque(), 'left')
                left_max = get_max(root.left)
            else:
                left_max = -float("inf")
            if root.right:
                # get_li(root.right, deque(), 'right')
                right_max = get_max(root.right)
            else:
                right_max = -float("inf")
            self.res = max(self.res, left_max + root.val + right_max, left_max, right_max)
            return max([left_max + root.val, right_max + root.val, root.val])

        if not root.left and not root.right:
            return root.val
        if root.left:
            # get_li(root.left, deque(), 'left')
            left_max = get_max(root.left)
        else:
            left_max = -float("inf")
        if root.right:
            # get_li(root.right, deque(), 'right')
            right_max = get_max(root.right)
        else:
            right_max = -float("inf")
        li = [left_max, root.val, right_max]
        for i in range(1, 3):
            li[i] += max(li[i - 1], 0)
        return max(max(li), self.res)
