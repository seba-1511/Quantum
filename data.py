#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import numpy as np

from random import randint
from pdb import set_trace as debug

INSTANCES_DIR = 'plantedInstances/'
SOLUTIONS_DIR = 'solutionsForInstances/'


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
        debug()
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
        return open(directory + filename, 'r').readlines()


    def read_config(self, file):
        res = ''
        file.seek(4, 0)

    def read_matrix(self, file):
        pass

    def read_cost(self, file):
        pass

if __name__ == '__main__':
    print 'No tests implemented'
