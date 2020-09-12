#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/3 下午8:17
"""
"""412. Fizz Buzz
写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

示例：

n = 15,

返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]"""


class Solution:
    def fizzBuzz(self, n: int):
        res = []
        for i in range(1, n + 1):
            if i % 3 == 0:
                if i % 5 == 0:
                    res.append('FizzBuzz')
                else:
                    res.append('Fizz')
            elif i % 5 == 0:
                res.append('Buzz')
            else:
                res.append(str(i))
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.fizzBuzz(16))
