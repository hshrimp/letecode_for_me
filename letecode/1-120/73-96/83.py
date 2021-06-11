#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-09-06 10:42
"""
"""给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        s = set()
        q = ListNode(0)
        q.next = head
        p = head
        while p:
            if p.val not in s:
                s.add(p.val)
                p = p.next
                q = q.next
            else:
                q.next = p.next
                p = q.next
        return head
