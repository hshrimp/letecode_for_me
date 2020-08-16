#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/8/12 上午10:20
"""
"""297. 二叉树的序列化与反序列化
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，
同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，
你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        stack = deque([root])
        while stack:
            cur = stack.popleft()
            if cur:
                res.append(cur.val)
                if cur.left:
                    stack.append(cur.left)
                else:
                    stack.append(None)
                if cur.right:
                    stack.append(cur.right)
                else:
                    stack.append(None)
            else:
                res.append(None)
        while res and res[-1] is None:
            res.pop()
        # print(res)
        return str(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        li = data[1:-1].split(', ')
        # print(li)
        if not li or not li[0]:
            return None
        root = TreeNode(int(li[0]))
        stack = deque([root])
        i = 1
        length = len(li)
        while i < length:
            cur = stack.popleft()
            if cur:
                if li[i] != 'None':
                    cur.left = TreeNode(int(li[i]))
                else:
                    cur.left = None
                stack.append(cur.left)
                i += 1
                if i < length:
                    if li[i] != 'None':
                        cur.right = TreeNode(int(li[i]))
                    else:
                        cur.right = None
                    stack.append(cur.right)
                i += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
