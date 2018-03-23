#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 3/22/18 3:40 PM
# @Author  : Ryan Huang
# @Site    : https://github.com/ryanhuang1014
# @File    : box.py
# @license : Copyright(C), BUPT
# @Contact : ryanhuang1014@gmail.com

import matplotlib.pyplot as plt
import numpy as np


# 箱状图

# 由于箱线图是对单个变量的可视化，其设置很简单。
# x_data 是变量的列表。
# Matplotlib 函数 boxplot() 为 y_data 的每一列或 y_data 序列中的每个向量绘制一个箱线图，
# 因此 x_data 中的每个值对应 y_data 中的一列/一个向量。

def boxplot(x_data, y_data, base_color="#539caf", median_color="#297083", x_label="", y_label="", title=""):
    _, ax = plt.subplots()

    # Draw boxplots, specifying desired style
    ax.boxplot(y_data
               # patch_artist must be True to control box fill
               , patch_artist = True
               # Properties of median line
               , medianprops = {'color': median_color}
               # Properties of box
               , boxprops = {'color': base_color, 'facecolor': base_color}
               # Properties of whiskers
               , whiskerprops = {'color': base_color}
               # Properties of whisker caps
               , capprops = {'color': base_color})

    # By default, the tick label starts at 1 and increments by 1 for
    # each box drawn. This sets the labels to the ones we want
    ax.set_xticklabels(x_data)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)