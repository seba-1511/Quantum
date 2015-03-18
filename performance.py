#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
from functools import wraps
import cProfile
import pstats


def timeit(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        start = time.time()
        res = fn(*args, **kwargs)
        end = time.time()
        name = fn.func_name
        print "@timeit: " + name + " took " + str(end - start) + " seconds"
        return res
    return measure_time


def profile(fn):
    @wraps(fn)
    def measure_perf(*args, **kwargs):
        prof = Profiler()
        prof.start()
        res = fn(*args, **kwargs)
        prof.stop()
        prof.score()
        return res
    return measure_perf


class Profiler():

    def __init__(self):
        self.prof = cProfile.Profile()

    def start(self):
        self.prof.enable()

    def stop(self):
        self.prof.disable()

    def score(self):
        ps = pstats.Stats(self.pr).sort_stats('cumulative')
        ps.print_stats()
