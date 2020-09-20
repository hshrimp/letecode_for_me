#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/16 下午5:10
"""
"""335. 路径交叉
给定一个含有 n 个正数的数组 x。从点 (0,0) 开始，先向北移动 x[0] 米，然后向西移动 x[1] 米，向南移动 x[2] 米，
向东移动 x[3] 米，持续移动。也就是说，每次移动后你的方位会发生逆时针变化。

编写一个 O(1) 空间复杂度的一趟扫描算法，判断你所经过的路径是否相交。

示例 1:

┌───┐
│   │
└───┼──>
    │

输入: [2,1,1,2]
输出: true 
示例 2:

┌──────┐
│      │
│
│
└────────────>

输入: [1,2,3,4]
输出: false 
示例 3:

┌───┐
│   │
└───┼>

输入: [1,1,1,1]
输出: true"""


class Solution:
    def isSelfCrossing(self, x) -> bool:
        length = len(x)
        if length < 4:
            return False
        i = 4
        while i <= length:
            print(i)
            if x[i - 4] >= x[i - 4 + 2] and x[i - 4 + 3] >= x[i - 4 + 1]:
                return True
            if i >= 5:
                if x[i - 5 + 1] == x[i - 5 + 3] and x[i - 5 + 2] <= x[i - 5] + x[i - 5 + 4]:
                    return True
            if i >= 6:
                if x[i - 6 + 5] >= x[i - 6 + 3] - x[i - 6 + 1] >= 0 and x[i - 6 + 4] >= x[i - 6 + 2] - x[i - 6] >= 0 and \
                        x[i - 6 + 4] <= x[i - 6 + 2]:
                    return True
            i += 1
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isSelfCrossing([1, 1, 2, 2, 3, 3, 4, 4, 10, 4, 4, 3, 3, 2, 2, 1, 1]))
