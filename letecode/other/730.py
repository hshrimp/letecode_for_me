#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020-06-03 17:13
"""
"""730. 统计不同回文子序列
给定一个字符串 S，找出 S 中不同的非空回文子序列个数，并返回该数字与 10^9 + 7 的模。

通过从 S 中删除 0 个或多个字符来获得子序列。

如果一个字符序列与它反转后的字符序列一致，那么它是回文字符序列。

如果对于某个  i，A_i != B_i，那么 A_1, A_2, ... 和 B_1, B_2, ... 这两个字符序列是不同的。

示例 1：

输入：
S = 'bccb'
输出：6
解释：
6 个不同的非空回文子字符序列分别为：'b', 'c', 'bb', 'cc', 'bcb', 'bccb'。
注意：'bcb' 虽然出现两次但仅计数一次。
示例 2：

输入：
S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
输出：104860361
解释：
共有 3104860382 个不同的非空回文子序列，对 10^9 + 7 取模为 104860361。
 
提示：

字符串 S 的长度将在[1, 1000]范围内。
每个字符 S[i] 将会是集合 {'a', 'b', 'c', 'd'} 中的某一个。
 """


class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        res = set(S)
        s = set()
        length = len(S)
        for i in range(length):
            cur = S[i]
            res.update([temp + cur for temp in s if temp + cur == (temp + cur)[::-1]])
            s.update([temp + cur for temp in s])
            s.add(cur)
        return len(res) % (10 * 9 + 7)

    def countPalindromicSubsequences2(self, S: str) -> int:
        """
        s[i] != s[j]:
        count("bc") = count("b") + count("c") - count("") = 1 + 1 - 0 = 2
        count("bcc") = count("bc") + count("cc") - count("c") = 2 + 2 - 1 = 3
        count("ab") = count("a") + count("b") - count("") = 1 + 1 - 0 = 2
        count("abc") = count("ab") + count("bc") - count("b") = 2 + 2 - 1 = 3
        count("abcc") = count("abc") + count("bcc") - count("bc") = 3 + 3 - 2 = 4
        count("abccb") = count("abcc") + count("bccb") - count("bcc") = 4 + 6 - 3 = 7

        s[i] == s[j]:
        count("cbc") = 2 * count("b") + 2 = 4
        count("bcab") = 2 * count("ca") + 2 = 6
        count("bcbcb") = 2 * count("cbc") + 1 = 2 * 4 + 1 = 9
        count("bbcabb") = 2 * count("bcab") - count("ca") = 10

        转移方程
        if s[i] != s[j]:
            dp[i][j] = dp[i + 1][j] + dp[i][j-1] - dp[i + 1][j - 1]

        if s[i] == s[j]:
            dp[i][j] = dp[i+1][j-1] * 2 + 1  # 中间这个数就是两端的数 类似 “bcbcb”
                     = dp[i+1][j-1] * 2 + 2 # 中间有两个数类似 “bcab”
                     = dp[i+1][j-1] * 2 - dp[l + 1][r - 1]

        作者：zhanghaha-2
        链接：https://leetcode-cn.com/problems/count-different-palindromic-subsequences/solution/dong-tai-gui-hua-dui-qu-jian-dpfen-lei-tao-lun-by-/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        :param S:
        :return:
        """
        n = len(S)
        # M = 1e9 +7
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for size in range(2, n + 1):
            for i in range(n - size + 1):  # n-size +1  逆序遍历
                j = i + size - 1
                if S[i] != S[j]:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
                else:
                    dp[i][j] = dp[i + 1][j - 1] * 2  # 小区间一分 外面套的大区间又有一份 所以*2
                    l, r = i + 1, j - 1
                    while l <= r and S[l] != S[i]:
                        l += 1
                    while l <= r and S[r] != S[i]:
                        r -= 1
                    if l > r:
                        dp[i][j] += 2
                    elif l == r:
                        dp[i][j] += 1
                    else:
                        dp[i][j] -= dp[l + 1][r - 1]

                dp[i][j] %= 1000000007
        return dp[0][-1]

    def countPalindromicSubsequences3(self, S: str) -> int:
        length = len(S)
        dp = [[0] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1
        for size in range(2, length + 1):
            for i in range(length - size + 1):
                j = i + size - 1
                if S[i] != S[j]:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
                else:
                    dp[i][j] = 2 * dp[i + 1][j - 1]
                    left = i + 1
                    right = j - 1
                    while left <= right and S[i] != S[left]:
                        left += 1
                    while left <= right and S[i] != S[right]:
                        right -= 1
                    if left > right:
                        dp[i][j] += 2
                    elif left == right:
                        dp[i][j] += 1
                    else:
                        dp[i][j] -= dp[left + 1][right - 1]
        return dp[0][-1] % 1000000007


if __name__ == '__main__':
    sol = Solution()
    print(sol.countPalindromicSubsequences2('abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'))
    print(sol.countPalindromicSubsequences3('abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'))
