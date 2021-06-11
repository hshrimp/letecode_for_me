#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-12-12 10:23
"""
"""给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/restore-ip-addresses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def restoreIpAddresses(self, s: str):
        res = []

        def track(nums, last):
            print(nums, last)
            if not last:
                return
            if len(nums) == 3:
                if last[0] == '0' and len(last) > 1:
                    return
                if int(last) <= 255:
                    res.append('.'.join(nums) + '.' + last)
                    return
                else:
                    return
            if last[0] == '0':
                track(nums + ['0'], last[1:])
                return
            i = 0
            while i < 3 and i < len(last):
                if int(last[0:i + 1]) <= 255:
                    track(nums + [last[0:i + 1]], last[i + 1:])
                i += 1

        track([], s)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.restoreIpAddresses("25525511135"))
