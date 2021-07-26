#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/7/22
"""
"""777. 在LR字符串中交换相邻字符
在一个由 'L' , 'R' 和 'X' 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。一次移动操作指用一个"LX"替换一个"XL"，
或者用一个"XR"替换一个"RX"。现给定起始字符串start和结束字符串end，请编写代码，当且仅当存在一系列移动操作使得start可以转换成end时， 返回True。

示例 :

输入: start = "RXXLRXRXL", end = "XRLXXRRLX"
输出: True
解释:
我们可以通过以下几步将start转换成end:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
 

提示：

1 <= len(start) = len(end) <= 10000。
start和end中的字符串仅限于'L', 'R'和'X'。
"""


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        before2after = {'XL': 'LX', 'RX': 'XR'}
        l = 0
        length = len(start)
        while l < length:
            print(start, end)
            while l < length and start[l] == end[l]:
                l += 1
            if l == length:
                return True
            r = l
            while r < length and start[r] != end[l]:
                r += 1
            for i in range(r, l, -1):
                if start[i - 1:i + 1] not in before2after:
                    return False
                else:
                    start = start[:i - 1] + start[i - 1:i + 1][::-1] + start[i + 1:]
            l += 1
        return start == end

    def canTransform2(self, start: str, end: str) -> bool:
        before2after = {'XL', 'RX'}
        l = 0
        start = list(start)
        length = len(start)
        while l < length:
            print(start, end)
            while l < length and start[l] == end[l]:
                l += 1
            if l == length:
                return True
            r = l
            while r < length and start[r] != end[l]:
                r += 1
            if r >= length:
                return False
            for i in range(r, l, -1):
                if start[i - 1] + start[i] not in before2after:
                    return False
                else:
                    start[i - 1], start[i] = start[i], start[i - 1]
            l += 1
        return start == end

    def canTransform3(self, start: str, end: str) -> bool:
        l = 0
        start = list(start)
        length = len(start)
        while l < length:
            print(start, end)
            while l < length and start[l] == end[l]:
                l += 1
            if l == length:
                return True
            if end[l] not in start[l:]:
                return False
            else:
                r = start[l:].index(end[l]) + l
            if end[l] == 'L':
                if start[l:r] == ['X'] * (r - l):
                    start[l], start[r] = start[r], start[l]
                else:
                    return False
            if end[l] == 'X':
                if start[l:r] == ['R'] * (r - l):
                    start[l], start[r] = start[r], start[l]
                else:
                    return False
            l += 1
        return start == end

    def canTransform4(self, start: str, end: str) -> bool:
        from collections import Counter
        if Counter(start) != Counter(end):
            return False
        l = 0
        start = list(start)
        length = len(start)
        while l < length:
            print(start, end)
            while l < length and start[l] == end[l]:
                l += 1
            if l == length:
                return True

            r = start[l:].index(end[l]) + l
            if end[l] == 'L':
                if start[l:r] == ['X'] * (r - l):
                    start[l], start[r] = start[r], start[l]
                else:
                    return False
            elif end[l] == 'X':
                if start[l:r] == ['R'] * (r - l):
                    start[l], start[r] = start[r], start[l]
                else:
                    return False
            else:
                return False
            l += 1
        return start == end

    def canTransform5(self, start: str, end: str) -> bool:
        i, j = 0, 0
        length = len(start)
        while i < length or j < length:
            while i < length and start[i] == 'X':
                i += 1
            while j < length and end[j] == 'X':
                j += 1
            if (i >= length and j < length) or (i < length and j >= length):
                return False
            if i >= length and j >= length:
                return True
            if start[i] != end[j]:
                return False
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False
            i += 1
            j += 1
        return True


if __name__ == '__main__':
    sol = Solution()
    start = "XLLR"
    end = "LXLR"
    print(sol.canTransform(start, end))
    print(sol.canTransform2(start, end))
    print(sol.canTransform3(start, end))
    print(sol.canTransform4(start, end))
    print(sol.canTransform5("RXXLRXRXL", "XRLXXRRLX"))
# "LX"替换一个"XL"，
# 或者用一个"XR"替换一个"RX"
