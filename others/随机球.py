#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/7/29 上午10:33
"""
import random
import numpy as np
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d.axes3d import Axes3D


def ramdom_circle():
    """
    随机在圆周上取点
    思路：以原点为圆心，半径为1的圆，随机生成x,y，伸缩x ** 2 + y ** 2到长度为1
    :return:
    """
    x = np.array([random.uniform(-1, 1) for _ in range(1000)])
    y = np.array([random.uniform(-1, 1) for _ in range(1000)])
    z = 1 / (np.sqrt(x ** 2 + y ** 2))
    x1 = x * z
    y1 = y * z
    plot.figure(figsize=(6, 6))
    plot.plot(x1, y1, 'r.')
    plot.show()


def ramdom_area_circle():
    """
    随机在圆面上取点
    思路：随机生成x,y，把x ** 2 + y ** 2>1的x,y去掉。就是落在圆外的点去掉。
    :return:
    """
    x = np.array([random.uniform(-1, 1) for _ in range(2000)])
    y = np.array([random.uniform(-1, 1) for _ in range(2000)])
    x1 = np.array([i for i, j in zip(x, y) if i ** 2 + j ** 2 <= 1])
    y1 = np.array([j for i, j in zip(x, y) if i ** 2 + j ** 2 <= 1])
    plot.figure(figsize=(6, 6))
    plot.plot(x1, y1, 'r.')


def ramdom_ball():
    """
    随机在球面上取点
    思路：由圆周的思路引申，伸缩x ** 2 + y ** 2 + z ** 2到长度为1
    :return:
    """
    x = np.array([random.uniform(-1, 1) for _ in range(1000)])
    y = np.array([random.uniform(-1, 1) for _ in range(1000)])
    z = np.array([random.uniform(-1, 1) for _ in range(1000)])
    p = 1 / (np.sqrt(x ** 2 + y ** 2 + z ** 2))
    x1 = x * p
    y1 = y * p
    z1 = z * p
    fig = plot.figure(figsize=(6, 6))
    axes3d = Axes3D(fig)
    axes3d.scatter(x1, y1, z1)
    plot.show()


def ramdom_area_ball():
    """
    随机在球体内取点
    思路：由圆面的思路引申，将落在球外的点去掉。
    :return:
    """
    x = np.array([random.uniform(-1, 1) for _ in range(15000)])
    y = np.array([random.uniform(-1, 1) for _ in range(15000)])
    z = np.array([random.uniform(-1, 1) for _ in range(15000)])
    x1 = np.array([i for i, j, k in zip(x, y, z) if i ** 2 + j ** 2 + k ** 2 <= 1])
    y1 = np.array([j for i, j, k in zip(x, y, z) if i ** 2 + j ** 2 + k ** 2 <= 1])
    z1 = np.array([k for i, j, k in zip(x, y, z) if i ** 2 + j ** 2 + k ** 2 <= 1])

    fig = plot.figure(figsize=(6, 6))
    axes3d = Axes3D(fig)
    axes3d.scatter(x1, y1, z1)
    plot.show()


if __name__ == '__main__':
    ramdom_circle()
    ramdom_area_circle()
    ramdom_ball()
    ramdom_area_ball()
