#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/12/9 下午7:56
"""
"""420. 强密码检验器
一个强密码应满足以下所有条件：

由至少6个，至多20个字符组成。
至少包含一个小写字母，一个大写字母，和一个数字。
同一字符不能连续出现三次 (比如 "...aaa..." 是不允许的, 但是 "...aa...a..." 是可以的)。
编写函数 strongPasswordChecker(s)，s 代表输入字符串，如果 s 已经符合强密码条件，则返回0；
否则返回要将 s 修改为满足强密码条件的字符串所需要进行修改的最小步数。

插入、删除、替换任一字符都算作一次修改。"""


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        min_r = 3 - any(c.isupper() for c in password) - any(c.islower() for c in password) - any(
            c.isdigit() for c in password)
        length = len(password)
        if length < 6:
            return max(min_r, 6 - length)
        count = 0
        repeat_count = {1: 0, 2: 0, 3: 0}
        for c, last in zip('.' + password, password + '.'):
            if c != last:
                if count > 2:
                    repeat = count - 2
                    for i in [3, 2, 1]:
                        repeat_count[i] += repeat // i
                        repeat %= i
                count = 0
            count += 1
        if length < 20:
            return max(sum(repeat_count.values()), min_r)
        min_remove = length - 20
        for i in range(1, 4):
            if min_remove > repeat_count[i] * i:
                min_remove -= repeat_count[i] * i
                repeat_count[i] = repeat_count[i] * i
            else:
                repeat_count[i] = (repeat_count[i] * i - min_remove + i - 1) // i + min_remove
                break
        return max(sum(repeat_count.values()), length - 20 + min_r)


if __name__ == '__main__':
    sol = Solution()
    print(sol.strongPasswordChecker("aaa123"))
