#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-01-07 10:02
"""
"""给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc" 
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split(' ')
        li = list(map(lambda x: x[::-1], li))
        return ' '.join(li)

    def reverseWords2(self, s: str) -> str:
        s = s[::-1]
        li = s.split(' ')
        li = li[::-1]
        return ' '.join(li)


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseWords("Let's take LeetCode contest"))
