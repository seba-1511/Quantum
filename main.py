#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from graph.plot import (
    plot,
    multiPlot,
    plotLines,
)
from data import (
    Instance,
    Solution,
)

if __name__ == '__main__':
    data = Instance(nb_sg=840, id=199)
    print 'Cost of config:', data.get_cost(data.config)
    print 'Real optimal: ', data.min_cost
    data = Instance(id=199)
    print 'Cost of config:', data.get_cost(data.config)
    print 'Real optimal: ', data.min_cost
    data = Instance(nb_sg=520, id=199)
    print 'Cost of config:', data.get_cost(data.config)
    print 'Real optimal: ', data.min_cost
    Sol = Solution(data)
