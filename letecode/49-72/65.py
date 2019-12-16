#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2019-11-05 10:00
"""
"""验证给定的字符串是否可以解释为十进制数字。

例如:

"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。这里给出一份可能存在于有效十进制数字中的字符列表：

数字 0-9
指数 - "e"
正/负号 - "+"/"-"
小数点 - "."
当然，在输入中，这些字符的上下文也很重要。

更新于 2015-02-10:
C++函数的形式已经更新了。如果你仍然看见你的函数接收 const char * 类型的参数，请点击重载按钮重置你的代码。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution(object):
    def isNumber(self, s):
        """
        有限状态机DFA
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        state = 0
        s = list(s)
        for i in s:
            if state == 0:
                if i == '.':
                    state = 8
                elif '0' <= i <= '9':
                    state = 1
                elif i == '+' or i == '-':
                    state = 7
                else:
                    return False
            elif state == 1:
                if '0' <= i <= '9':
                    state = 1
                elif i == 'e' or i == 'E':
                    state = 4
                elif i == '.':
                    state = 2
                else:
                    return False
            elif state == 2:
                if '0' <= i <= '9':
                    state = 3
                elif i == 'e' or i == 'E':
                    state = 4
                else:
                    return False
            elif state == 3:
                if '0' <= i <= '9':
                    state = 3
                elif i == 'e' or i == 'E':
                    state = 4
                else:
                    return False
            elif state == 4:
                if '0' <= i <= '9':
                    state = 6
                elif i == '+' or i == '-':
                    state = 5
                else:
                    return False
            elif state == 5:
                if '0' <= i <= '9':
                    state = 6
                else:
                    return False
            elif state == 6:
                if '0' <= i <= '9':
                    state = 6
                else:
                    return False
            elif state == 7:
                if '0' <= i <= '9':
                    state = 1
                elif i == '.':
                    state = 8
                else:
                    return False
            elif state == 8:
                if '0' <= i <= '9':
                    state = 3
                else:
                    return False
        return state in [1, 2, 3, 6]


if __name__ == '__main__':
    sol = Solution()
    s = '2e0'
    print(sol.isNumber(s))
