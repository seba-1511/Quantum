#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import numpy as np

from random import randint


class Solution(object):

    """ Is an instance of the solutions for a given instance problem or id """

    def __init__(self, instance=None, id=None):
        id = instance.id if instance.id is not None else id
        id = randint()


class Instance(object):

    """ The instance of a problem given an id"""

    def __init__(self, nb_sg=420, id=0):
        self.nb_qubits = 504
        self.nb_sg = nb_sg
        self.id = id
        file = self.load_file()
        self.config = self.read_solution(file)
        self.J = self.read_matrix(file)
        self.min_cost = self.read_cost(file)

    def load_file(self):
        filename = ''
        directory = os.path.dirname(os.path.abspath(__file__))
        directory = os.path.join(directory, 'plantedInstances')

    def read_solution(self, file):
        pass

    def read_matrix(self, file):
        pass

    def read_cost(self, file):
        pass

if __name__ == '__main__':
    print 'No tests implemented'
