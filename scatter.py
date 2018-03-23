#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 3/22/18 3:36 PM
# @Author  : Ryan Huang
# @Site    : https://github.com/ryanhuang1014
# @File    : scatter.py
# @license : Copyright(C), BUPT
# @Contact : ryanhuang1014@gmail.com

import matplotlib.pyplot as plt
import numpy as np

# 散点图

#我们首先将 Matplotlib 的 pyplot 导入为 plt，
# 并调用函数 plt.subplots() 来创建新的图。
# 我们将 x 轴和 y 轴的数据传递给该函数，然后将其传递给 ax.scatter() 来画出散点图。
# 我们还可以设置点半径、点颜色和 alpha 透明度，甚至将 y 轴设置为对数尺寸，最后为图指定标题和坐标轴标签。

def scatterplot(x_data, y_data, x_label="", y_label="", title="", color = "r", yscale_log=False):

    # Create the plot object
    _, ax = plt.subplots()

    # Plot the data, set the size (s), color and transparency (alpha)
    # of the points
    ax.scatter(x_data, y_data, s = 10, color = color, alpha = 0.75)

    if yscale_log == True:
        ax.set_yscale('log')

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)