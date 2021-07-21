#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/1/12 上午10:08
"""

"""464. 我能赢吗
在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和达到或超过 100 的玩家，即为胜者。

如果我们将游戏规则改为 “玩家不能重复使用整数” 呢？

例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。

给定一个整数 maxChoosableInteger （整数池中可选择的最大数）和另一个整数 desiredTotal（累计和），
判断先出手的玩家是否能稳赢（假设两位玩家游戏时都表现最佳）？

你可以假设 maxChoosableInteger 不会大于 20， desiredTotal 不会大于 300。

示例：

输入：
maxChoosableInteger = 10
desiredTotal = 11

输出：
false

解释：
无论第一个玩家选择哪个整数，他都会失败。
第一个玩家可以选择从 1 到 10 的整数。
如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。"""


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        import functools
        if maxChoosableInteger >= desiredTotal:
            return True
        if sum(range(1, maxChoosableInteger + 1)) < desiredTotal:
            return False

        @functools.lru_cache(None)
        def find(visited, des):
            for i in range(1, maxChoosableInteger + 1):
                cur = 1 << i
                if visited & cur == 0:
                    if i >= des or not find(visited | cur, des - i):
                        return True

            return False

        return find(0, desiredTotal)

    def canIWin2(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        import functools
        if desiredTotal <= maxChoosableInteger: return True
        if sum(range(maxChoosableInteger + 1)) < desiredTotal: return False

        @functools.lru_cache(None)
        def dfs(used, desiredTotal):
            print(bin(used), desiredTotal)
            for i in range(maxChoosableInteger):
                cur = 1 << i
                if cur & used == 0:
                    if desiredTotal <= i + 1 or not dfs(cur | used, desiredTotal - i - 1):
                        return True
            return False

        return dfs(0, desiredTotal)


if __name__ == '__main__':
    sol = Solution()
    maxChoosableInteger = 10
    desiredTotal = 40
    print(sol.canIWin(maxChoosableInteger, desiredTotal))
    print(sol.canIWin2(maxChoosableInteger, desiredTotal))
