#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-12-20 10:27
"""
"""根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/daily-temperatures
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def dailyTemperatures(self, T):
        i = 0
        l = len(T)
        while i < l:
            for j in range(i + 1, l):
                if T[i] < T[j]:
                    T[i] = j - i
                    break
            else:
                T[i] = 0
            i += 1
        return T

    def dailyTemperatures2(self, T):
        l = len(T)
        res = [0] * l
        stack = []
        for i in range(l - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res



if __name__ == '__main__':
    sol = Solution()
    print(sol.dailyTemperatures2([73, 74, 75, 71, 69, 72, 76, 73]))
