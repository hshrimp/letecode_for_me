#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/12/3 下午4:46
"""
"""410. 分割数组的最大值
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

注意:
数组长度 n 满足以下条件:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
示例:

输入:
nums = [7,2,5,10,8]
m = 2

输出:
18

解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。"""


class Solution:
    def splitArray(self, nums, m: int) -> int:
        length = len(nums)
        dp = [[0] * m for _ in range(length)]
        count = 0
        for i in range(length):
            count += nums[i]
            dp[i][0] = count
        count = nums[0]
        for i in range(1, m):
            if nums[i] > count:
                count = nums[i]
            dp[i][i] = count
        visited = {}
        for i in range(1, m):
            for j in range(1 + i, length):
                num = float('inf')
                for k in range(1, j + 1):
                    # print(j, i, k, num)
                    # print(dp[j - k][i - 1], sum(nums[j - k + 1:j + 1]))
                    if (j - k + 1, j + 1) in visited:
                        count = visited[(j - k + 1, j + 1)]
                    else:
                        count = sum(nums[j - k + 1:j + 1])
                        visited[(j - k + 1, j + 1)] = count
                    num = min(max(dp[j - k][i - 1], count), num)
                dp[j][i] = num
        return dp[-1][-1]

    def splitArray2(self, nums, m: int) -> int:
        def check(mid):
            count, cnt = 0, 1
            for num in nums:
                if count + num > mid:
                    count = num
                    cnt += 1
                else:
                    count += num
            return cnt <= m

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (right - left) // 2 + left
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    sol = Solution()
    nums = [7, 2, 5, 10, 8]
    m = 3
    print(sol.splitArray(nums, m))
    print(sol.splitArray2(nums, m))
