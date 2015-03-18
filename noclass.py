#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import numpy as np

from data import (
    Instance,
    LookupInstance,
)


def run():
    print 'Loading all instances...'
    nb_sg = 420
    instances = LookupInstance()
    start = time.time()

    print 'Whole annealing: ', (time.time() - start)

if __name__ == '__main__':
    # run()
    a = [1 for i in xrange(1000)]
    b = np.array(a)
    s = time.time()
    for x in xrange(1000):
        c = [2 * i for i in a]
    print 'list: ', (time.time() - s)
    s = time.time()
    for x in xrange(1000):
        c = [2 * i for i in b]
    print 'numpy: ', (time.time() - s)
