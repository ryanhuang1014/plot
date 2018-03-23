#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 3/22/18 3:37 PM
# @Author  : Ryan Huang
# @Site    : https://github.com/ryanhuang1014
# @File    : line.py
# @license : Copyright(C), BUPT
# @Contact : ryanhuang1014@gmail.com

import matplotlib.pyplot as plt
import numpy as np


# 折线图
# 线图的实现代码，和散点图的代码结构很相似，只在变量设置上有少许变化

def lineplot(x_data, y_data, x_label="", y_label="", title=""):
    # Create the plot object
    _, ax = plt.subplots()

    # Plot the best fit line, set the linewidth (lw), color and
    # transparency (alpha) of the line
    ax.plot(x_data, y_data, lw = 2, color = '#539caf', alpha = 1)

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
