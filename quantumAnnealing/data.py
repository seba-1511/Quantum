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
    #res[size - 3] = {size-3: 0}

    return res
