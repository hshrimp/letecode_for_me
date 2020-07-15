#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/9 下午4:11
"""
"""173. 二叉搜索树迭代器
实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。

调用 next() 将返回二叉搜索树中的下一个最小的数。

示例：

BSTIterator iterator = new BSTIterator(root);
iterator.next();    // 返回 3
iterator.next();    // 返回 7
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 9
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 15
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 20
iterator.hasNext(); // 返回 false
 
提示：

next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数。"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.get_stack(root)
        self.stack.sort(reverse=True)

    def get_stack(self, root):
        # 前序遍历
        if root:
            self.stack.append(root.val)
            self.get_stack(root.left)
            self.get_stack(root.right)

    def get_stack2(self, root):
        # 中序遍历
        if root:
            self.get_stack(root.left)
            self.stack.append(root.val)
            self.get_stack(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.stack.pop()

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack != []


class BSTIterator2:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.get_stack(root)

    def get_stack(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        r = self.stack.pop()
        if r.right:
            self.get_stack(r.right)
        return r.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
