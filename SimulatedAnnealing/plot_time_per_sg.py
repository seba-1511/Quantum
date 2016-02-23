#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from graph.plot import (
    multiPlot,
    plotLines,
)

if __name__ == '__main__':
    x = [
        420,
        504,
        588,
        672,
        756,
        840]
    y = [
        6.15,
        7.96,
        9.28,
        13.27,
        13.55,
        14.15,
    ]
    plotLines([[x, y]], title='Average time to solve 5 times',
              xlabel='Nb Subgraphs', ylabel='Time (s)')
