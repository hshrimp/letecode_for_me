#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/3/30 下午3:45
"""
"""515. 在每个树行中找最大值
您需要在二叉树的每一行中找到最大的值。

示例：

输入: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

输出: [1, 3, 9]"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode):
        res = []

        def find(r, level):
            if not r:
                return
            if len(res) < level:
                res.append([r.val])
            else:
                res[level].append(r.val)
            find(r.left, level + 1)
            find(r.right, level + 1)

        find(root, 0)
        return [max(li) for li in res]


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestValues())
