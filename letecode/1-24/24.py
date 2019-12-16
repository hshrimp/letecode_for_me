#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-09-02 09:30
"""
"""给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        p, q = head, head.next
        if q:
            p.next = q.next
            q.next = p
            head = q
        else:
            return head
        while p.next:
            v = p
            p = p.next
            q = p.next
            if q:
                p.next = q.next
                q.next = p
                v.next = q
            else:
                return head
        return head
