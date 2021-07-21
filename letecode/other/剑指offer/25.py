#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/3/3 16:11
"""
"""面试题25. 合并两个排序的链表
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：

0 <= 链表长度 <= 1000

注意：本题与主站 21 题相同：https://leetcode-cn.com/problems/merge-two-sorted-lists/"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p, q = l1, l2
        head = ListNode(None)
        tail = head
        while p and q:
            if p.val <= q.val:
                tail.next = p
                tail = tail.next
                p = p.next
            else:
                tail.next = q
                tail = tail.next
                q = q.next
        if p and not q:
            tail.next = p
        if not p and q:
            tail.next = q

        return head.next
