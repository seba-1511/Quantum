#-*- coding: utf-8 -*-
import matplotlib.pyplot as uniquePyPlot
from pdb import set_trace as debug


def plot(x, y, title='', xlabel='', ylabel=''):
    uniquePyPlot.clf()
    figure = uniquePyPlot
    figure.scatter(x, y)
    figure.title(title)
    figure.xlabel(xlabel)
    figure.ylabel(ylabel)
    figure.autoscale(tight=True)
    figure.grid()
    figure.savefig(title + '.png', format='png')


def multiPlot(plotArray, title='', xlabel='', ylabel=''):
    """
        plotArray is of the form: [[X1, Y1], [X2, Y2]]
        Where Xi, Yi are arrays of of the values to plot.
    """
    uniquePyPlot.clf()
    figure = uniquePyPlot
    figure.title(title)
    figure.xlabel(xlabel)
    figure.ylabel(ylabel)
    markers = '+,.1234'
    colors = 'rbgyo'
    if len(plotArray) > 5:
        print 'More than 5 plots given as parameters (plotArray)'
        return False
    for i, (Xi, Yi) in enumerate(plotArray):
        figure.scatter(
            Xi,
            Yi,
            marker=markers[i],
            c=colors[i]
        )
    figure.autoscale(tight=True)
    figure.grid()
    figure.savefig(title + '.png', format='png')


def plotLines(plotArray, title='', xlabel='', ylabel=''):
    """
        plotArray is of the form: [[X1, Y1], [X2, Y2]]
        Where Xi, Yi are arrays of of the values to plot.
    """
    uniquePyPlot.clf()
    figure = uniquePyPlot
    figure.title(title)
    figure.xlabel(xlabel)
    figure.ylabel(ylabel)
    markers = '+,.1234'
    colors = 'rbgyo'
    if len(plotArray) > 5:
        print 'More than 5 plots given as parameters (plotArray)'
        return False
    for i, (Xi, Yi) in enumerate(plotArray):
        figure.plot(
            Xi,
            Yi,
            marker=markers[i],
            c=colors[i]
        )
    figure.autoscale(tight=True)
    figure.grid()
    figure.savefig(title + '.png', format='png')

if __name__ == '__main__':
    x = [i for i in xrange(10)]
    y = [i**2 for i in xrange(10)]
    x1 = [i for i in xrange(10)]
    y2 = [i**3 for i in xrange(10)]
    x3 = [i for i in xrange(10)]
    y3 = [i*3 for i in xrange(10)]
    plotLines([[x, y],[x1, y2],[x3, y3],], title="test")
