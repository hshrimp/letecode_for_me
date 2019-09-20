#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-09-19 10:19
"""
"""给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        temp = 0
        count = []
        if len(num1) > len(num2):
            num2, num1 = num1, num2
        i = 1
        while i - 1 < len(num1):
            cur = int(num1[-i]) + int(num2[-i])
            temp, cur = divmod(cur + temp, 10)
            count.append(str(cur))
            i += 1
        if temp:
            while i - 1 < len(num2):
                temp, cur = divmod(int(num2[-i]) + temp, 10)
                count.append(str(cur))
                if not temp:
                    return num2[:-i] + ''.join(count[::-1])
                i += 1
            if temp:
                return '1' + ''.join(count[::-1])
        else:
            return num2[:-i + 1] + ''.join(count[::-1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.addStrings('99', '9'))
