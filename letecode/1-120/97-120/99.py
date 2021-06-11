#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-01-19 14:50
"""
"""二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。

示例 1:

输入: [1,3,null,null,2]

   1
  /
 3
  \
   2

输出: [3,1,null,null,2]

   3
  /
 1
  \
   2
示例 2:

输入: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

输出: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
进阶:

使用 O(n) 空间复杂度的解法很容易实现。
你能想出一个只使用常数空间的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/recover-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify r in-place instead.   morris算法
        """

        tmp = root
        first_node = None
        second_node = None
        flag = None

        while tmp:
            if tmp.left:
                pre = tmp.left
                while pre.right and pre.right != tmp:
                    pre = pre.right
                if not pre.right:
                    pre.right = tmp
                    tmp = tmp.left
                    continue
                pre.right = None
            if flag and flag.val > tmp.val:
                if first_node is None:
                    first_node = flag
                second_node = tmp
            flag = tmp
            tmp = tmp.right

        first_node.val, second_node.val = second_node.val, first_node.val
