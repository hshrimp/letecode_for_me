#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-12-12 10:09
"""
"""反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        h = ListNode(-1)
        h.next = head
        if not head or not head.next:
            return head
        c = head
        n = c.next
        while n:
            h = c
            c = n
            n = n.next
            c.next = h
        head.next = None
        return c
