#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/12/16 下午7:08
"""
"""423. 从英文中重建数字
给定一个非空字符串，其中包含字母顺序打乱的英文单词表示的数字0-9。按升序输出原始的数字。

注意:

输入只包含小写英文字母。
输入保证合法并可以转换为原始的数字，这意味着像 "abc" 或 "zerone" 的输入是不允许的。
输入字符串的长度小于 50,000。
示例 1:

输入: "owoztneoer"

输出: "012" (zeroonetwo)
示例 2:

输入: "fviefuro"

输出: "45" (fourfive)"""

from collections import defaultdict


class Solution:
    def originalDigits(self, s: str) -> str:
        nums = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                'eight': '8', 'nine': '9'}
        char2count = defaultdict(list)
        count = 0
        for c in 'abcdefghijklmnopqrstuvwxyz':
            for num in nums.keys():
                if c in num:
                    if c not in char2count:
                        char2count[c] = []
                    char2count[c].append(num)
                    count += 1
        s_char_count = defaultdict(int)
        for c in s:
            s_char_count[c] += 1
        res = {}
        while count:
            for k, v in char2count.items():
                if len(v) == 1:
                    cur_en_num = v[0]
                    cur_num = nums[cur_en_num]
                    nums.pop(cur_en_num)
                    res[cur_num] = s_char_count[k]
                    for char in cur_en_num:
                        # print(k, v, char, char2count[char], char2count)
                        s_char_count[char] -= res[cur_num]
                        if cur_en_num in char2count[char]:
                            char2count[char].remove(cur_en_num)
                            count -= 1

        res = sorted(res.items(), key=lambda x: x[0])
        result = ''
        for k, v in res:
            result += k * v
        return result

    def originalDigits2(self, s: str) -> str:
        from collections import Counter
        count = Counter(s)
        num = {}
        num['0'] = count['z']
        num['8'] = count['g']
        num['4'] = count['u']
        num['2'] = count['w']
        num['6'] = count['x']
        num['5'] = count['f'] - num['4']
        num['3'] = count['h'] - num['8']
        num['9'] = count['i'] - num['5'] - num['6'] - num['8']
        num['1'] = count['o'] - num['0'] - num['2'] - num['4']
        num['7'] = count['s'] - num['6']
        res = [key * num[key] for key in sorted(num.keys())]
        return ''.join(res)


if __name__ == '__main__':
    sol = Solution()
    print(sol.originalDigits('owoztneoerfviefurozero'))
    print(sol.originalDigits2('owoztneoerfviefurozero'))
