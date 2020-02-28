#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/2/24 17:57
"""
"""面试题06. 从尾到头打印链表
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
 
限制：

0 <= 链表长度 <= 10000"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode):
        li = []
        while head:
            li.append(head.val)
            head = head.next
        return li[::-1]
