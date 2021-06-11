# !/usr/bin/python
# -*-coding:utf-8-*-
# Author: wushaohong
"""147. 对链表进行插入排序
对链表进行插入排序。

插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。

插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。

示例 1：

输入: 4->2->1->3
输出: 1->2->3->4
示例 2：

输入: -1->5->3->4->0
输出: -1->0->3->4->5"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        p = head.next
        head.next = None
        new = ListNode(-1)
        new.next = head

        while p:
            print('p=', p.val)
            q = new
            while q.next and q.next.val <= p.val:
                print('q.next=', q.next.val)
                q = q.next
            temp = p
            p = p.next
            temp.next = q.next
            q.next = temp
        return new.next


if __name__ == '__main__':
    li = [4, 2, 1, 3]
    head = ListNode(li[0])
    p = head
    for i in li[1:]:
        n = ListNode(i)
        p.next = n
        p = p.next
    sol = Solution()
    res = sol.insertionSortList(head)
    while res:
        print(res.val)
        res = res.next
