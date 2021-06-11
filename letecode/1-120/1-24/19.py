#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-08-29 10:13
"""
"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return None
        p, q = head, head
        count = 0
        while p:
            count += 1
            p = p.next
        if count == n:
            return head.next
        point = count - n - 1
        for _ in range(point):
            q = q.next
        if n == 1:
            q.next = None
        else:
            q.next = q.next.next
        return head

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        # if not head.next:
        #     return None
        temp = ListNode(0)
        temp.next = head
        q, p = temp, temp

        for _ in range(n + 1):
            p = p.next
        while p:
            q = q.next
            p = p.next
        q.next = q.next.next
        return temp.next


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeNthFromEnd())
