# !/usr/bin/python
# -*-coding:utf-8-*-
# Author: wushaohong
"""148. 排序链表
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        li = []
        p = head
        while p:
            temp = p
            p = p.next
            temp.next = None
            li.append(temp)
        li = sorted(li, key=lambda x: x.val)
        new = ListNode(-1)
        q = new
        for x in li:
            q.next = x
            q = q.next
        return new.next
