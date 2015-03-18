#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time

from data import (
    Instance,
    LookupInstance,
)


print 'Loading all instances...'
nb_sg = 420
instances = LookupInstance()
start = time.time()

print 'Whole annealing: ', (time.time() - start)
