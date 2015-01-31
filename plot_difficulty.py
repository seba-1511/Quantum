#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os
import numpy as np
from graph.plot import (
    plot,
    multiPlot,
    plotLines,
)

from pdb import set_trace as debug

if __name__ == '__main__':
    timing_file = 'tts_frustratedBonds_loopSize6.txt'
    directory = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(directory, timing_file)
    f = open(directory, 'r')
    timings = f.readlines()
    timings = np.array(map(lambda x: float(x.split()[1]), timings))
    step = 0.001
    x = np.arange(0, timings.max(), step)
    y = [np.sum(timings > i) for i in x]
    plotLines([[x, y]], title='Difficulty',
              xlabel='Time', ylabel='Nb Instances')
