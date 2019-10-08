#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-09-25 09:56
"""
"""给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def majorityElement(self, nums) -> int:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        max = 0

        for k, v in d.items():
            if v > max:
                max = v
                count = k
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))
