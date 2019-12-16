#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-10-22 10:04
"""
"""给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        count = 1
        p = head
        while p.next:
            count += 1
            p = p.next
        q = head
        k = k % count
        if k == 0:
            return head
        count = count - k
        while count > 1:
            q = q.next
            count -= 1
        r = q.next
        q.next = None
        p.next = head
        return r


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    head = ListNode(1)
    p = head
    for i in a[1:]:
        i = ListNode(i)
        p.next = i
        p = p.next
    sol = Solution()
    h = sol.rotateRight(head, 0)
    while h:
        print(h.val, '->')
        h = h.next
