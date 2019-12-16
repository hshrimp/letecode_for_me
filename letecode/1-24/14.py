#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-12-16 10:09
"""
"""编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        sr = ''
        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs[1:]:
                if i >= len(s):
                    return sr
                if s[i] != char:
                    return sr
            sr += char
        return sr
