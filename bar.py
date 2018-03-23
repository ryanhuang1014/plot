#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 3/22/18 3:39 PM
# @Author  : Ryan Huang
# @Site    : https://github.com/ryanhuang1014
# @File    : bar.py
# @license : Copyright(C), BUPT
# @Contact : ryanhuang1014@gmail.com

import matplotlib.pyplot as plt
import numpy as np


# 条形图

#在 barplot() 函数中，
# x_data 表示 x 轴上的不同类别，
# y_data 表示 y 轴上的条形高度。
# 误差条形是额外添加在每个条形中心上的线，可用于表示标准差。

def barplot(x_data, y_data, error_data, x_label="", y_label="", title=""):
    _, ax = plt.subplots()
    # Draw bars, position them in the center of the tick mark on the x-axis
    ax.bar(x_data, y_data, color = '#539caf', align = 'center')
    # Draw error bars to show standard deviation, set ls to 'none'
    # to remove line between points
    ax.errorbar(x_data, y_data, yerr = error_data, color = '#297083', ls = 'none', lw = 2, capthick = 2)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)


# 堆叠条形图

#绘制该图的代码与分组条形图有相同的风格，
# 我们循环地遍历每一组，
# 但我们这次在旧的柱体之上而不是旁边绘制新的柱体
def stackedbarplot(x_data, y_data_list, colors, y_data_names="", x_label="", y_label="", title=""):
    _, ax = plt.subplots()
    # Draw bars, one category at a time
    for i in range(0, len(y_data_list)):
        if i == 0:
            ax.bar(x_data, y_data_list[i], color = colors[i], align = 'center', label = y_data_names[i])
        else:
            # For each category after the first, the bottom of the
            # bar will be the top of the last category
            ax.bar(x_data, y_data_list[i], color = colors[i], bottom = y_data_list[i - 1], align = 'center', label = y_data_names[i])
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    ax.legend(loc = 'upper right')


# 分组条形图

#y_data_list 变量现在实际上是一组列表，
# 其中每个子列表代表了一个不同的组。
# 然后我们循环地遍历每一个组，
# 并在 X 轴上绘制柱体和对应的值，
# 每一个分组的不同类别将使用不同的颜色表示。

def groupedbarplot(x_data, y_data_list, colors, y_data_names="", x_label="", y_label="", title=""):
    _, ax = plt.subplots()
    # Total width for all bars at one x location
    total_width = 0.8
    # Width of each individual bar
    ind_width = total_width / len(y_data_list)
    # This centers each cluster of bars about the x tick mark
    alteration = np.arange(-(total_width/2), total_width/2, ind_width)


    # Draw bars, one category at a time
    for i in range(0, len(y_data_list)):
        # Move the bar to the right on the x-axis so it doesn't
        # overlap with previously drawn ones
        ax.bar(x_data + alteration[i], y_data_list[i], color = colors[i], label = y_data_names[i], width = ind_width)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    ax.legend(loc = 'upper right')
