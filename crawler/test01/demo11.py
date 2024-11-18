# coding=utf-8
# @File: demo11.py
# @Author: zijier
# @Desc: 
# @Date: 8:55 PM 2024/03/14

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

# 读取图片
n1 = plt.imread('test.jpg')
# n1为三维数组，最高维表示的是图像的高，次高维表示的是图像的宽，最低维[R,G,B]颜色
plt.imshow(n1)
# 编写灰度公式
n2 = np.array([0.299, 0.587, 0.114])
# 将n1数组颜色值与n2数组进行（灰度公式固定值）点成运算
x = np.dot(n1, n2)
# 传入数组，显示灰度
plt.imshow(x, cmap='gray')
# 显示图像
plt.show()
