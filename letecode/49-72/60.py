#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-09-29 10:38
"""
"""给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        all = []

        def run(li1, li2):
            if len(li2) == 1:
                all.append(li1 + li2)
                return
            for i, n in enumerate(li2):
                run(li1 + [n], li2[0:i] + li2[i + 1:])
                if len(all) == k:
                    return

        run([], [i for i in range(1, n + 1)])
        return ''.join([str(i) for i in all[-1]])

    def getPermutation2(self, n: int, k: int) -> str:
        li = [str(i) for i in range(1, n + 1)]
        res = ''
        nums = [1]
        for i in range(2, n):
            nums.append(nums[-1] * i)
        nums.reverse()

        while k > 0:
            for i, num in enumerate(nums):
                p, k = divmod(k, num)
                if not k:
                    res = res + li[p-1]
                    li.pop(p-1)
                    res += ''.join(li[::-1])
                    return res
                else:
                    res = res + li[p]
                    li.pop(p)


if __name__ == '__main__':
    sol = Solution()
    print(sol.getPermutation(4, 9))
    print(sol.getPermutation2(4, 9))
