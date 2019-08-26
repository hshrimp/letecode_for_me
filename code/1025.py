#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-08-21 09:34
"""
"""
爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

选出任一 x，满足 0 < x < N 且 N % x == 0 。
用 N - x 替换黑板上的数字 N 。
如果玩家无法执行这些操作，就会输掉游戏。

只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。
示例 1：

输入：2
输出：true
解释：爱丽丝选择 1，鲍勃无法进行操作。
示例 2：

输入：3
输出：false
解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。
 
提示：

1 <= N <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divisor-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def divisorGame(self, N: int) -> bool:
        if N == 1:
            return False
        if N == 2:
            return True

        dp = [0] * (N + 1)
        dp[2] = 1
        dp[3] = 2
        for i in range(4, N + 1):
            num = N // 2
            ou = 0
            for j in range(num, 0, -1):
                if N % j == 0:
                    if dp[i - j] == 2:
                        dp[i] = 1
                        ou = 1
                        break
            if ou == 0:
                dp[i] = 2
        if dp[N] == 2:
            return False
        else:
            return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.divisorGame(1))
