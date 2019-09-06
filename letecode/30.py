#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-09-05 09:46
"""
"""给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def findSubstring(self, s: str, words):
        if not words or not s:
            return []
        res = []
        length = len(words[0])
        all_len = len(words) * length
        d = set()
        for w in words:
            d.add(w[0])
            # if w not in s:
            #     return []
        k = 0
        while len(s[k:]) >= all_len:
            if s[k] not in d:
                k += 1
                continue
            temp = list(words)
            p = k
            while temp:
                if s[p:p + length] in temp:
                    temp.remove(s[p:p + length])
                    p += length
                else:
                    break
            if not temp:
                res.append(k)
            k += 1
        return res


if __name__ == '__main__':
    s = "barsfoothefoobarman"
    words = ["foo", "bar"]
    sol = Solution()
    print(sol.findSubstring(s, words))
