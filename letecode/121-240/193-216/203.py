#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/16 下午4:25
"""
"""203. 移除链表元素
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        p = ListNode()
        pre = p
        p.next = head
        cur = head
        while cur:
            if cur.val == val:
                cur = cur.next
                p.next = cur
            else:
                p = cur
                cur = cur.next
        return pre.next
