#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import os
import cPickle as pk
import numpy as np
from random import randint
from scipy.sparse import *
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
    res = res.tocsc()
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
        with open(str(nb_qubits) + 'Hd.bin_scipy', 'wb') as f:
            pk.dump(res, f)
    return res.tocsc()


def add_sparse(s1, s2):
    """
        Return the addition of two sparse matrices.
    """
    return s1 + s2


def dot_scal_sparse(scal, sparse):
    """
        Returns the product of a scalar with a sparse matrix.
    """
    return sparse.multiply(scal)


def dot_sparse_vec(sparse, vec):
    """
        Returns the product of a sparse matrix with a list vector.
    """
    return sparse.dot(vec)


def add_vector(A, B):
    """ Must return unchanged A """
    return A + B


def dot_vec_vec(vec, wec):
    return vec.dot(wec)


def dot_vec_float(vec, fl):
    return vec.dot(fl)


class SparseRK(object):

    """
        RK for vector equations.
    """

    def __init__(self, F, y_dot=None):
        """
            F: the matrix of functions
            y_dot: could be an array of the functions for y's (Not used yet)
        """
        self.F = F
        self.dim = F(0).shape[0]

    def compute(self, y, t=0, dt=0.1):
        f = self.F(t)
        keys = self.keys
        a_n = dot_sparse_vec(f, y, keys)

        f = self.F(t + 0.5 * dt)
        b_n = dot_vec_float(a_n, 0.5 * dt)
        b_n = add_vector(y, b_n)
        b_n = dot_sparse_vec(f, b_n, keys)

        c_n = dot_vec_float(b_n, 0.5 * dt)
        c_n = add_vector(y, c_n)
        c_n = dot_sparse_vec(f, c_n, keys)

        f = self.F(t + dt)
        d_n = dot_vec_float(c_n, dt)
        d_n = add_vector(y, d_n)
        d_n = dot_sparse_vec(f, d_n, keys)

        b_n = dot_vec_float(b_n, 2)
        c_n = dot_vec_float(c_n, 2)
        approx = add_vector(a_n, b_n)
        approx = add_vector(approx, c_n)
        approx = add_vector(approx, d_n)
        approx = dot_vec_float(approx, (dt / 6.0))
        return add_vector(y, approx)


def linear_schedule():
    A = lambda t: 1.0 - t / T
    B = lambda t: t / T
    return (A, B)


def new_schedule():
    A = lambda t: 1.0 - t * 2 / T
    B = lambda t: t * 2 / T
    return (A, B)


if __name__ == '__main__':
    NB_QUBITS = 7
    NB_ENTRIES = 2 ** NB_QUBITS
    epsilon = 1e-6
    T = 40.00002
    A, B = linear_schedule()

    H_p = generate_instance(NB_ENTRIES)
    H_d = driver_matrix(NB_ENTRIES, load=True)


    H_p = dot_scal_sparse(1j, H_p)
    H_d = dot_scal_sparse(1j, H_d)

    F = lambda t: add_sparse(
        dot_scal_sparse(A(t), H_d),
        dot_scal_sparse(B(t), H_p),
    )

    # y_dot = SparseRK(F)
    init = [1 / math.sqrt(NB_ENTRIES)] * NB_ENTRIES
    init = np.array(init)
    dt = 0.001
    t = 0

    profile = 0
    if profile:
        p = Profiler()
        p.start()
    start = time()
    # compute = y_dot.compute
    while t < T:
        # Replaces val = compute(init, t, dt) *********************************
        # val = y_dot.compute(y=init, t=t, dt=dt)
        f = F(t)

        a_n = dot_sparse_vec(f, init)

        f = F(t + 0.5 * dt)
        b_n = dot_vec_float(a_n, 0.5 * dt)
        b_n = add_vector(init, b_n)
        b_n = dot_sparse_vec(f, b_n)

        c_n = dot_vec_float(b_n, 0.5 * dt)
        c_n = add_vector(init, c_n)
        c_n = dot_sparse_vec(f, c_n)

        f = F(t + dt)
        d_n = dot_vec_float(c_n, dt)
        d_n = add_vector(init, d_n)
        d_n = dot_sparse_vec(f, d_n)

        b_n = dot_vec_float(b_n, 2)
        c_n = dot_vec_float(c_n, 2)
        approx = add_vector(a_n, b_n)
        approx = add_vector(c_n, approx)
        approx = add_vector(d_n, approx)
        approx = dot_vec_float(approx, (dt / 6.0))
        val = add_vector(approx, init)
        #**********************************************************************
        t += dt
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
                # start = 0.0
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
    * Remove sum() implement as loops
    * Make everything global
"""
