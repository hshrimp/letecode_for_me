#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-10-21 11:04
"""
"""给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        i = 0
        res = [1]
        while i < rowIndex:
            li = [1] * (len(res) + 1)
            for j in range(1, len(li) - 1):
                li[j] = res[j] + res[j - 1]
            res = li
            i += 1

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.getRow(4))
