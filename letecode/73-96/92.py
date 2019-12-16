#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-12-11 11:08
"""
"""反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        h = ListNode(0)
        h.next = head
        p = head
        t = p
        c = 1
        while c < m:
            t = p
            p = p.next
            c += 1
        q = p
        while c < n:
            q = q.next
            c += 1
        q = q.next
        while n - m > -1:
            k = p.next
            p.next = q
            q = p
            p = k
            m += 1
        t.next = q
        return h.next

    def reverseBetween2(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        h = ListNode(0)
        h.next = head
        p = head
        t = h
        c = 1
        while c < m:
            t = p
            p = p.next
            c += 1
        hl = t
        tail = p
        ne = p.next
        while c < n:
            t = p
            p = ne
            ne = ne.next
            p.next = t
            c += 1
        hl.next = p
        tail.next = ne
        return h.next
