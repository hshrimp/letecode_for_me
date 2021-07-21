#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/8 下午2:20
"""
"""1081. 不同字符的最小子序列
返回字符串 text 中按字典序排列最小的子序列，该子序列包含 text 中所有不同字符一次。

示例 1：

输入："cdadabcc"
输出："adbc"
示例 2：

输入："abcd"
输出："abcd"
示例 3：

输入："ecbacba"
输出："eacb"
示例 4：

输入："leetcode"
输出："letcod"
 
提示：

1 <= text.length <= 1000
text 由小写英文字母组成
 
注意：本题目与 316 https://leetcode-cn.com/problems/remove-duplicate-letters/ 相同"""


class Solution:
    def smallestSubsequence(self, text: str) -> str:
        def exist(li, index):
            if not li:
                flag[0] = True
                return
            while li[0] in text[index:]:
                index += text[index:].index(li[0])
                if set(li) - set(text[index:]) == set():
                    exist(li[1:], index + 1)
                else:
                    break
                index += 1

        from itertools import permutations
        s = set(text)
        lis = list(permutations(s))
        lis.sort()
        flag = [False]
        for li in lis:
            exist(list(li), 0)
            if flag[0]:
                return ''.join(li)

    def smallestSubsequence2(self, text: str) -> str:
        from collections import Counter
        stack = []
        visited = set()
        count = Counter(text)
        for c in text:
            if c not in visited:
                while stack and stack[-1] > c and count[stack[-1]] > 0:
                    visited.remove(stack.pop())
                    print(c, stack, visited)
                stack.append(c)
                visited.add(c)
            count[c] -= 1
        return ''.join(stack)


if __name__ == '__main__':
    sol = Solution()
    print(sol.smallestSubsequence('ddeeeccdce'))
    print(sol.smallestSubsequence2('cdadabcc'))
