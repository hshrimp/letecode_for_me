#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/3/4 下午4:08
"""
"""501. 二叉搜索树中的众数
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
返回[2].

提示：如果众数超过1个，不需考虑输出顺序

进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode):
        from collections import defaultdict
        d = defaultdict(int)

        def count(r):
            if not r:
                return
            d[r.val] += 1
            count(r.left)
            count(r.right)

        count(root)
        d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        res = []
        for k, v in d:
            if v != d[0][1]:
                break
            res.append(k)
        return res

    def findMode2(self, root: TreeNode):
        if not root:
            return []
        cur, times = [0], [0]
        res = []
        max_times = [0]

        def mid(r):
            if not r:
                return
            if r.left:
                mid(r.left)
            if cur[0] == r.val:
                times[0] += 1
            else:
                if times[0] == max_times[0]:
                    res.append(cur[0])
                if times[0] > max_times[0]:
                    max_times[0] = times[0]
                    res.clear()
                    res.append(cur[0])
                cur[0] = r.val
                times[0] = 1
            mid(r.right)

        mid(root)
        if times[0] == max_times[0]:
            res.append(cur[0])
        if times[0] > max_times[0]:
            res.clear()
            res.append(cur[0])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMode())
