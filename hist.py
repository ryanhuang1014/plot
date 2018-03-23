#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 3/22/18 3:38 PM
# @Author  : Ryan Huang
# @Site    : https://github.com/ryanhuang1014
# @File    : hist.py
# @license : Copyright(C), BUPT
# @Contact : ryanhuang1014@gmail.com

import matplotlib.pyplot as plt
import numpy as np


# 直方图

#这里有两个步骤需要注意，
# 首先，n_bins 参数控制直方图的箱体数量或离散化程度。
# 更多的箱体或柱体能给我们提供更多的信息，
# 但同样也会引入噪声并使我们观察到的全局分布图像变得不太规则。
# 而更少的箱体将给我们更多的全局信息，
# 我们可以在缺少细节信息的情况下观察到整体分布的形状。
# 其次，cumulative 参数是一个布尔值，它允许我们选择直方图是不是累积的，
# 即选择概率密度函数（PDF）或累积密度函数（CDF）

def histogram(data, n_bins, cumulative=False, x_label = "", y_label = "", title = ""):
    _, ax = plt.subplots()
    ax.hist(data, n_bins = n_bins, cumulative = cumulative, color = '#539caf')
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)


# 两层叠加直方图

#在叠加直方图的代码中，我们需要注意几个问题。
# 首先，我们设定的水平区间要同时满足两个变量的分布。
# 根据水平区间的范围和箱体数，我们可以计算每个箱体的宽度。
# 其次，我们在一个图表上绘制两个直方图，需要保证一个直方图存在更大的透明度。

# Overlay 2 histograms to compare them
def overlaid_histogram(data1, data2, n_bins = 0, data1_name="", data1_color="#539caf", data2_name="", data2_color="#7663b0", x_label="", y_label="", title=""):
    # Set the bounds for the bins so that the two distributions are fairly compared
    max_nbins = 10
    data_range = [min(min(data1), min(data2)), max(max(data1), max(data2))]
    binwidth = (data_range[1] - data_range[0]) / max_nbins


    if n_bins == 0:
        bins = np.arange(data_range[0], data_range[1] + binwidth, binwidth)
    else:
        bins = n_bins

    # Create the plot
    _, ax = plt.subplots()
    ax.hist(data1, bins = bins, color = data1_color, alpha = 1, label = data1_name)
    ax.hist(data2, bins = bins, color = data2_color, alpha = 0.75, label = data2_name)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    ax.legend(loc = 'best')