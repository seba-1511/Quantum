#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy


def add_sparse(s1, s2):
    """
        Return the addition of two sparse matrices.
    """
    res = deepcopy(s1)
    for row in s2.keys():
        for col in s2[row].keys():
            res[row][col] = s1[row][col] if row in s1 and col in s1[row] else 0
            res[row][col] += s2[row][col]
    return res


def dot_scal_sparse(scal, sparse):
    """
        Returns the product of a scalar with a sparse matrix.
    """
    res = deepcopy(sparse)
    for row in res.keys():
        for col in res[row].keys():
            res[row][col] *= scal
    return res

if __name__ == '__main__':
    NB_QUBITS = 10

    A = lambda t: 2 * t
    B = lambda t: 3 * t
    H_d = {}
    H_p = {x: {x: 1} for x in xrange(NB_QUBITS)}

    H = lambda t: add_sparse(
        dot_scal_sparse(A(t), H_d), dot_scal_sparse(B(t), H_p))

    print dot_scal_sparse(3.0, H_p)

    # TODO: Represent sparse matrices as dict of dict: a[row][col] = val
    # Even though lists are faster, to add and multiply it will be practical
    # to have the col/row separation
