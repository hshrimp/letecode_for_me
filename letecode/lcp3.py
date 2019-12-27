#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-12-27 11:02
"""
"""力扣团队买了一个可编程机器人，机器人初始位置在原点(0, 0)。小伙伴事先给机器人输入一串指令command，机器人就会无限循环这条指令的步骤进行移动。指令有两种：

U: 向y轴正方向移动一格
R: 向x轴正方向移动一格。
不幸的是，在 xy 平面上还有一些障碍物，他们的坐标用obstacles表示。机器人一旦碰到障碍物就会被损毁。

给定终点坐标(x, y)，返回机器人能否完好地到达终点。如果能，返回true；否则返回false。

示例 1：

输入：command = "URR", obstacles = [], x = 3, y = 2
输出：true
解释：U(0, 1) -> R(1, 1) -> R(2, 1) -> U(2, 2) -> R(3, 2)。
示例 2：

输入：command = "URR", obstacles = [[2, 2]], x = 3, y = 2
输出：false
解释：机器人在到达终点前会碰到(2, 2)的障碍物。
示例 3：

输入：command = "URR", obstacles = [[4, 2]], x = 3, y = 2
输出：true
解释：到达终点后，再碰到障碍物也不影响返回结果。
 
限制：

2 <= command的长度 <= 1000
command由U，R构成，且至少有一个U，至少有一个R
0 <= x <= 1e9, 0 <= y <= 1e9
0 <= obstacles的长度 <= 1000
obstacles[i]不为原点或者终点

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/programmable-robot
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def robot(self, command: str, obstacles, x: int, y: int) -> bool:
        p = [0, 0]
        while p[0] <= x and p[1] <= y:
            for c in command:
                if c == 'U':
                    p[1] += 1
                else:
                    p[0] += 1
                if p in obstacles:
                    return False
                if p == [x, y]:
                    return True
        return False

    def robot2(self, command: str, obstacles, x: int, y: int) -> bool:
        p = [0, 0]
        road = set()
        road.add((0, 0))
        for c in command:
            if c == 'U':
                p[1] += 1
            else:
                p[0] += 1
            road.add((p[0], p[1]))
            if p in obstacles:
                return False
            if p == [x, y]:
                return True
        a, b = divmod(x, p[0])
        node = (b, y - a * p[1])
        s = set()
        for t in obstacles:
            if t[0] > x:
                continue
            i, j = divmod(t[0], p[0])
            s.add((j, t[1] - i * p[1]))
        temp = s.intersection(road)
        if len(temp) > 0:
            return False
        elif node in road:
            return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    # command = "URRURRR"
    # obstacles = [[7, 7], [0, 5], [2, 7], [8, 6], [8, 7], [6, 5], [4, 4], [0, 3], [3, 6]]
    # x = 4915
    # y = 1966
    command = "URR"
    obstacles = [[4, 2]]
    x = 3
    y = 2
    print(sol.robot2(command, obstacles, x, y))
