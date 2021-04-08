#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2021/3/9 上午11:02
"""
"""488. 祖玛游戏
回忆一下祖玛游戏。现在桌上有一串球，颜色有红色(R)，黄色(Y)，蓝色(B)，绿色(G)，还有白色(W)。 现在你手里也有几个球。

每一次，你可以从手里的球选一个，然后把这个球插入到一串球中的某个位置上（包括最左端，最右端）。
接着，如果有出现三个或者三个以上颜色相同的球相连的话，就把它们移除掉。重复这一步骤直到桌上所有的球都被移除。

找到插入并可以移除掉桌上所有球所需的最少的球数。如果不能移除桌上所有的球，输出 -1 。

示例 1：

输入：board = "WRRBBW", hand = "RB"
输出：-1
解释：WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW
示例 2：

输入：board = "WWRRBBWW", hand = "WRBRW"
输出：2
解释：WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty
示例 3：

输入：board = "G", hand = "GGGGG"
输出：2
解释：G -> G[G] -> GG[G] -> empty 
示例 4：

输入：board = "RBYYBBRRB", hand = "YRBGB"
输出：3
解释：RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty 

提示：

你可以假设桌上一开始的球中，不会有三个及三个以上颜色相同且连着的球。
1 <= board.length <= 16
1 <= hand.length <= 5
输入的两个字符串均为非空字符串，且只包含字符 'R','Y','B','G','W'。"""


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        from collections import Counter
        b = Counter(board)
        h = Counter(hand)
        for k, v in b.items():
            if v + h[k] < 3:
                return -1
        res = [6]

        def remove(cur, begin):
            # print(cur, begin)
            begin = max(0, begin)
            length = len(cur)
            if length - begin < 3:
                return cur
            if length - begin == 3 and cur[begin] == cur[begin + 1] == cur[begin + 2]:
                return cur[:begin]
            if length - begin > 3:
                if cur[begin] == cur[begin + 1] == cur[begin + 2] == cur[begin + 3]:
                    return remove(cur[:begin] + cur[begin + 4:], begin=begin - 2)
                if cur[begin] == cur[begin + 1] == cur[begin + 2]:
                    return remove(cur[:begin] + cur[begin + 3:], begin=begin - 2)
                if cur[begin + 1] == cur[begin + 2] == cur[begin + 3]:
                    return remove(cur[:begin + 1] + cur[begin + 4:], begin=begin - 1)
            return cur

        # print('remove:', remove('RBBYYYBBRRRBB', 5-2))

        def dfs(cur_str, last, times):
            # print(cur_str, last, times)
            if times >= res[0]:
                return
            if not cur_str:
                if times < res[0]:
                    res[0] = times
                return
            if len(cur_str) == 1 and last.get(cur_str, 0):
                dfs('', {}, times + 2)
            for i in range(len(cur_str)):
                for key in last.keys():
                    if last.get(key) > 0:
                        temp = remove(cur_str[:i] + key + cur_str[i:], begin=i - 2)
                        cur_last = dict(last)
                        cur_last[key] -= 1
                        dfs(temp, cur_last, times + 1)

        dfs(board, h, 0)
        return res[0] if res[0] != 6 else -1

    def findMinStep2(self, board: str, hand: str) -> int:
        def backtrack(board):
            print(board)
            if not board: return 0
            i = 0
            ans = 6
            while i < len(board):
                j = i + 1
                while j < len(board) and board[i] == board[j]: j += 1
                balls = 3 - (j - i)
                if counter[board[i]] >= balls:
                    balls = max(0, balls)
                    counter[board[i]] -= balls
                    ans = min(ans, balls + backtrack(board[:i] + board[j:]))
                    if ans == 2:
                        print('')
                    counter[board[i]] += balls
                i = j
            return ans

        from collections import Counter
        counter = Counter(hand)
        ans = backtrack(board)
        return -1 if ans > 5 else ans


if __name__ == '__main__':
    sol = Solution()
    # print(sol.findMinStep("RRYGGYYRRYGGYYRR", "GGBBB"))
    print(sol.findMinStep2("RRYGGYYRRYGGYYRR", "GGBBB"))
