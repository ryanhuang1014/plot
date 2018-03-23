# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Ryan Huang
# Time: 2016/11/24
#

import pylab
import random


class curve(object):
    """

    一些关于曲线(curve)的具体配置:
    1) Ｘ坐标的范围，即xRange

    2) Ｙ坐标的范围，即yRange

    3) 线条line的颜色，即lineColor. 可以有以下几种
      cyan(青色),magenta(玫瑰红)
        colorsList = ['red','green','yellow','blue','black','cyan','magenta']

    4) 线条line连线的形状，即lineStyle. 可以有以下几种
        lineStyle=['-','--','-.',':','None',' ','']

    5) 线条line的宽度，即linewidth

    6) 作图点的样式,即markerStyle. 可以有以下几种
        's'(square)即为方形，'p'(pentagon)五角星形,'h'(hexagon)六边形
        'x'x形, D'(diamond)菱形,'d'薄菱形
        makerStyle=['s','p','*','h','H','+','x','D','d']

    7) 坐标点的样式的大小，即 markerSize

    8) 坐标点的样式的颜色，即 markerColor

    9) 本条curve在最后的多条curve组成的图案中的图例，即 label

    所有的object共分为3层，marker, line ==>curve;  curve, 坐标的一些参数 ==> figure
    """
    numCurve = -1
    lineStyleList = ['-', '--', '-.', ':', 'None', ' ', '']
    colorsList = ['r', 'g', 'b', 'm', 'y', 'c', 'k']
    markerStyleList = ['s', 'p', '*', '+', 'H', 'h', 'x', 'D', 'd']

    def __init__(self, xRange=None, yRange=None, \
                 lineColor=None, lineStyle=None, lineWidth=None, \
                 markerStyle=None, markerSize=None, markerColor=None, \
                 label=None):

        super(curve, self).__init__()
        if yRange:
            self.yRange = yRange
        else:
            raise IOError

        if xRange:
            self.xRange = xRange
        else:
            self.xRange = list(range(len(yRange)))

        if len(xRange) != len(yRange):
            raise IOError

        if lineColor:
            self.lineColor = lineColor
        else:
            self.lineColor = curve.colorsList[(curve.numCurve + 2) % len(curve.colorsList)]

        if lineWidth:
            self.lineWidth = lineWidth
        else:
            self.lineWidth = 3

        if lineStyle:
            self.lineStyle = lineStyle
        else:
            self.lineStyle = curve.lineStyleList[(curve.numCurve + 1) % len(curve.lineStyleList)]

        if markerStyle:
            self.markerStyle = markerStyle
        else:
            self.markerStyle = curve.markerStyleList[curve.numCurve % len(curve.markerStyleList)]

        if markerSize:
            self.markerSize = markerSize
        else:
            self.markerSize = 10

        if markerColor:
            self.markerColor = markerColor
        else:
            self.markerColor = curve.colorsList[curve.numCurve % len(curve.colorsList)]

        if label:
            self.label = label
        else:
            self.label = "no label now"

        curve.numCurve += 1


class curvePlot(object):
    """

    一些关于figure(整个画幅)的基本配置:
    1) figure的大小，即figsize
      'figsize' : (6,8)

    2) figure的标题，即title
        'title' : 'hello title'

    3) x轴的名字，即 xlabel
      'xlabel' : 'hello xlabel'

    4) x轴的长度范围，即xlim
      xLim=[0, 10]

    5) x轴每一格的长度，即xaxis_locator
       'xaxis_locator' : 0.5, #规定了x轴每一格的宽度,这样的话x轴一格的宽度就为0.5

    6) y轴的名字，即 ylabel
      'ylabel' : 'hello ylabel'

    7) y轴的长度范围，即ylim
      yLim=[0, 10]

    8) y轴每一格的长度，即yaxis_locator
        'yaxis_locator' : 0.5, #规定了y轴每一格的宽度,这样的话y轴一格的宽度就为0.5

    9) 图例放置的位置，即legend_loc
        'legend_loc' : 'best'  #总共可以有'best’,‘upper right’, ‘upper left’, ‘center’, ‘lower left’, ‘lower right’，这5个图例的摆放方式

    10) 是否在图中启用背景网状虚线，即grid
      'grid' : True,


    一些关于曲线(curve)的具体配置:
    base colors for a figure, cyan(青色),magenta(玫瑰红)
    colorsList = ['red','green','yellow','blue','black','cyan','magenta']
    线条的形状可以有以下几种
    lineStyle=['-','--','-.',':','.',' ','']
    作图点的样式可以有以下几种
    's'(square)即为方形，'p'(pentagon)五角星形,'h'(hexagon)六边形
    'x'x形, D'(diamond)菱形,'d'薄菱形
    makerStyle=['s','p','*','h','H','+','x','D','d']
    """

    def __init__(self, figsize=None, \
                 title=None, \
                 xlabel=None, xLim=None, xlabel_fontsize=None, xtick_label_fontsize=None, xaxis_locator=None, \
                 ylabel=None, yLim=None, ylabel_fontsize=None, ytick_label_fontsize=None, yaxis_locator=None, \
                 legend_loc=None, legend_size=None, isGrid=None):

        super(curvePlot, self).__init__()
        self.curveList = []
        self.curveId = 0

        # 重新另起一幅图
        if figsize:
            pylab.figure(figsize=figsize)
        else:
            pylab.figure(figsize=(6, 8))
        # 画幅--figure的基本配置
        if title:
            pylab.title(title, fontsize=10)
        else:
            pylab.title('no title now', fontsize=10)

        if xlabel and xlabel_fontsize:
            pylab.xlabel(xlabel, fontsize=xlabel_fontsize)
        else:
            pylab.xlabel('no xlabel now or no xlabel_fontsize', fontsize=5)

        if xtick_label_fontsize:
            pylab.xticks(fontsize=xtick_label_fontsize)
        else:
            pylab.xticks(fontsize=5)

        if xLim:
            pylab.xlim(xLim)
        else:
            pylab.xlim([0, 10])

        if xaxis_locator:
            self.xaxis_locator = xaxis_locator
        else:
            self.xaxis_locator = 1

        if ylabel and ylabel_fontsize:
            pylab.ylabel(ylabel, fontsize=ylabel_fontsize)
        else:
            pylab.ylabel('no ylabel now or no ylabel_fontsize', fontsize=5)

        if ytick_label_fontsize:
            pylab.yticks(fontsize=ytick_label_fontsize)
        else:
            pylab.yticks(fontsize=5)

        if yLim:
            pylab.ylim(yLim)
        else:
            pylab.ylim([0, 10])

        if yaxis_locator:
            self.yaxis_locator = yaxis_locator
        else:
            self.yaxis_locator = 1

        if legend_loc:
            self.legend_loc = legend_loc
        else:
            self.legend_loc = 'best'

        if legend_size:
            self.legend_size = legend_size
        else:
            self.legend_size = 5

        if isGrid:
            self.isGrid = isGrid
        else:
            self.isGrid = True

    # 设置在实际有用ax中是否包括网格
        pylab.grid(self.isGrid)
        ax = pylab.gca()
        # ax.set_frame_on(False)

    #设置一个figure中，有用的坐标图在一个完整figure中的位置
        ax.set_position([0.18, 0.2, 0.77, 0.77])
    #设置xaxis_locator和yaxis_locator中，ｘ轴和ｙ轴上每格的间隔距离
        ax.xaxis.set_major_locator(pylab.MultipleLocator(self.xaxis_locator))
        ax.yaxis.set_major_locator(pylab.MultipleLocator(self.yaxis_locator))

    # 曲线curve的具体配置在添加曲线的时候取得

    def addCurve(self, curve):
        self.curveId += 1
        self.curveList.append(curve)
        print('this curve id is', str(self.curveId - 1))

    def removeCurve(self, removeId):
        self.curveList.remove(self.curveList[removeId])
        print('the removed curveId is', removeId, 'now the curveList length is ', len(self.curveList))

    def plotSingleCurve(self, curve):
        pylab.plot(curve.xRange, curve.yRange, marker=curve.markerStyle, markersize=curve.markerSize,
                   markerfacecolor=curve.markerColor, \
                   color=curve.lineColor, linewidth=curve.lineWidth, linestyle=curve.lineStyle, \
                   label=curve.label)
        pylab.legend(loc=self.legend_loc, prop={'size': self.legend_size})

    def plotMultipleCurve(self):
        for i in range(len(self.curveList)):
            pylab.plot(self.curveList[i].xRange, self.curveList[i].yRange, \
                       marker=self.curveList[i].markerStyle, markersize=self.curveList[i].markerSize,
                       markerfacecolor=self.curveList[i].markerColor, \
                       color=self.curveList[i].lineColor, linewidth=self.curveList[i].lineWidth,
                       linestyle=self.curveList[i].lineStyle, \
                       label=self.curveList[i].label)
        pylab.legend(loc=self.legend_loc, prop={'size': self.legend_size})

    def show(self):
        pylab.show()

    def saveFigure(self, name):
        if name:
            name = name + '.pdf'
            pylab.savefig(name)
        else:
            name = "no name now"
            pylab.savefig(name)


if __name__ == '__main__':
    # 画多个curve的用例
    xRange1 = list(range(1, 6))
    xRange2 = list(range(2, 7))

    xRange = list(range(0, 5))
    yRange = list(range(2, 7))
    cur = curve(xRange=xRange, yRange=yRange, label='cur', markerColor='g', lineColor='g', lineWidth=2, lineStyle=':')
    cur1 = curve(xRange=xRange1, yRange=yRange, label='cur1', markerColor='y', lineColor='y', lineWidth=12)
    cur2 = curve(xRange=xRange2, yRange=yRange, label='cur2', markerColor='cyan', lineColor='y', lineWidth=12)

    cPlot = curvePlot(xLim=[-10, 10], yLim=[-2, 15], xaxis_locator=0.5)
    cPlot.addCurve(cur)
    cPlot.addCurve(cur1)
    cPlot.addCurve(cur2)
    cPlot.plotMultipleCurve()
    cPlot.show()