#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/2/17 14:07
"""
"""给定一个二叉树

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

进阶：

你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

示例：

输入：root = [1,2,3,4,5,null,7]
输出：[1,#,2,3,#,4,5,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
 
提示：

树中的节点数小于 6000
-100 <= node.val <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        seq = [root]
        while seq:
            l = len(seq)
            if seq[0].left:
                seq.append(seq[0].left)
            if seq[0].right:
                seq.append(seq[0].right)
            for i in range(l - 1):
                seq[i].next = seq[i + 1]
                if seq[i + 1].left:
                    seq.append(seq[i + 1].left)
                if seq[i + 1].right:
                    seq.append(seq[i + 1].right)
            seq = seq[l:]
        return root

