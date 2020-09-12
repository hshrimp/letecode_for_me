#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/4 上午11:05
"""
"""319. 灯泡开关
初始时有 n 个灯泡关闭。 第 1 轮，你打开所有的灯泡。 第 2 轮，每两个灯泡你关闭一次。 
第 3 轮，每三个灯泡切换一次开关（如果关闭则开启，如果开启则关闭）。第 i 轮，每 i 个灯泡切换一次开关。
 对于第 n 轮，你只切换最后一个灯泡的开关。 找出 n 轮后有多少个亮着的灯泡。

示例:

输入: 3
输出: 1 
解释: 
初始时, 灯泡状态 [关闭, 关闭, 关闭].
第一轮后, 灯泡状态 [开启, 开启, 开启].
第二轮后, 灯泡状态 [开启, 关闭, 开启].
第三轮后, 灯泡状态 [开启, 关闭, 关闭]. 

你应该返回 1，因为只有一个灯泡还亮着。"""


class Solution:
    def bulbSwitch(self, n: int) -> int:
        res = [0] * n
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                if j % i == 0:
                    if res[j - 1] == 0:
                        res[j - 1] = 1
                    else:
                        res[j - 1] = 0
        return sum(res)

    def bulbSwitch2(self, n: int) -> int:
        return int(n**0.5)


if __name__ == '__main__':
    sol = Solution()
    print(sol.bulbSwitch(16))
    print(sol.bulbSwitch2(16))
