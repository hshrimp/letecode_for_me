#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/16 下午5:24
"""
"""207. 课程表
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]

给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？

示例 1:

输入: 2, [[1,0]] 
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
 
提示：

输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
1 <= numCourses <= 10^5"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        def dfs(i):
            if status[i] == 1:
                return False
            if status == -1:
                return True
            status[i] = 1
            for j in a2b[i]:
                if not dfs(j):
                    return False
            status[i] = -1
            return True

        a2b = [[] for _ in range(numCourses)]
        status = [0] * numCourses
        for cur, pre in prerequisites:
            a2b[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

    def canFinish2(self, numCourses: int, prerequisites) -> bool:
        a2b = [[] for _ in range(numCourses)]
        cur_num = [0] * numCourses
        for cur, pre in prerequisites:
            a2b[pre].append(cur)
            cur_num[cur] += 1
        p = [i for i in range(numCourses) if not cur_num[i]]
        for i in p:
            for j in a2b[i]:
                cur_num[j] -= 1
                if not cur_num[j]:
                    p.append(j)
        return not any(cur_num)


if __name__ == '__main__':
    sol = Solution()
    print(sol.canFinish(2, [[1, 0]]))
    print(sol.canFinish2(5, [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [4, 2], [2, 4]]))
