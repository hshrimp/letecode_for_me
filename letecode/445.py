#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-04-14 10:10
"""
"""445. 两数相加 II
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

示例：

输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse(li):
            p = None
            c = li
            n = li.next
            while n:
                c.next = p
                p = c
                c = n
                n = n.next
            c.next = p
            return c

        l1 = reverse(l1)
        l2 = reverse(l2)

        h = ListNode(None)
        w = h
        sign = 0
        while l1 or l2:
            if l1 and l2:
                v = l1.val + l2.val + sign
                l1 = l1.next
                l2 = l2.next
            elif l1 and not l2:
                v = l1.val + sign
                l1 = l1.next
            elif not l1 and l2:
                v = l2.val + sign
                l2 = l2.next
            if v >= 10:
                sign = 1
                v -= 10
            else:
                sign = 0
            w.next = ListNode(v)
            w = w.next
        if sign == 1:
            w.next = ListNode(1)
            w = w.next
        h = reverse(h.next)
        return h

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = 0, 0
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
        num = str(num1 + num2)
        h = ListNode(None)
        w = h
        for c in num:
            w.next = ListNode(int(c))
            w = w.next
        return h.next
