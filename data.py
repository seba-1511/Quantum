#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import numpy as np

from random import randint
from pdb import set_trace as debug

TOTAL_NB_QUBITS = 512
INSTANCES_DIR = 'plantedInstances/'
SOLUTIONS_DIR = 'solutionsForInstances/'
VALUES_START = 4


class Solution(object):

    """ Is an instance of the solutions for a given instance problem or id """

    def __init__(self, instance=None):
        pass


class Instance(object):

    """ The instance of a problem given an id"""

    def __init__(self, nb_sg=420, id=0):
        self.nb_qubits = 504
        self.nb_sg = nb_sg
        self.id = id
        file = self.load_file()
        self.config = self.read_config(file)
        self.J = self.read_matrix(file)
        self.min_cost = self.read_cost(file)
        file.close()

    def load_file(self):
        filename = 'plantedFrustLoops_Nq%s_Nsg%s_s%s.dat' % (
            self.nb_qubits,
            self.nb_sg,
            self.id
        )
        directory = os.path.dirname(os.path.abspath(__file__))
        directory = os.path.join(directory, INSTANCES_DIR)
        file = open(directory + filename, 'r')
        return file.readlines()

    def read_config(self, file):
        config = []
        for i in xrange(VALUES_START, self.nb_qubits + VALUES_START):
            values = file[i].split()
            config.append(int(values[1]))
        return np.array(config)

    def read_matrix(self, file):
        matrix = np.zeros((TOTAL_NB_QUBITS, TOTAL_NB_QUBITS))
        for i in xrange(self.nb_qubits + VALUES_START + 2, len(file) - 2):
            row, col, value = file[i].split()
            matrix[int(row), int(col)] += int(value)
        return matrix

    def read_cost(self, file):
        pass

if __name__ == '__main__':
    print 'No tests implemented'
