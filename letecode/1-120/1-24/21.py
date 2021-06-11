#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-12-16 10:11
"""
"""将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        head = ListNode(-1)
        ln = head
        while l1 or l2:
            if l1:
                temp1 = l1.val
            if l2:
                temp2 = l2.val
            if temp1 <= temp2:
                if l1:
                    l1 = l1.next
                else:
                    ln.next = l2
                    break
                ln.next = ListNode(temp1)
                ln = ln.next
            else:
                if l2:
                    l2 = l2.next
                else:
                    ln.next = l1
                    break
                ln.next = ListNode(temp2)
                ln = ln.next
        return head.next
