#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-10-10 17:08
"""
"""给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def canJump(self, nums) -> bool:
        # res = []

        def trackback(nums, n):
            if n >= len(nums):
                # res.append(1)
                return True
            for i in range(n):
                if trackback(nums[i + 1:], nums[i]):
                    return True
            else:
                return False

        return trackback(nums[1:], nums[0])

    def canJump2(self, nums) -> bool:
        if len(nums) == 1:
            return True
        n = nums[0]
        temp = list(nums)
        while n > 0:
            point = 0
            value = 0
            if n >= len(temp) - 1:
                return True
            for i in range(n):
                if value + point <= temp[i + 1] + i:
                    point = i + 1
                    value = temp[i + 1]
            n = value
            temp = temp[point:]
        else:
            return False

    def canJump3(self, nums) -> bool:
        length = len(nums) - 1
        li = [True] + [False] * length
        for i, v in enumerate(nums):
            if li[i]:
                li[i + 1:i + 1 + v] = [True] * v
        return li[-1]

    def canJump4(self, nums) -> bool:
        end = 0
        maxPosition = 0
        for i in range(len(nums) - 1):
            # 找能跳的最远的
            maxPosition = max(maxPosition, nums[i] + i)
            if i == end:
                # 遇到边界，就更新边界，并且步数加一
                end = maxPosition
                if end >= len(nums) - 1:
                    return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.canJump([3, 2, 2, 0, 4]))
    print(sol.canJump2([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]))
    print(sol.canJump3([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0, 0]))
    print(sol.canJump4([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0, 0]))
