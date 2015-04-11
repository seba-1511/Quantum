#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os
import numpy as np
from data import LookupInstance
from graph.plot import (
    plot,
    multiPlot,
    plotLines,
)

if __name__ == '__main__':
    inst = LookupInstance()
    sol = inst.config
    costs = []
    for q in xrange(10):
        for i, o in enumerate(sol):
            cost = 0
            for j, s in enumerate(sol):
                temp = sol[:]
                temp[i] = -1 * temp[i]
                temp[j] = -1 * temp[j]
                cost += inst.get_cost(temp)
                costs.append(cost)

    plotLines([[xrange(10), costs]], title='Area',
              xlabel='Radius', ylabel='Volume')
