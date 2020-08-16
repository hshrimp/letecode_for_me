#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/8/10 下午3:22
"""
"""273. 整数转换英文表示
将非负整数转换为其对应的英文表示。可以保证给定输入小于 231 - 1 。

示例 1:

输入: 123
输出: "One Hundred Twenty Three"
示例 2:

输入: 12345
输出: "Twelve Thousand Three Hundred Forty Five"
示例 3:

输入: 1234567
输出: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
示例 4:

输入: 1234567891
输出: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"""


class Solution:
    def numberToWords(self, num: int) -> str:
        def get(cur):
            s = []
            if cur >= 100:
                cur, last = divmod(cur, 100)
                s += [num2str[cur] + ' ' + 'Hundred']
                cur = last
            if cur >= 20:
                cur, last = divmod(cur, 10)
                s += [num2str[cur * 10]]
                cur = last
            if cur:
                s += [num2str[cur]]
            return ' '.join(s)

        if not num:
            return 'Zero'
        num2str = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
                   10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
                   17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
                   50: 'Fifty', 60: 'Sixty', 70: 'Seventy',
                   80: 'Eighty', 90: 'Ninety'}
        l = [1000000000, 1000000, 1000, 100]
        title = ['Billion', 'Million', 'Thousand', 'Hundred']
        res = []
        i = 0
        while i < len(l):
            cur, num = divmod(num, l[i])
            temp = get(cur)
            if temp:
                res.append(temp + ' ' + title[i])
            i += 1
        temp = get(num)
        if temp:
            res.append(temp)
        return ' '.join(res)


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberToWords(100) + 'aaa')
