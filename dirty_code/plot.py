# -*- coding: utf-8 -*-
import pylab
import random


class curve(object):
    """
    一些关于曲线(curve)的具体配置:
    base colors for a figure, cyan(青色),magenta(玫瑰红)
    curveColors = ['red','green','yellow','blue','black','cyan','magenta']
    线条的形状可以有以下几种
    lineStyle=['-','--','-.',':','None',' ','']
    作图点的样式可以有以下几种
    's'(square)即为方形，'p'(pentagon)五角星形,'h'(hexagon)六边形
    'x'x形, D'(diamond)菱形,'d'薄菱形
    makerStyle=['s','p','*','h','H','+','x','D','d']
    """
    numCurve = -1
    markerStyleList = ['s', 'p', '*', '+', 'H', 'h', 'x', 'D', 'd']
    colorsList = ['r', 'g', 'b', 'm', 'y', 'c', 'k']
    lineStyleList = ['-', '--', '-.', ':', 'None', ' ', '']

    def __init__(self, yRange, markerSize=15, label=None, lineWidth=3, xRange=None):
        super(curve, self).__init__()
        if not xRange:
            xRange = list(range(len(yRange)))
        curve.numCurve += 1
        self.xRange = xRange
        self.yRange = yRange
        self.marker = curve.markerStyleList[curve.numCurve % len(curve.markerStyleList)]
        self.markerSize = markerSize
        self.markerFaceColor = curve.colorsList[curve.numCurve % len(curve.colorsList)]
        self.label = label
        self.curveColor = curve.colorsList[(curve.numCurve + 2) % len(curve.colorsList)]
        self.lineWidth = lineWidth
        self.lineStyle = curve.lineStyleList[curve.numCurve % len(curve.lineStyleList)]


class curvePlot(object):
    """
    一些关于figure(整个画幅)的基本配置:
    'figsize' : (6,8),
    'axis': [0,10,0,10],   #分别表示x轴和y轴的范围
    'title' : 'hello title',
    'xlabel' : 'hello xlabel',
    'ylabel' : 'hello ylabel',
    'grid' : True,
    'xaxis_locator' : 0.5, #规定了X轴每一格的宽度,这样的话x轴一格的宽度就为0.5
    'yaxis_locator' : 0.5,   #规定了Y轴每一格的宽度
    'legend_loc' : 'best'  #规定了图例的位置,总共可以有'best’,‘upper right’, ‘upper left’, ‘center’, ‘lower left’, ‘lower right’，这5中图例的摆放方式

    一些关于曲线(curve)的具体配置:
    base colors for a figure, cyan(青色),magenta(玫瑰红)
    curveColors = ['red','green','yellow','blue','black','cyan','magenta']
    线条的形状可以有以下几种
    lineStyle=['-','--','-.',':','.',' ','']
    作图点的样式可以有以下几种
    's'(square)即为方形，'p'(pentagon)五角星形,'h'(hexagon)六边形
    'x'x形, D'(diamond)菱形,'d'薄菱形
    makerStyle=['s','p','*','h','H','+','x','D','d']
    """

    def __init__(self, xLim=[0, 10], yLim=[0, 10], figsize=(6, 8), title='hello title',
                 xlabel='hello xlabel', ylabel='hello ylabel', isGrid=True,
                 xaxis_locator=1, yaxis_locator=1, legend_loc='best'):
        super(curvePlot, self).__init__()
        self.curveList = []
        self.curveId = 0
        self.legendLoc = legend_loc

        # 重新另起一幅图
        pylab.figure(figsize=figsize)
        # 画幅--figure的基本配置
        pylab.xlim(xLim)
        pylab.ylim(yLim)
        pylab.title(title, fontsize=50)
        pylab.xlabel(xlabel, fontsize=30)
        pylab.ylabel(ylabel, fontsize=30)
        pylab.grid(isGrid)
        ax = pylab.gca()
        ax.xaxis.set_major_locator(pylab.MultipleLocator(xaxis_locator))
        ax.yaxis.set_major_locator(pylab.MultipleLocator(yaxis_locator))
        # 曲线的可选选项
        self.curveColorsList = ['r', 'g', 'y', 'b', 'k', 'c', 'm']
        self.lineStyleList = ['-', '--', '-.', ':', '.', ' ', '']
        self.makerStyleList = ['s', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd']

        # 曲线curve的具体配置在添加曲线的时候取得

    def addCurve(self, curve):
        self.curveId += 1
        self.curveList.append(curve)
        print('this curve id is', str(self.curveId - 1))

    def removeCurve(self, removeId):
        self.curveList.remove(self.curveList[removeId])
        print('the removed curveId is', removeId, 'now the curveList length is ', len(self.curveList))

    def plotSingleCurve(self, curve):
        pylab.plot(curve.xRange, curve.yRange, marker=curve.marker, color=curve.curveColor,
                   markerfacecolor=curve.markerFaceColor,
                   label=curve.label, linewidth=curve.lineWidth, linestyle=curve.lineStyle)
        pylab.legend(loc=self.legendLoc, fontsize=10)

    def plotMultipleCurve(self):
        for i in range(len(self.curveList)):
            pylab.plot(self.curveList[i].xRange, self.curveList[i].yRange, marker=self.curveList[i].marker,
                       color=self.curveList[i].curveColor, markerfacecolor=self.curveList[i].markerFaceColor,
                       ms=self.curveList[i].markerSize, label=self.curveList[i].label,
                       linewidth=self.curveList[i].lineWidth,
                       linestyle=self.curveList[i].lineStyle)
        pylab.legend(loc=self.legendLoc, fontsize=10)

    def show(self):
        pylab.show()


class bar(object):
    """
    利用bar绘制条形图，条形图与直方图hist的不同在于，条形图bar横坐标可以不是连续的，而 直方图一般是连续的
    """
    numBar = -1
    colorsList = ['r', 'g', 'b', 'm', 'y', 'c', 'k']

    def __init__(self, xRange, yRange, width, legend=None, yerr=None):  # xerr, yerr 暂时未指定
        super(bar, self).__init__()
        bar.numBar += 1
        self.xRange = xRange
        self.yRange = yRange
        self.width = width
        self.legend = legend
        self.yerr = yerr
        self.barColor = bar.colorsList[(bar.numBar) % len(bar.colorsList)]


class barPlot(object):
    """docstring for barPlot"""

    def __init__(self, xLim=[0, 10], yLim=[0, 10], figsize=(6, 8), title='hello title',
                 xlabel='hello xlabel', ylabel='hello ylabel', xticks=None, isGrid=True,
                 xaxis_locator=1, yaxis_locator=1, legend_loc='best'):
        super(barPlot, self).__init__()

        self.barList = []
        self.barId = 0
        self.plotBarList = []
        self.legendLoc = legend_loc

        # 重新另起一幅图
        pylab.figure(figsize=figsize)
        # 画幅--figure的基本配置
        pylab.xlim(xLim)
        pylab.ylim(yLim)
        pylab.title(title, fontsize=50)
        pylab.xlabel(xlabel, fontsize=30)
        pylab.ylabel(ylabel, fontsize=30)
        pylab.grid(isGrid)
        ax = pylab.gca()
        ax.xaxis.set_major_locator(pylab.MultipleLocator(xaxis_locator))
        ax.yaxis.set_major_locator(pylab.MultipleLocator(yaxis_locator))
        self.xticks = xticks

    def addbar(self, bar):
        self.barId += 1
        self.barList.append(bar)
        print('this bar id is', str(self.barId - 1))

    def removebar(self, removeId):
        self.barList.remove(self.barList[removeId])
        print('the removed barId is', removeId, 'now the barList length is ', len(barList))

    def plotSingleBar(self, bar):
        ba = pylab.bar(left=bar.xRange, height=bar.yRange, width=bar.width, color=bar.barColor, yerr=bar.yerr)
        if self.xticks:
            pylab.xticks([bar.xRange[j] + bar.width / 2 for j in range(len(bar.xRange))],
                         self.xticks, fontsize=30)
        barLegend = [bar.legend]
        pylab.legend((ba), barLegend, loc=self.legendLoc, fontsize=10)

    def plotMultipleBar(self):
        for i in range(len(self.barList)):
            self.plotBarList.append(pylab.bar(left=self.barList[i].xRange, height=self.barList[i].yRange,
                                              width=self.barList[i].width, color=self.barList[i].barColor,
                                              yerr=self.barList[i].yerr))
        if self.xticks:
            pylab.xticks(
                [self.barList[i].xRange[j] + self.barList[i].width / 3 for j in range(len(self.barList[i].xRange))],
                self.xticks, fontsize=30)
        allBarLegend = [self.barList[i].legend for i in range(len(self.barList))]
        pylab.legend(self.plotBarList, allBarLegend, loc=self.legendLoc, fontsize=10)

    def show(self):
        pylab.show()


class scatter(object):
    """
    指定x，y的范围，利用area指定散点图的点大小，label用来指定图例的样式。
    scatter和curve类似，利用label指定图例的大小，而bar不同是直接用legend，所以底层封装不同
    """
    numScatter = -1
    colorsList = ['r', 'g', 'b', 'm', 'y', 'c', 'k']
    makerStyleList = ['s', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd']

    def __init__(self, xRange, yRange, area=10, lineWidths=None, label=None):
        super(scatter, self).__init__()
        scatter.numScatter += 1
        self.xRange = xRange
        self.yRange = yRange
        self.lineWidths = lineWidths
        self.scatterColor = scatter.colorsList[(scatter.numScatter) % len(scatter.colorsList)]
        self.scatterMarker = scatter.makerStyleList[(scatter.numScatter) % len(scatter.colorsList)]
        self.area = area
        self.label = label


class scatterPlot(object):
    """docstring for scatterPlot"""

    def __init__(self, xLim=[0, 10], yLim=[0, 10], figsize=(6, 8), title='hello title',
                 xlabel='hello xlabel', ylabel='hello ylabel', isGrid=True,
                 xaxis_locator=1, yaxis_locator=1, legend_loc='best'):
        super(scatterPlot, self).__init__()
        self.scatterList = []
        self.scatterId = 0
        self.plotScatterList = []
        self.legendLoc = legend_loc

        # 重新另起一幅图
        pylab.figure(figsize=figsize)
        # 画幅--figure的基本配置
        pylab.xlim(xLim)
        pylab.ylim(yLim)
        pylab.title(title, fontsize=50)
        pylab.xlabel(xlabel, fontsize=30)
        pylab.ylabel(ylabel, fontsize=30)
        pylab.grid(isGrid)
        ax = pylab.gca()
        ax.xaxis.set_major_locator(pylab.MultipleLocator(xaxis_locator))
        ax.yaxis.set_major_locator(pylab.MultipleLocator(yaxis_locator))

    def addScatter(self, scatter):
        self.scatterId += 1
        self.scatterList.append(scatter)

    def removeScatter(self, removeID):
        self.scatterList.remove(self.scatterList[removeID])

    def plotSingleScatter(self, scatter):
        pylab.scatter(scatter.xRange, scatter.yRange, s=scatter.area, c=scatter.scatterColor,
                      alpha=0.5, linewidths=scatter.lineWidths, label=scatter.label)
        pylab.legend(loc=self.legendLoc, fontsize=10)

    def plotMultipleScatter(self):
        for i in range(len(self.scatterList)):
            pylab.scatter(self.scatterList[i].xRange, self.scatterList[i].yRange,
                          s=self.scatterList[i].area, c=self.scatterList[i].scatterColor,
                          alpha=0.5, linewidths=self.scatterList[i].lineWidths,
                          marker=self.scatterList[i].scatterMarker, label=self.scatterList[i].label)
        pylab.legend(loc=self.legendLoc, fontsize=10)

    def show(self):
        pylab.show()


class barh(object):
    """
    bottom 即为在y轴上面可以被划分的数目
    width  即为在x轴上面的长度
    """
    numBarh = -1
    colorsList = ['r', 'g', 'b', 'm', 'y', 'c', 'k']

    def __init__(self, bottom, width, height, legend=None, xerr=None):  # xerr, yerr 暂时未指定
        super(barh, self).__init__()
        barh.numBarh += 1
        self.bottom = bottom
        self.width = width
        self.height = height
        self.legend = legend
        self.xerr = xerr
        self.barhColor = barh.colorsList[(barh.numBarh) % len(barh.colorsList)]


class barhPlot(object):
    """docstring for barPlot"""

    def __init__(self, xLim=[0, 10], yLim=[0, 10], figsize=(6, 8), title='hello title', left=None,
                 xlabel='hello xlabel', ylabel='hello ylabel', xticks=None, yticks=None, isGrid=True,
                 xaxis_locator=1, yaxis_locator=1, legend_loc='best'):
        super(barhPlot, self).__init__()

        self.barhList = []
        self.barhId = 0
        self.plotBarhList = []
        self.legendLoc = legend_loc

        # 重新另起一幅图
        pylab.figure(figsize=figsize)
        # 画幅--figure的基本配置,left 是y轴整体的位置，表示Barh底的开始位置x=？
        self.left = left
        pylab.xlim(xLim)
        pylab.ylim(yLim)
        pylab.title(title, fontsize=50)
        pylab.xlabel(xlabel, fontsize=30)
        pylab.ylabel(ylabel, fontsize=30)
        pylab.grid(isGrid)
        ax = pylab.gca()
        ax.xaxis.set_major_locator(pylab.MultipleLocator(xaxis_locator))
        ax.yaxis.set_major_locator(pylab.MultipleLocator(yaxis_locator))
        self.yticks = yticks

    def addbarh(self, barh):
        self.barhId += 1
        self.barhList.append(barh)
        print('this barh id is', str(self.barhId - 1))

    def removebar(self, removeId):
        self.barhList.remove(barhList[removeId])
        print('the removed barId is', removeId, 'now the barList length is ', len(barList))

    def plotSingleBarh(self, barh):
        bah = pylab.barh(left=self.left, bottom=barh.bottom, height=barh.height, width=barh.width, color=barh.barhColor,
                         xerr=barh.xerr)
        if self.yticks:
            pylab.yticks([barh.bottom[j] for j in range(len(barh.bottom))],
                         self.yticks, fontsize=30)
        barhLegend = [barh.legend]
        pylab.legend((bah), barhLegend, loc=self.legendLoc, fontsize=10)

    def plotMultipleBarh(self):
        for i in range(len(self.barhList)):
            self.plotBarhList.append(pylab.barh(left=self.left, bottom=self.barhList[i].bottom,
                                                height=self.barhList[i].height, width=self.barhList[i].width,
                                                color=self.barhList[i].barhColor, xerr=self.barhList[i].xerr))
        if self.yticks:
            pylab.yticks([self.barhList[0].bottom[j] for j in range(len(self.barhList[0].bottom))],
                         self.yticks, fontsize=30)
        allBarhLegend = [self.barhList[i].legend for i in range(len(self.barhList))]
        pylab.legend(self.plotBarhList, allBarhLegend, loc=self.legendLoc, fontsize=10)

    def show(self):
        pylab.show()


def main():
    pass

# 画出单个barh的基本配置
# barhh=barh(bottom=[1,2,3,4,5],width=[2,3,4,5,6],height=0.5,legend='222')
# bhPlo=barhPlot(yticks=['12','23','34','45','56'],left=0)
# bhPlo.plotSingleBarh(barhh)
# bhPlo.show()

# 同时画多个barh的用例
# barhh=barh(bottom=[1,2,3,4,5],width=[2,3,4,5,6],height=0.2,legend='222')
# barhh1=barh(bottom=[1.2,2.2,3.2,4.2,5.2],width=[7,7,7,7,7],height=0.2,legend='333')
# bhPlo=barhPlot(yticks=['12','23','34','45','56'],left=0)
# bhPlo.addbarh(barhh)
# bhPlo.addbarh(barhh1)
# bhPlo.plotMultipleBarh()
# bhPlo.show()


# 同时画多个curve的用例
# xRange=list(range(0,5))
# yRange=list(range(2,7))
# cur=curve(yRange=yRange,label='cur')
# X = [ i for i in range(10)]
# Y = [random.randint(1,10) for i in range(10)]
# cur1=curve(yRange=Y,label='cur1')
# cPlot=curvePlot(xLim=[-10,10],yLim=[-2,15])
# cPlot.addCurve(cur)
# cPlot.addCurve(cur1)
# cPlot.plotMultipleCurve()
# cPlot.show()

# 画单个curve的用例
# xRange=list(range(0,5))
# yRange=list(range(2,7))
# cur=curve(xRange=xRange,yRange=yRange,label='cur')
# cPlot=curvePlot(xLim=[-10,10],yLim=[-2,15])
# cPlot.plotSingleCurve(cur)
# cPlot.show()



# 同时画多个bar的用例
# '''
# xticks即为x轴下面的坐标的名字，所以应该和一组bar中X轴数据的个数一致,在pylab.xticks中可以改变xticks摆放的位置
# '''
# ba=bar((1,4),(2,5),width=0.5,legend='233')
# ba1=bar((2,5),(3,7),width=0.5,legend='zzz')
# plo=barPlot(xticks=['G1','G2'])
# plo.addbar(ba)
# plo.addbar(ba1)
# plo.plotMultipleBar()
# plo.show()

# 画单个bar的用例
# '''
# xticks即为x轴下面的坐标的名字，所以应该和一组bar中X轴数据的个数一致,在pylab.xticks中可以改变xticks摆放的位置
# '''
# ba=bar((1,4),(2,5),width=0.5,legend='233')
# plo=barPlot(xticks=['G1','G2'])
# plo.plotSingleBar(ba)
# plo.show()



# 单一散点图的基本配置
# x=[1,2,3,4,5]
# y=[2,3,4,5,6]
# sca=scatter(x,y,area=100,label='hahah')
# sPlo=scatterPlot()
# sPlo.plotSingleScatter(sca)
# sPlo.show()


# 多个散点图的基本配置
# x=[1,2,3,4,5]
# y=[2,3,4,5,6]
# sca=scatter(x,y,area=100,label='11')
# x1=[2,2,2,5,6,7]
# y1=[3,4,5,6,7,8]
# sca1=scatter(x1,y1,area=100,label='22')
# sPlo=scatterPlot()
# sPlo.addScatter(sca)
# sPlo.addScatter(sca1)
# sPlo.plotMultipleScatter()
# sPlo.show()

if __name__ == '__main__':
    main()
