#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-11-26 10:14
"""
"""格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。

给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。

示例 1:

输入: 2
输出: [0,1,3,2]
解释:
00 - 0
01 - 1
11 - 3
10 - 2

对于给定的 n，其格雷编码序列并不唯一。
例如，[0,2,3,1] 也是一个有效的格雷编码序列。

00 - 0
10 - 2
11 - 3
01 - 1
示例 2:

输入: 0
输出: [0]
解释: 我们定义格雷编码序列必须以 0 开头。
     给定编码总位数为 n 的格雷编码序列，其长度为 2^n。当 n = 0 时，长度为 2^0 = 1。
     因此，当 n = 0 时，其格雷编码序列为 [0]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gray-code
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return ['0']
        num = 2 ** n

        def track(li):
            if len(li) == num:
                return li
            for i, c in enumerate(li[-1]):
                print(li, li[-1], i, c)
                if c == '0':
                    t = li[-1][0:i] + '1' + li[-1][i + 1:]
                elif c == '1':
                    t = li[-1][0:i] + '0' + li[-1][i + 1:]
                if t not in li:
                    res = track(li + [t])
                    if res:
                        return res

        lis = ['0' * n]
        lis = track(lis)
        for i, l in enumerate(lis):
            lis[i] = int(l, 2)
        return lis

    def grayCode2(self, n):
        if n == 0:
            return ['0']
        res = ['0', '1']
        for i in range(n - 1):
            res = ['0' + v for v in res] + ['1' + v for v in res[::-1]]
        return [int(v, 2) for v in res]


if __name__ == '__main__':
    sol = Solution()
    print(sol.grayCode2(2))
