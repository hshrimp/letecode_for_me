#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/4/23 下午4:33
"""
"""556. 下一个更大元素 III
给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。

注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。

示例 1：

输入：n = 12
输出：21
示例 2：

输入：n = 21
输出：-1
 
提示：
1 <= n <= 231 - 1"""


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        import bisect
        n = str(n)[::-1]
        cur_min = n[0]
        for i in range(1, len(n)):
            if n[i] < cur_min:
                temp = sorted(n[:i])
                index = bisect.bisect_right(temp, n[i])
                res = int(n[i + 1:][::-1] + temp[index] + ''.join(temp[:index]) + n[i] + ''.join(temp[index + 1:]))
                return res if res <= 2 ** 31 - 1 else -1
            else:
                cur_min = n[i]
        else:
            return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.nextGreaterElement(1234543213))
