#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/11 下午5:39
"""
"""187. 重复的DNA序列
所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来查找目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。

示例：

输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC", "CCCCCAAAAA"]"""


class Solution:
    def findRepeatedDnaSequences(self, s: str):
        res = set()
        for i in range(len(s) - 9):
            temp = s[i:i + 10]
            if temp in s[i + 1:]:
                res.add(s[i:i + 10])
        return list(res)

    def findRepeatedDnaSequences2(self, s: str):
        temp = set()
        res = set()
        for i in range(len(s) - 9):
            if s[i:i + 10] in temp:
                res.add(s[i:i + 10])
            else:
                temp.add(s[i:i + 10])
        return list(res)



if __name__ == '__main__':
    sol = Solution()
    print(sol.findRepeatedDnaSequences(s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
