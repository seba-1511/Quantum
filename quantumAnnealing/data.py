#!/usr/bin/env python
# -*- coding: utf-8 -*-


from random import randint


def load_instance(nb_qubits, id, sg):
    pass


def generate_instance(size):
    res = {
        x: {
            x: randint(0, size)
        } for x in xrange(size)
    }
    # res[size - 3] = {size-3: 0}

    return res


def inst_0():
    lis = [1, 2, 3, 4, 1, 2, 3, 4, 7, 6, 0, 34, 2, 6, 2, 5]
    return {i: {i: x} for i, x in enumerate(lis)}


def inst_1():
    lis = [1, 0, 3, 4, 2, 89, 4, 4, 1, 6, 2, 34, 3, 6, 1, 5, 1, 2, 3, 4, 1, 2, 3, 4, 7, 6, 8, 34, 2, 6, 2, 5]
    return {i: {i: x} for i, x in enumerate(lis)}
