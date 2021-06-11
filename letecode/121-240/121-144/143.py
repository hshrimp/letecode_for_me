# !/usr/bin/python
# -*-coding:utf-8-*-
# Author: wushaohong
"""143. 重排链表
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3."""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        length = 0
        p = head
        stack = []
        while p:
            length += 1
            stack.append(p)
            p = p.next
        half = length // 2 + 1
        i = 0
        p = head
        while i < half:
            temp = stack.pop()
            temp.next = p.next
            p.next = temp
            i += 1
            p = p.next.next
        p.next = None
