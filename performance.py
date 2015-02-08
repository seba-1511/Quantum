#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
from functools import wraps


def timeit(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        start = time.time()
        res = fn(*args, **kwargs)
        end = time.time()
        print "@timeit: " + fn.func_name + " took " + str(end - start) + " seconds"
        return res
