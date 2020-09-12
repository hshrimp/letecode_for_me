#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/2 下午3:22
"""

"""312. 戳气球
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 
这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

求所能获得硬币的最大数量。

说明:

你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
示例:

输入: [3,1,5,8]
输出: 167 
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167"""
from collections import defaultdict
from functools import lru_cache


class Solution:
    def maxCoins(self, nums) -> int:
        def track(count, li):
            if len(li) == 2:
                nonlocal res
                res = max(res, count)
                return
            for i in range(1, len(li) - 1):
                track(count + li[i - 1] * li[i] * li[i + 1], li[:i] + li[i + 1:])

        res = 0
        nums.insert(0, 1)
        nums.append(1)
        track(0, nums)
        return res

    def maxCoins2(self, nums) -> int:
        def get(li):
            # print(li, visited)
            if len(li) == 2:
                return 0
            if tuple(li[1:-1]) in visited:
                return visited[tuple(li[1:-1])]
            temp = [get(li[:i] + li[i + 1:]) + li[i - 1] * li[i] * li[i + 1] for i in range(1, len(li) - 1)]
            # print('temp', temp)
            visited[tuple(li[1:-1])] = max(temp)
            return visited[tuple(li[1:-1])]

        visited = defaultdict(int)
        length = len(nums)
        for i in range(length):
            visited[(nums[i],)] = nums[i]
        for i in range(2, length + 1):
            for j in range(length - i + 1):
                # print(i, j)
                get([1] + nums[j:j + i] + [1])
        return visited[tuple(nums)]

    def maxCoins3(self, nums) -> int:
        def get(li):
            # print(li, visited)
            if len(li) == 2:
                return 0
            if tuple(li[1:-1]) in visited:
                return visited[tuple(li[1:-1])]
            temp = [get(li[:i] + li[i + 1:]) + li[i - 1] * li[i] * li[i + 1] for i in range(1, len(li) - 1)]
            # print('temp', temp, li, visited)
            visited[tuple(li[1:-1])] = max(temp)
            return visited[tuple(li[1:-1])]

        visited = defaultdict(int)
        length = len(nums)
        for i in range(length):
            visited[(nums[i],)] = nums[i]
        for i in range(length):
            # print(nums[:i + 1])
            get([1] + nums[:i + 1] + [1])
        return visited[tuple(nums)]

    def maxCoins4(self, nums) -> int:
        @lru_cache(None)
        def get(left, right):
            if left >= right - 1:
                return 0
            best = 0
            for i in range(left + 1, right):
                total = val[left] * val[i] * val[right]
                total += get(left, i) + get(i, right)
                best = max(best, total)
            return best

        length = len(nums)
        val = [1] + nums + [1]
        return get(0, length + 1)

    def maxCoins5(self, nums) -> int:
        def get(left, right):
            if left >= right - 1:
                return 0
            if (left, right) in visited:
                return visited[(left, right)]
            best = 0
            for i in range(left + 1, right):
                total = val[left] * val[i] * val[right]
                total += get(left, i) + get(i, right)
                best = max(best, total)
            visited[(left, right)] = best
            return best

        length = len(nums)
        visited = defaultdict(int)
        val = [1] + nums + [1]
        return get(0, length + 1)

    def maxCoins6(self, nums) -> int:
        """动态规划"""
        n = len(nums)
        val = [1] + nums + [1]

        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    total = val[i] * val[k] * val[j]
                    total += dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], total)

        return dp[0][n + 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxCoins([4, 5, 4, 4, 4, 5, 4, 4, 5]))
    print(sol.maxCoins2([3, 1, 5, 8]))
    print(sol.maxCoins3([3, 1, 5, 8]))
    print(sol.maxCoins4([3, 1, 5, 8]))
    print(sol.maxCoins5([3, 1, 5, 8]))
    print(sol.maxCoins6([3, 1, 5, 8]))
