#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-08-27 10:14
"""
"""
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。

找到所有出现两次的元素。

你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？

示例：

输入:
[4,3,2,7,8,2,3,1]

输出:
[2,3]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-duplicates-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def findDuplicates(self, nums):
        li = []
        d = {}
        for i in nums:
            if i in d:
                li.append(i)
            else:
                d[i] = 1
        return li

    def findDuplicates2(self, nums):
        li = []
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num)-1] *= -1
            else:
                li.append(abs(num))
        return li


if __name__ == '__main__':
    sol = Solution()
    print(sol.findDuplicates2([4, 3, 2, 7, 8, 2, 3, 1]))
