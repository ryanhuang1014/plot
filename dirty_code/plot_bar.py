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

class bar(object):
    """
    利用bar绘制条形图，条形图与直方图hist的不同在于，条形图bar横坐标可以不是连续的，而 直方图一般是连续的

    一些关于曲线(curve)的具体配置:
    1) Ｘ坐标的范围，即xRange

    2) Ｙ坐标的范围，即yRange

    3) width是每条长方形的宽度
    width=0.5

    4) barColor 为每条的颜色
    barColor = 'g'

    5) label 为每个条形图的图示
    label = 'no one'

    6) yerr为在y轴上的误差,一般是在y轴上的最大值和最小值
    yerr = (2, 3, 4, 1, 2)

    7) 如果没有指定每个柱子的ｘ轴坐标，gap才奏效. 在x轴上,不同列的柱组成一组.gap就是这一组柱子的间隔
    gap = 5

    """
    numBar = -1
    colorsList = ['r', 'g', 'b', 'm', 'y', 'c', 'k']

    def __init__(self, xRange=None, yRange=None, width=None, barColor=None, label=None, yerr=None, gap=None):  # xerr, yerr 暂时未指定
        super(bar, self).__init__()

        if width:
            self.width = width
        else:
            self.width = 0.7

        if gap:
            self.gap = gap
        else:
            self.gap = 5

        if yRange:
            self.yRange = yRange
        else:
            raise IOError

        if xRange:
            self.xRange = xRange
        else:
            self.xRange = [i*self.gap + (bar.numBar+1)*self.width  for i in xrange(len(self.yRange))]

        if label:
            self.label = label
        else:
            self.label = 'no label now'

        if yerr:
            self.yerr = yerr
        else:
            self.yerr = None

        if barColor:
            self.barColor = barColor
        else:
            self.barColor = bar.colorsList[(bar.numBar) % len(bar.colorsList)]

        bar.numBar += 1



class barPlot(object):
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
    """

    def __init__(self, figsize=None, \
                  title=None,\
                  xLim=None, xlabel=None, xlabel_fontsize=None, xtick_label_fontsize=None, xaxis_locator=None, xticks=None, \
                  yLim=None, ylabel=None, ylabel_fontsize=None, ytick_label_fontsize=None, yaxis_locator=None, yticks=None, \
                  legend_loc=None, legend_size=None, isGrid=True ):

        super(barPlot, self).__init__()

        self.barList = []
        self.barId = 0
        self.plotBarList = []
        self.legendLoc = legend_loc

        # 重新另起一幅图
        if figsize:
            pylab.figure(figsize=figsize)
        else:
            pylab.figure(figsize=(6, 80))

        # 画幅--figure的基本配置
        if title:
            pylab.title(title, fontsize=50)
        else:
            pylab.title('no title now', fontsize=50)

        if xlabel and xlabel_fontsize:
            pylab.xlabel(xlabel, fontsize=xlabel_fontsize)
        else:
            pylab.xlabel('no xlabel now or no xlabel_fontsize', fontsize=5)

        if xtick_label_fontsize:
            self.xtick_label_fontsize = xtick_label_fontsize
        else:
            self.xtick_label_fontsize = 5

        if xLim:
            pylab.xlim(xLim)
        else:
            pylab.xlim([0, 10])

        if xaxis_locator:
            self.xaxis_locator = xaxis_locator
        else:
            self.xaxis_locator = 1

        if xticks:
            self.xticks = xticks
        else:
            self.xticks = 'no xticks now'

        if ylabel and ylabel_fontsize:
            pylab.ylabel(ylabel, fontsize=ylabel_fontsize)
        else:
            pylab.ylabel('no ylabel now or no ylabel_fontsize', fontsize=5)

        if ytick_label_fontsize:
            self.ytick_label_fontsize = ytick_label_fontsize
        else:
            self.ytick_label_fontsize = None

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
    # 设置一个figure中，有用的坐标图在一个完整figure中的位置
        ax.set_position([0.18,0.15,0.8,0.8])
    # 设置xaxis_locator和yaxis_locator中，ｘ轴和ｙ轴上每格的间隔距离
        ax.xaxis.set_major_locator(pylab.MultipleLocator(self.xaxis_locator))
        ax.yaxis.set_major_locator(pylab.MultipleLocator(self.yaxis_locator))


    def addbar(self, bar):
        self.barId += 1
        self.barList.append(bar)
        print('this bar id is', str(self.barId - 1))

    def removebar(self, removeId):
        self.barList.remove(self.barList[removeId])
        print('the removed barId is', removeId, 'now the barList length is ', len(self.barList))

    def plotSingleBar(self, bar):
        pylab.bar(left=bar.xRange, height=bar.yRange, width=bar.width, color=bar.barColor, label=bar.label, yerr=bar.yerr)
        pylab.xticks([bar.xRange[j] + bar.width / 2 for j in range(len(bar.xRange))], self.xticks, fontsize=30)
        pylab.legend(loc=self.legendLoc, prop={'size': self.legend_size})

    def plotMultipleBar(self):
        for i in range(len(self.barList)):
            # print (self.barList[i].width*i)
            pylab.bar(left=self.barList[i].xRange, height=self.barList[i].yRange, \
                      width=self.barList[i].width, color=self.barList[i].barColor, \
                      label=self.barList[i].label, yerr=self.barList[i].yerr)

            pylab.xticks(
                [self.barList[i].xRange[j] + self.barList[i].width /10 for j in range(len(self.barList[i].xRange))], \
                self.xticks, fontsize=self.xtick_label_fontsize)
            pylab.yticks(fontsize = self.ytick_label_fontsize)

        pylab.legend(loc=self.legendLoc, prop={'size': self.legend_size})

    def show(self):
        pylab.show()

    def saveFigure(self, name):
        if name:
            print name
            name = name + '.pdf'
            pylab.savefig(name)
        else:
            name = "no name now"
            pylab.savefig(name)


if __name__ == '__main__':

    # 同时画多个bar的用例
    # '''
    # xticks即为x轴下面的坐标的名字，所以应该和一组bar中X轴数据的个数一致,在pylab.xticks中可以改变xticks摆放的位置
    # '''
    ba = bar(yRange=(1, 4), width=1, label='233')
    ba1 = bar(yRange=(2, 5), width=1, label='zzz')
    ba2 = bar(yRange=(6, 10), width=1, label='333')

    plo = barPlot(xticks=['G1', 'G2', 'G3'])
    plo.addbar(ba)
    plo.addbar(ba1)
    plo.addbar(ba2)

    plo.plotMultipleBar()
    plo.show()

    #画单个bar的用例
    '''
    xticks即为x轴下面的坐标的名字，所以应该和一组bar中X轴数据的个数一致,在pylab.xticks中可以改变xticks摆放的位置
    '''
    # ba=bar((1,4),(2,5),width=0.5,label='233')
    # plo=barPlot(xticks=['G1','G2'])
    # plo.plotSingleBar(ba)
    # plo.show()