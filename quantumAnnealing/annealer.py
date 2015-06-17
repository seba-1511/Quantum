#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import cPickle as pk
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


def dot_sparse_vec(sparse, vec):
    """
        Returns the product of a sparse matrix with a list vector.
    """
    res = []
    for row in sparse.keys():
        val = sum([vec[col] * sparse[row][col] for col in sparse[row].keys()])
        res.append(val)
    return res


def bit_difference(nb1, nb2, diff):
    s = sum([a != b for a, b in zip(nb1, nb2)])
    return s == diff
    if len(nb1) <= 0:
        return diff >= 0
    elif diff <= 0:
        return False
    else:
        diff -= 0 if nb1[0] == nb2[0] else 1
        return bit_difference(nb1[1:], nb2[1:], diff)


def driver_matrix(nb_qubits):
    bnb_qubits = bin(nb_qubits)
    if os.path.isfile(str(nb_qubits) + 'Hd.bin'):
        with open(str(nb_qubits) + 'Hd.bin') as f:
            res = pk.load(f)
    else:
        res = {
            x: {} for x in xrange(nb_qubits)
        }
        for row in xrange(nb_qubits):
            for col in xrange(nb_qubits):
                brow = bin(row)[2:]
                bcol = bin(col)[2:]
                diff = len(bnb_qubits) - len(bcol)
                bcol = ('0' * diff) + bcol
                diff = len(bnb_qubits) - len(brow)
                brow = ('0' * diff) + brow
                if bit_difference(brow, bcol, 1):
                    res[row][col] = 1
        with open(str(nb_qubits) + 'Hd.bin', 'wb') as f:
            pk.dump(res, f)
    return res

if __name__ == '__main__':
    NB_QUBITS = 5
    NB_ENTRIES = 2 ** NB_QUBITS

    A = lambda t: t
    B = lambda t: 1.0 - t
    H_d = driver_matrix(NB_ENTRIES)
    H_p = {x: {x: 1} for x in xrange(NB_ENTRIES)}

    H = lambda t: add_sparse(
        dot_scal_sparse(A(t), H_d), dot_scal_sparse(B(t), H_p))

    print H_d

    # DONE: Represent sparse matrices as dict of dict: a[row][col] = val
    # Even though lists are faster, to add and multiply it will be practical
    # to have the col/row separation
    # There should be NB_QUBITS neighbors for the driver_matrix
