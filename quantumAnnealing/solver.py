#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import numpy as np
from time import time
from performance import Profiler
from runge_kutta import (
    RK,
    SparseRK,
    dot_vec_vec,
)
from annealer import (
    driver_matrix,
    add_sparse,
    dot_scal_sparse,
    dot_sparse_vec,
)
from data import (
    load_instance,
    generate_instance,
    inst_0,
    inst_1,
)


def linear_schedule():
    A = lambda t: 1.0 - t / T
    B = lambda t: t / T
    return (A, B)


def new_schedule():
    A = lambda t: 1.0 - t * 2 / T
    B = lambda t: t * 2 / T
    return (A, B)

if __name__ == '__main__':
    # p = Profiler()
    # p.start()
    NB_QUBITS = 6
    NB_ENTRIES = 2 ** NB_QUBITS
    epsilon = 1e-6
    T = 20.00002
    A, B = linear_schedule()

    H_p = generate_instance(NB_ENTRIES)
    H_d = driver_matrix(NB_ENTRIES, load=True)

    # H = lambda t: add_sparse(
        # dot_scal_sparse(A(t), H_d),
        # dot_scal_sparse(B(t), H_p)
    #)
    # F = lambda t: dot_scal_sparse(1j, H(t))

    H_p = dot_scal_sparse(1j, H_p)
    H_d = dot_scal_sparse(1j, H_d)

    F = lambda t: add_sparse(
        dot_scal_sparse(A(t), H_d),
        dot_scal_sparse(B(t), H_p)
    )

    y_dot = SparseRK(F)
    init = [1 / math.sqrt(NB_ENTRIES)] * NB_ENTRIES
    dt = 0.001
    t = 0

    profile = 0
    if profile:
        p = Profiler()
        p.start()
    start = time()
    compute = y_dot.compute
    while t < T:
        val = compute(y=init, t=t, dt=dt)
        t += dt
        init = val
        if t % 1.0 < epsilon:
            error = 0
            for i in init:
                error += abs(i) ** 2
            # print 'Checking at t=', t, ' error: ', abs(1.0 - error)
            if abs(1.0 - error) > epsilon:
                # print 'Restarted', t
                dt *= 10 ** -1
                t = 0.0
                init = [1 / math.sqrt(NB_ENTRIES)] * NB_ENTRIES
                # start = 0.0
        # print 'timing: ', time() - start
    print 'Total time: ', time() - start
    # print 'dt=', dt
    # print 'T: ', T
    if profile:
        p.stop()
        p.score()

    problem = [H_p[i][i] for i in xrange(NB_ENTRIES)]
    probs = [abs(i) ** 2 for i in init]
    import pdb; pdb.set_trace()
    # print 'Problem: ', problem
    # print 'Probs: ', probs
    # print 'problem.min: ', np.min(problem)
    # print 'probs.found_min: ', problem[np.argmax(probs)]
    # print 'Sum: ', sum(probs)
    # p.stop()
    # p.score()

"""
TODO:
    * Remove sum() implement as loops
    * Make everything global
"""
