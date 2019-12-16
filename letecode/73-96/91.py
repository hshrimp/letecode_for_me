#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-12-11 09:51
"""
"""一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-ways
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        a = 1
        b = 1
        for i in range(1, len(s)):
            t = b
            if s[i] == '0':
                if s[i - 1] in ['1', '2']:
                    b = a
                else:
                    return 0
            elif s[i - 1] == '1' or (s[i - 1] == '2' and 1 <= int(s[i]) <= 6):
                b = a + b
            a = t
        return b


if __name__ == '__main__':
    sol = Solution()
    print(sol.numDecodings('226'))
