# -*- coding: utf-8 -*-

from plot_curve import *
import os
import numpy as np
import pandas as pd
from plot_bar import *

#设置图片的画图为黄金比例
fig_width_pt = 246.0
inches_per_pt = 1.0 / 72.27  # Convert pt to inch
golden_mean = (np.sqrt(5) - 1.0) / 2.0  # Aesthetic ratio
fig_width = fig_width_pt * inches_per_pt  # width in inches
fig_height = fig_width * golden_mean  # height in inches
fig_size = [fig_width, fig_height]


bPlot = barPlot(figsize=fig_size, xticks=['query flow', 'short flow', 'long flow'], xLim=[-1, 22], yLim=[0, 40], \
                yaxis_locator=10, xlabel = ' ', ylabel = 'Deadline miss rate (%)', xlabel_fontsize = 12, ylabel_fontsize = 12, \
                xtick_label_fontsize = 10, ytick_label_fontsize = 10, legend_loc = 'best', title = ' ', legend_size=9)

bar_baseline = bar(width=1.2, xRange=(1, 8, 15), yRange=(30, 20, 3), label='TCP', barColor='#1b9e77')
bar_mptcp = bar(width=1.2, xRange=(2.2, 9.2, 16.2), yRange=(20, 8, 0), label='MPTCP', barColor='#d95f02')
bar_dmtcp = bar(width=1.2, xRange=(3.4, 10.4, 17.4), yRange=(3, 2, 0), label='DMTCP', barColor='#7570b3')

bPlot.addbar(bar_baseline)
bPlot.addbar(bar_mptcp)
bPlot.addbar(bar_dmtcp)

bPlot.plotMultipleBar()
bPlot.saveFigure('big-topo-miss-deadline')
bPlot.show()