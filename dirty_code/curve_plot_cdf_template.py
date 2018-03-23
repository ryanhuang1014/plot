# -*- coding: utf-8 -*-
from plot_curve import *
import os
import numpy as np
import statsmodels.api as sm

######################不能直接运行##################

#设置了figure的尺寸，为黄金比例
fig_width_pt = 246.0
inches_per_pt = 1.0 / 72.27  # Convert pt to inch
golden_mean = (np.sqrt(5) - 1.0) / 2.0  # Aesthetic ratio
fig_width = fig_width_pt * inches_per_pt  # width in inches
fig_height = fig_width * golden_mean  # height in inches
fig_size = [fig_width, fig_height]
print (fig_size)

#利用os模块，在操作实际文件
UNDER_DIR = os.listdir(".")
DIR_NAME = [dir_name for dir_name in UNDER_DIR if os.path.isdir(dir_name)]
DIR_NAME.remove('.idea')
DIR_NAME.remove('pic')

FLOW_1 = []
FLOW_2 = []
FLOW_4 = []
FLOW_10 = []
FLOW_16 = []

for dir in DIR_NAME:
    if 'shortflow_CDF_1_' in dir:
        FLOW_1.append(dir)
    elif 'shortflow_CDF_2_' in dir:
        FLOW_2.append(dir)
    elif 'shortflow_CDF_4_' in dir:
        FLOW_4.append(dir)
    elif 'shortflow_CDF_10_' in dir:
        FLOW_10.append(dir)
    elif 'shortflow_CDF_16_' in dir:
        FLOW_16.append(dir)

def get_protocol_index(protocl_name):
    if protocl_name == 'mptcp':
        return 0
    elif protocl_name == 'dmtcp':
        return 1
    elif protocl_name == 'baseline':
        return 2
    else:
        return None


def plot_cdf(dir_names):
    #cPlot是plot_curve中的总体坐标的配置
    cPlot = curvePlot(legend_size=6, figsize=fig_size, xLim=[0, 140], yLim=[0, 1.001], xaxis_locator=20, yaxis_locator=0.2, \
                      xlabel='Flow Completion time(ms)', ylabel='CDF', xlabel_fontsize=12, ylabel_fontsize=12, \
                      xtick_label_fontsize=10, ytick_label_fontsize=10, legend_loc='lower right', title=' ')
    FCT_LIST = []
    MARKER_STYLE_LIST = ['*', 'o', 'p']
    MARKER_COLOR_LIST = ['#1b9e77', '#d95f02', '#7570b3']
    LINE_STYLE_LIST = ['-', '--', '-.']
    LINE_COLOR_LIST = ['#1f78b4', '#33a02c', '#fb9a99']
    for dir in dir_names:
        dir_tmp = dir.split('_')
        protocol = dir_tmp[0]

        #利用numpy来载入一列的文件
        fct_item = np.loadtxt(dir+'/flow.tr', delimiter=' ', usecols=(2,), dtype=float)
        FCT_LIST.append(fct_item)

        #利用sm包，使用fct_item来cdf
        ecdf = sm.distributions.ECDF(fct_item)
        x = np.linspace(min(fct_item), max(fct_item), len(fct_item)/5)
        y = list(ecdf(x))

        #把时间转化为毫秒
        x = x*1000
        x = list(x)
        print max(x), max(y), x, y

        index = get_protocol_index(protocol)
        if protocol == 'baseline':
            protocol = 'TCP'
        elif protocol == 'mptcp':
            protocol = 'MPTCP'
        elif protocol == 'dmtcp':
            protocol = 'DMTCP'
        else:
            protocol = None
    #cur_tmp是曲线的本身
        cur_tmp = curve(xRange=x, yRange=y, label=protocol, lineWidth=2, lineStyle=LINE_STYLE_LIST[index], \
                        lineColor=LINE_COLOR_LIST[index], markerSize=8, markerStyle=MARKER_STYLE_LIST[index], markerColor=MARKER_COLOR_LIST[index])
        cPlot.addCurve(cur_tmp)
    cPlot.plotMultipleCurve()
    cPlot.saveFigure('4-packet-fct-cdf')
    cPlot.show()

plot_cdf(FLOW_4)

# fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharex=False, sharey=False)
# fct_item = np.loadtxt('mptcp_shortflow_CDF_1_0.8_small/flow.tr', delimiter=' ', usecols=(2,), dtype=float)
# ecdf = sm.distributions.ECDF(fct_item)
# min_fct = min(fct_item)
# max_fct = max(fct_item)
#
# x = np.linspace(min_fct, max_fct, len(fct_item))
# y = ecdf(x)
# plt.plot(x, y, label='mptcp')
# plt.show()
# print x