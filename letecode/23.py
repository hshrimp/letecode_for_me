#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-08-30 10:21
"""
"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        l = []
        for li in lists:
            while li:
                n = ListNode(li.val)
                l.append(n)
                li = li.next
        l = sorted(l, key=lambda x: x.val)
        if not l:
            return None
        head = l[0]
        for i in range(1, len(l)):
            l[i - 1].next = l[i]
        return head

    def mergeKLists2(self, lists) -> ListNode:
        def merge2(l1, l2):
            head = ListNode(0)
            q = head
            while l1 or l2:
                if l1 and l2:
                    if l1.val < l2.val:
                        q.next = l1
                        l1 = l1.next
                        q = q.next
                    else:
                        q.next = l2
                        l2 = l2.next
                        q = q.next
                elif l1:
                    q.next = l1
                    break
                else:
                    q.next = l2
                    break
            return head.next

        while len(lists) > 1:
            length = len(lists)
            l = []
            for i in range(1, length, 2):
                li = merge2(lists[i], lists[i - 1])
                l.append(li)
            if length % 2 != 0:
                l.append(lists[-1])
            lists = l
        return lists[0] if lists else None
