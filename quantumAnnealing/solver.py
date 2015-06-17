#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
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
)

if __name__ == '__main__':
    NB_QUBITS = 5
    NB_ENTRIES = 2 ** 5
    T = 20.0
    A = lambda t: 1.0 - t / T
    B = lambda t: t / T

    H_p = generate_instance(NB_ENTRIES)
    H_d = driver_matrix(NB_ENTRIES)

    H = lambda t: add_sparse(
        dot_scal_sparse(A(t), H_d),
        dot_scal_sparse(B(t), H_p)
    )
    F = lambda t: dot_scal_sparse(1j, H(t))

    y_dot = SparseRK(F)
    init = [1] * NB_ENTRIES
    dt = 0.001
    t = 0

    while t < T:
        val = y_dot(y=init, t=t, dt=dt)
        t += dt
        init = val

    problem = [H_p[i][i] for i in xrange(NB_ENTRIES)]
    probs = [abs(a) ** 2 for a in init]
    print 'Problem: ', problem
    print 'Probs: ', probs
    print 'problem.argmin: ', np.argmin(problem)
    print 'probs.argmax: ', np.argmax(probs)
