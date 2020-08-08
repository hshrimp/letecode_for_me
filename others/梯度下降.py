#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/8/3 下午2:55
"""
"""使用梯度下降求函数 𝑓(𝑥,𝑦)=𝑥**2+𝑦**2 的最小值。"""


def get_get_gradient(x, y):
    return 2 * x, 2 * y


def gradient_descent():
    x, y = 5, 22
    e = 0.0001
    learning_rate = 0.01
    while x ** 2 + y ** 2 > e:
        grad = get_get_gradient(x, y)
        print('learning_rate * grad[0]:', learning_rate * grad[0], 'learning_rate * grad[1]:', learning_rate * grad[1])
        x = x - learning_rate * grad[0]
        y = y - learning_rate * grad[1]
    return x, y, x ** 2 + y ** 2


if __name__ == '__main__':
    print(gradient_descent())
