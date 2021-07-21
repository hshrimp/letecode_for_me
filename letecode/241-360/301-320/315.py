#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/7 下午4:54
"""
"""315. 计算右侧小于当前元素的个数
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

示例：

输入：nums = [5,2,6,1]
输出：[2,1,1,0] 
解释：
5 的右侧有 2 个更小的元素 (2 和 1)
2 的右侧仅有 1 个更小的元素 (1)
6 的右侧有 1 个更小的元素 (1)
1 的右侧有 0 个更小的元素
 
提示：

0 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4"""


class Solution:
    def countSmaller(self, nums):
        from collections import defaultdict
        d = defaultdict(int)
        length = len(nums)
        res = [0] * length
        for i in range(length - 1, -1, -1):
            d[nums[i]] += 1
            res[i] = sum([d[k] for k in d.keys() if k < nums[i]])
        return res

    def countSmaller2(self, nums):
        from collections import defaultdict
        d = defaultdict(int)
        length = len(nums)
        res = [0] * length
        for i in range(length - 2, -1, -1):
            d[nums[i + 1]] += 1

            if nums[i] > nums[i + 1]:
                res[i] = res[i + 1] + sum([d[k] for k in d.keys() if nums[i + 1] <= k < nums[i]])
            elif nums[i] < nums[i + 1]:
                res[i] = res[i + 1] - sum([d[k] for k in d.keys() if nums[i] <= k < nums[i + 1]])
            else:
                res[i] = res[i + 1]
        return res

    def countSmaller3(self, nums):
        import bisect
        temp = []
        res = []
        for n in reversed(nums):
            index = bisect.bisect_left(temp, n)
            res.append(index)
            temp.insert(index, n)
        return res[::-1]

    def countSmaller33(self, nums):
        import bisect
        length = len(nums)
        temp = []
        res = [0] * length
        for i in range(length - 1, -1, -1):
            index = bisect.bisect_left(temp, nums[i])
            res[i] = index
            temp.insert(index, nums[i])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.countSmaller(nums=[5, 2, 6, 1]))
    print(sol.countSmaller2(nums=[5, 2, 6, 1]))
    print(sol.countSmaller3(nums=[5, 2, 6, 1]))
    print(sol.countSmaller33(nums=[5, 2, 6, 1]))
