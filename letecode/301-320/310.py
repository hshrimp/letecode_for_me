#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/2 上午11:06
"""
"""310. 最小高度树
对于一个具有树特征的无向图，我们可选择任何一个节点作为根。图因此可以成为树，在所有可能的树中，具有最小高度的树被称为最小高度树。
给出这样的一个图，写出一个函数找到所有的最小高度树并返回他们的根节点。

格式

该图包含 n 个节点，标记为 0 到 n - 1。给定数字 n 和一个无向边 edges 列表（每一个边都是一对标签）。
你可以假设没有重复的边会出现在 edges 中。由于所有的边都是无向边， [0, 1]和 [1, 0] 是相同的，因此不会同时出现在 edges 里。

示例 1:

输入: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

输出: [1]
示例 2:

输入: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

输出: [3, 4]
说明:

 根据树的定义，树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。
树的高度是指根节点和叶子节点之间最长向下路径上边的数量。"""
from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges):
        def find_deep(node):
            stack = {node}
            deep = 0
            visited = {node}
            while len(visited) < n:
                if deep >= res[0]:
                    return
                temp = set()
                for num in stack:
                    temp.update(node2other[num])
                deep += 1
                visited.update(temp)
                stack = temp
            if deep == res[0]:
                res[1].append(node)
            else:
                res[0] = deep
                res[1] = [node]

        if n == 1:
            return [0]
        node2other = defaultdict(set)
        res = [n, []]
        for edge in edges:
            node2other[edge[0]].add(edge[1])
            node2other[edge[1]].add(edge[0])
        for node in node2other.keys():
            find_deep(node)
        return res[1]

    def findMinHeightTrees2(self, n: int, edges):
        def find_deep(node):
            stack = {node}
            deep = 0
            visited = set()
            while len(visited) < n:
                if deep >= res[0]:
                    return
                temp = set()
                for num in stack:
                    if num not in visited:
                        temp.update(node2other[num])
                deep += 1
                visited.update(stack)
                stack = temp
            if deep == res[0]:
                res[1].append(node)
            else:
                res[0] = deep
                res[1] = [node]

        if n == 1:
            return [0]
        node2other = defaultdict(set)
        res = [n, []]
        for edge in edges:
            node2other[edge[0]].add(edge[1])
            node2other[edge[1]].add(edge[0])
        for node in node2other.keys():
            find_deep(node)
        return res[1]

    def findMinHeightTrees3(self, n: int, edges):
        node2other = defaultdict(set)
        for edge in edges:
            node2other[edge[0]].add(edge[1])
            node2other[edge[1]].add(edge[0])
        stack = {num for num in node2other.keys() if len(node2other[num]) == 1}
        while n > 2:
            temp = set()
            for num in stack:
                n -= 1
                value = node2other[num].pop()
                node2other[value].remove(num)
                if len(node2other[value]) == 1:
                    temp.add(value)
            stack = temp
        return list(stack)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMinHeightTrees(n=6, edges=[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
    print(sol.findMinHeightTrees2(n=4, edges=[[1, 0], [1, 2], [1, 3]]))
    print(sol.findMinHeightTrees3(n=6, edges=[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
