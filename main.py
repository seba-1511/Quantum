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
    print 'Timing: ', data.timing
    data = Instance(id=199)
    print 'Cost of config:', data.get_cost(data.config)
    print 'Real optimal: ', data.min_cost
    print 'Timing: ', data.timing
    data = Instance(nb_sg=504, id=199)
    print 'Cost of config:', data.get_cost(data.config)
    print 'Real optimal: ', data.min_cost
    print 'Timing: ', data.timing
    Sol = Solution(data)
