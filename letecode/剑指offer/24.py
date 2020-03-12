#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/3/3 15:30
"""
"""面试题24. 反转链表
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
 
限制：

0 <= 节点个数 <= 5000

注意：本题与主站 206 题相同：https://leetcode-cn.com/problems/reverse-linked-list/"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        h = None
        if not head or not head.next:
            return head
        c = head
        n = head.next
        while n:
            c.next = h
            h = c
            c = n
            n = n.next
        c.next = h
        return c
