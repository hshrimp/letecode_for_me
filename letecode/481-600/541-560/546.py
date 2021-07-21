#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/4/15 下午5:12
"""
"""546. 移除盒子
给出一些不同颜色的盒子，盒子的颜色由数字表示，即不同的数字表示不同的颜色。

你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。
每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1），这样一轮之后你将得到 k * k 个积分。

当你将所有盒子都去掉之后，求你能获得的最大积分和。

 
示例 1：

输入：boxes = [1,3,2,2,2,3,4,3,1]
输出：23
解释：
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 分) 
----> [1, 3, 3, 3, 1] (1*1=1 分) 
----> [1, 1] (3*3=9 分) 
----> [] (2*2=4 分)
示例 2：

输入：boxes = [1,1,1]
输出：9
示例 3：

输入：boxes = [1]
输出：1
 

提示：

1 <= boxes.length <= 100
1 <= boxes[i] <= 100"""


class Solution:
    def removeBoxes(self, boxes) -> int:
        visited = {}

        def dfs(l, r, n):
            if (l, r, n) in visited:
                return visited[(l, r, n)]
            if l + 1 == r:
                return (n + 1) ** 2
            if boxes[l] == boxes[l + 1]:
                return dfs(l + 1, r, n + 1)
            res = (n + 1) ** 2 + dfs(l + 1, r, 0)
            for i in range(l + 2, r):
                if boxes[l] == boxes[i]:
                    res = max(res, dfs(l + 1, i, 0) + dfs(i, r, n + 1))
            visited[(l, r, n)] = res
            return res

        return dfs(0, len(boxes), 0)


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]))
