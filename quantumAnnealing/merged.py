#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data import generate_instance
from annealer import driver_matrix
from time import time
from performance import Profiler

# Variables definition:

NB_QUBITS = 12
NB_ENTRIES = 2 ** NB_QUBITS
epsilon = 1e-6
T = 0.00002

H_p = generate_instance(NB_ENTRIES)
H_d = driver_matrix(NB_ENTRIES, load=True)

A = lambda t: 1.0 - t / T
B = lambda t: t / T

init = [1 / math.sqrt(NB_ENTRIES)] * NB_ENTRIES
dt = 0.000001
t = 0

# Functions definition:


def A():
    return 1.0 - t / T


def B():
    return t / T


def add_sparse(s1, s2):
    """
        Return the addition of two sparse matrices.
    """
    res = {k: s1[k].copy() for k in s1.keys()}
    for row in s2.keys():
        for col in s2[row].keys():
            res[row][col] = s1[row][col] if row in s1 and col in s1[row] else 0
            res[row][col] += s2[row][col]
    return res


def F(t):
    return add_sparse(
        dot_scal_sparse(A(t), H_d),
        dot_scal_sparse(B(t), H_p)
    )


def dot_scal_sparse(scal, sparse):
    """
        Returns the product of a scalar with a sparse matrix.
    """
    res = {k: sparse[k].copy() for k in sparse.keys()}
    for row in res.keys():
        for col in res[row].keys():
            res[row][col] *= scal
    return res


def dot_sparse_vec(sparse, vec):
    """
        Returns the product of a sparse matrix with a list vector.
    """
    res = []
    for row in sparse.keys():
        val = sum([vec[col] * sparse[row][col] for col in sparse[row].keys()])
        res.append(val)
    return res


def add_vector(A, B):
    return [a + b for a, b in zip(A, B)]


def dot_vec_float(vec, fl):
    return [fl * v for v in vec]

# Computations:
p = Profiler()
p.start()
start = time()
while t < T:
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
    approx = add_vector(approx, c_n)
    approx = add_vector(approx, d_n)
    approx = dot_vec_float(approx, (dt / 6.0))
    init = add_vector(init, approx)
    t += dt
    if t % 1.0 < epsilon:
        print 'Checking at t=', t, ' error: ', abs(1.0 - sum([abs(i) ** 2
                                                              for i in init]))
        if abs(1.0 - sum([abs(i) ** 2 for i in init])) > epsilon:
            print 'Restarted', t
            dt *= 10 ** -1
            t = 0.0
            init = [1 / math.sqrt(NB_ENTRIES)] * NB_ENTRIES
            # start = 0.0
    print 'timing: ', time() - start
print 'Total time: ', time() - start
print 'dt=', dt
print 'T: ', T
p.stop()
p.score()

problem = [H_p[i][i] for i in xrange(NB_ENTRIES)]
probs = [abs(i) ** 2 for i in init]
# print 'Problem: ', problem
# print 'Probs: ', probs
print 'problem.min: ', np.min(problem)
print 'probs.found_min: ', problem[np.argmax(probs)]
print 'Sum: ', sum(probs)
# p.stop()
# p.score()
