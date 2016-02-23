#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import os
import cPickle as pk
import numpy as np
from random import randint
from scipy.sparse import dok_matrix
from time import time
from performance import Profiler
from annealer import (
    # driver_matrix,
    bit_difference,
)
from data import (
    load_instance,
    # generate_instance,
    inst_0,
    inst_1,
)

DTYPE = np.float32


def generate_instance(size):
    res = dok_matrix((size, size), dtype=DTYPE)
    for x in xrange(size):
        res[x, x] = randint(0, size)
    res = res.tocsr()
    return res


def driver_matrix(nb_qubits, load=False):
    #: nb_qubits is actually 2 ** NB_QUBITS
    bnb_qubits = bin(nb_qubits)
    if os.path.isfile(str(nb_qubits) + 'Hd_scipy.bin') and load:
        with open(str(nb_qubits) + 'Hd_scipy.bin') as f:
            res = pk.load(f)
    else:
        res = dok_matrix((nb_qubits, nb_qubits), dtype=DTYPE)
        for row in xrange(nb_qubits):
            for col in xrange(nb_qubits):
                brow = bin(row)[2:]
                bcol = bin(col)[2:]
                diff = len(bnb_qubits) - len(bcol)
                bcol = ('0' * diff) + bcol
                diff = len(bnb_qubits) - len(brow)
                brow = ('0' * diff) + brow
                if bit_difference(brow, bcol, 1):
                    res[row, col] = -1
        with open(str(nb_qubits) + 'Hd_scipy.bin', 'wb') as f:
            pk.dump(res, f)
    return res.tocsr()


if __name__ == '__main__':
    NB_QUBITS = 8
    NB_ENTRIES = 2 ** NB_QUBITS
    epsilon = 1e-6
    T = 4.00002

    H_p = generate_instance(NB_ENTRIES)
    H_d = driver_matrix(NB_ENTRIES, load=True)


    H_p = H_p.dot(1j)
    H_d = H_d.dot(1j)

    init = [1 / math.sqrt(NB_ENTRIES) for _ in xrange(NB_ENTRIES)]
    init = np.array(init)
    dt = 0.001
    t = 0

    profile = 0
    if profile:
        p = Profiler()
        p.start()
    start = time()
    while t < T:
        # Replaces val = compute(init, t, dt) *********************************
        f = H_d.dot(1.0 - t/T) + H_p.dot(t / T)

        a_n = f.dot(init)
        half_dt = 0.5 * dt

        f = H_d.dot(1.0 - (t + half_dt) / T) + H_p.dot((t + half_dt) / T)
        b_n = f.dot(init + a_n * half_dt)

        c_n = f.dot(init + b_n * half_dt)

        f = H_d.dot(1.0 - (t + dt) / T) + H_p.dot((t + dt) / T)
        d_n = f.dot(init + c_n * dt)

        b_n *= 2
        c_n *= 2
        approx = (a_n + b_n + c_n + d_n) * dt / 6.0
        val = init + approx
        #**********************************************************************
        t += dt
        init = val
        if t % 1.0 < epsilon:
            error = 0
            for i in init:
                error += abs(i) * abs(i)
            # print 'Checking at t=', t, ' error: ', abs(1.0 - error)
            if abs(1.0 - error) > epsilon:
                print 'Restarted', t
                dt *= 0.1
                t = 0.0
                init = [1 / math.sqrt(NB_ENTRIES)] * NB_ENTRIES
                start = 0.0
        # print 'timing: ', time() - start
    print 'Total time: ', time() - start
    # print 'dt=', dt
    # print 'T: ', T
    if profile:
        p.stop()
        p.score()

    H_p = H_p.todok()
    problem = [H_p[i, i] for i in xrange(NB_ENTRIES)]
    probs = [abs(i) * abs(i) for i in init]
    # print 'Problem: ', problem
    # print 'Probs: ', probs
    print 'problem.min: ', np.min(problem)
    print 'probs.found_min: ', problem[np.argmax(probs)]
    # print 'Sum: ', sum(probs)
    # p.stop()
    # p.score()

"""
TODO:
    * Make everything global:
        * replace all lambdas
        *
"""
