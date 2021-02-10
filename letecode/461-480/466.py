#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/2/5 下午4:04
"""
"""466. 统计重复个数
由 n 个连接的字符串 s 组成字符串 S，记作 S = [s,n]。例如，["abc",3]=“abcabcabc”。

如果我们可以从 s2 中删除某些字符使其变为 s1，则称字符串 s1 可以从字符串 s2 获得。
例如，根据定义，"abc" 可以从 “abdbec” 获得，但不能从 “acbbe” 获得。

现在给你两个非空字符串 s1 和 s2（每个最多 100 个字符长）和两个整数 0 ≤ n1 ≤ 106 和 1 ≤ n2 ≤ 106。
现在考虑字符串 S1 和 S2，其中 S1=[s1,n1] 、S2=[s2,n2] 。

请你找出一个可以满足使[S2,M] 从 S1 获得的最大整数 M 。

示例：

输入：
s1 ="acb",n1 = 4
s2 ="ab",n2 = 2

返回：
2"""


class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        from collections import deque
        S1 = deque(s1 * n1)
        S2 = s2 * n2
        res = 0
        while True:
            if len(S1) < len(S2):
                return res
            que = deque(S2)
            while que:
                if S1:
                    if S1.popleft() == que[0]:
                        que.popleft()
                else:
                    return res
            res += 1

    def getMaxRepetitions2(self, s1: str, n1: int, s2: str, n2: int) -> int:
        dp = []
        for i in range(len(s2)):
            start = i
            end = 0
            for j in range(len(s1)):
                if s1[j] == s2[start]:
                    start += 1
                    if start == len(s2):
                        start = 0
                        end += 1
            dp.append((start, end))
        res = 0
        next = 0
        for _ in range(n1):
            res += dp[next][1]
            next = dp[next][0]
        return res // n2


if __name__ == '__main__':
    sol = Solution()
    print(sol.getMaxRepetitions(s1="acb", n1=4, s2="ab", n2=2))
    print(sol.getMaxRepetitions2(s1="abaacdabc", n1=4, s2="adcbd", n2=2))
    print(sol.getMaxRepetitions2(s1="nlhqgllunmelayl", n1=10, s2="lnl", n2=1))
