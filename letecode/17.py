#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-08-28 09:48
"""
"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    m = {
        '2': 'abc', '3': 'def', '4': 'ghi',
        '5': 'jkl', '6': 'mno', '7': 'pqrs',
        '8': 'tuv', '9': 'wxyz'
    }

    def dfs(self, i, digits, ans, tmp):
        if i == len(digits):
            ans.append(''.join(tmp))
            return
        for ch in self.m[digits[i]]:
            tmp.append(ch)
            self.dfs(i + 1, digits, ans, tmp)
            tmp.pop()

    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        ans = []
        tmp = []
        self.dfs(0, digits, ans, tmp)
        return ans

    def letterCombinations(self, digits: str):
        l = len(digits)
        if l == 0:
            return []
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        li = list(d[digits[0]])
        for i in range(1, l):
            chars = d[digits[i]]
            temp = []
            for c in chars:
                for s in li:
                    temp.append(s + c)
            li = temp
        return li


if __name__ == '__main__':
    sol = Solution()
    print(sol.letterCombinations('23'))
