#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from time import time
from performance import Profiler
from annealer import (
    driver_matrix,
)
from data import (
    load_instance,
    generate_instance,
    inst_0,
    inst_1,
)



def add_sparse(s1, s2, s1_keys, s2_keys):
    """
        Return the addition of two sparse matrices.
    """
    res = {k: s1[k].copy() for k in s1_keys}
    for row in s2_keys:
        for col in s2[row].keys():
            res[row][col] = s1[row][col] if row in s1 and col in s1[row] else 0
            res[row][col] += s2[row][col]
    return res


def dot_scal_sparse(scal, sparse, sparse_keys):
    """
        Returns the product of a scalar with a sparse matrix.
    """
    res = {k: sparse[k].copy() for k in sparse_keys}
    for row in sparse_keys:
        for col in sparse[row].keys():
            res[row][col] = sparse[row][col] * scal
    return res


def dot_sparse_vec(sparse, vec, keys):
    """
        Returns the product of a sparse matrix with a list vector.
    """
    res = []
    app = res.append
    for row in keys:
        val = 0
        for col in sparse[row].keys():
            val += vec[col] * sparse[row][col]
        app(val)
    return res


def add_vector(A, B):
    """ Must return unchanged A """
    res = []
    for a, b in zip(A, B):
        res.append(a+b)
    return res
    # for i, a in enumerate(A):
        # B[i] += a
    # return B


def dot_vec_vec(vec, wec):
    return sum([v * w for v, w in zip(vec, wec)])


def dot_vec_float(vec, fl):
    return [fl * v for v in vec]


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
        self.dim = len(F(0))
        self.keys = F(0).keys()

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
    T = 4.00002
    A, B = linear_schedule()

    H_p = generate_instance(NB_ENTRIES)
    H_d = driver_matrix(NB_ENTRIES, load=True)
    H_p_keys = H_p.keys()
    H_d_keys = H_d.keys()

    # H = lambda t: add_sparse(
        # dot_scal_sparse(A(t), H_d),
        # dot_scal_sparse(B(t), H_p)
    #)
    # F = lambda t: dot_scal_sparse(1j, H(t))

    # H_p = dot_scal_sparse(1j, H_p, H_p_keys)
    res = {k: H_p[k].copy() for k in H_p_keys}
    for row in H_p_keys:
        for col in H_p[row].keys():
            res[row][col] = H_p[row][col] * 1j
    H_p = res
    # H_d = dot_scal_sparse(1j, H_d, H_d_keys)
    res = {k: H_d[k].copy() for k in H_d_keys}
    for row in H_d_keys:
        for col in H_d[row].keys():
            res[row][col] = H_d[row][col] * 1j
    H_d = res

    F = lambda t: add_sparse(
        dot_scal_sparse(A(t), H_d, H_d_keys),
        dot_scal_sparse(B(t), H_p, H_p_keys),
        H_d_keys, H_p_keys
    )
    F_keys = F(0).keys()

    # y_dot = SparseRK(F)
    init = [1 / math.sqrt(NB_ENTRIES)] * NB_ENTRIES
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

        # f = F(t)

        a_n = dot_sparse_vec(f, init, F_keys)

        f = F(t + 0.5 * dt)
        b_n = dot_vec_float(a_n, 0.5 * dt)
        b_n = add_vector(init, b_n)
        b_n = dot_sparse_vec(f, b_n, F_keys)

        c_n = dot_vec_float(b_n, 0.5 * dt)
        c_n = add_vector(init, c_n)
        c_n = dot_sparse_vec(f, c_n, F_keys)

        f = F(t + dt)
        d_n = dot_vec_float(c_n, dt)
        d_n = add_vector(init, d_n)
        d_n = dot_sparse_vec(f, d_n, F_keys)

        b_n = dot_vec_float(b_n, 2)
        c_n = dot_vec_float(c_n, 2)
        approx = add_vector(a_n, b_n)
        approx = add_vector(c_n, approx)
        approx = add_vector(d_n, approx)
        approx = dot_vec_float(approx, (dt / 6.0))
        val = add_vector(approx, init)
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
                # start = 0.0
        # print 'timing: ', time() - start
    print 'Total time: ', time() - start
    # print 'dt=', dt
    # print 'T: ', T
    if profile:
        p.stop()
        p.score()

    problem = [H_p[i][i] for i in xrange(NB_ENTRIES)]
    probs = [abs(i) * abs(i) for i in init]
    # print 'Problem: ', problem
    print 'Probs: ', probs
    # print 'problem.min: ', np.min(problem)
    # print 'probs.found_min: ', problem[np.argmax(probs)]
    # print 'Sum: ', sum(probs)
    # p.stop()
    # p.score()

"""
TODO:
    * Make everything global
"""
