#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/4 上午9:03
"""
"""155. 最小栈
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。
 
示例:

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
 
提示：

pop、top 和 getMin 操作总是在 非空栈 上调用。"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = []
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min:
            self.min.append(x)
        else:
            for i in range(len(self.min)):
                if x < self.min[i]:
                    self.min.insert(i, x)
                    return
            else:
                self.min.append(x)

    def pop(self) -> None:
        if self.stack:
            num = self.stack.pop()
            self.min.remove(num)

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min[0] if self.min else None


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = []
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min:
            self.min.append(x)
        else:
            self.min.append(min(self.min[-1], x))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min[-1] if self.min else None
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
