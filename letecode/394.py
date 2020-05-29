#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-05-28 20:43
"""
"""394. 字符串解码
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例:

s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef"."""


class Solution:
    def decodeString(self, s: str) -> str:
        def get_num(s, left):
            for i in range(2, left + 1):
                if not s[left - i:left].isdigit():
                    return int(s[left - i + 1:left]), left - i + 1
            else:
                return int(s[:left]), 0

        length = len(s)
        while '[' in s:
            index = s.index('[')
            left = index
            for i in range(index + 1, length):
                if s[i] == ']':
                    num, start = get_num(s, left)
                    s = s[:start] + s[left + 1:i] * num + s[i + 1:]
                    break
                if s[i] == '[':
                    left = i

        return s

    def decodeString2(self, s: str) -> str:
        def get_num(s, left):
            for i in range(2, left + 1):
                if not s[left - i].isdigit():
                    return int(s[left - i + 1:left]), left - i + 1
            else:
                return int(s[:left]), 0

        if '[' not in s:
            return s
        flag = 0
        length = len(s)
        index = s.index('[')
        num, start = get_num(s, index)
        for i in range(index + 1, length):
            if s[i] == ']':
                if flag == 0:
                    return s[:start] + num * self.decodeString2(s[index + 1:i]) + self.decodeString2(s[i + 1:])
                else:
                    flag -= 1
            if s[i] == '[':
                flag += 1

    def decodeString3(self, s: str) -> str:
        stack = []
        length = len(s)
        i = 0
        while i < length:
            if s[i].isdigit():
                index = s[i:].index('[')
                stack.append(int(s[i:index + i]))
                i += index + 1
            elif s[i] == ']':
                string = ''
                while stack:
                    temp = stack.pop()
                    if isinstance(temp, int):
                        stack.append(temp * string[::-1])
                        break
                    else:
                        string += temp[::-1]
                i += 1
            else:
                stack.append(s[i])
                i += 1
        return ''.join(stack)

    def decodeString4(self, s: str) -> str:
        res = ''
        stack = []
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                stack.append((num, res))
                num = 0
                res = ''
            elif c == ']':
                top = stack.pop()
                res = top[1] + top[0] * res
            else:
                res += c
        return res


if __name__ == '__main__':
    sol = Solution()
    s = "100[leetcode]"
    # s = '3[a2[c]]'
    s = "3[a]2[bc]"
    s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"  # "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
    print(sol.decodeString4(s))
