#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import png
import numpy as np

from scipy import misc
from random import randint, random, choice
from math import log
from pdb import set_trace as debug
from graph.plot import plotLines

TOTAL_NB_QUBITS = 512
INSTANCES_DIR = 'plantedInstances/'
SOLUTIONS_DIR = 'solutionsForInstances/'
VALUES_START = 4


def hamming_distance(str1, str2):
    """Implements the Hamming distance between 2 strings."""
    assert(len(str1) == len(str2))
    return sum([1 if x != y else 0 for x, y in zip(str1, str2)])


class Solution(object):

    """ Is an instance of the solutions for a given instance problem or id """

    def __init__(self, instance=None):
        self.instance = instance


class Instance(object):

    """ The instance of a problem given an id """

    def __init__(self, nb_sg=420, id=0, nb_qubits=504):
        self.nb_qubits = nb_qubits
        self.nb_sg = nb_sg
        self.id = id
        file = self.load_file()
        self.config = self.read_config(file)
        self.J = self.read_matrix(file)
        self.h = self.read_h(file)
        self.min_cost = self.read_cost(file)
        self.timing = self.parse_timing()

    def parse_timing(self):
        timing_file = 'tts_frustratedBonds_loopSize6.txt'
        directory = os.path.dirname(os.path.abspath(__file__))
        directory = os.path.join(directory, timing_file)
        filename = 'plantedFrustLoops_Nq%s_Nsg%s_s%s.dat' % (
            512,
            self.nb_sg,
            self.id,
        )
        f = open(directory, 'r')
        timings = f.readlines()
        for line in timings:
            values = line.split()
            if values[0] == filename:
                return int(values[1])

    def get_cost(self, sol):
        assert len(sol) == self.J.shape[0]
        H = 0
        for i, row in enumerate(self.J):
            for j, value in enumerate(row):
                H += (value * sol[i] * sol[j]) + (sol[i] * self.h[i])
        return H

    def load_file(self):
        filename = 'plantedFrustLoops_Nq%s_Nsg%s_s%s.dat' % (
            self.nb_qubits,
            self.nb_sg,
            self.id,
        )
        directory = os.path.dirname(os.path.abspath(__file__))
        directory = os.path.join(directory, INSTANCES_DIR)
        file = open(directory + filename, 'r')
        value = file.readlines()
        file.close()
        return value

    def read_config(self, file):
        config = np.zeros(TOTAL_NB_QUBITS)
        for i in xrange(VALUES_START, self.nb_qubits + VALUES_START):
            place, value = file[i].split()
            config[int(place)] += int(value)
        return config

    def read_matrix(self, file):
        matrix = np.zeros((TOTAL_NB_QUBITS, TOTAL_NB_QUBITS))
        for i in xrange(self.nb_qubits + VALUES_START + 1, len(file) - 1):
            row, col, value = file[i].split()
            matrix[int(row), int(col)] += int(value)
        return matrix

    def read_h(self, file):
        return np.zeros(TOTAL_NB_QUBITS)

    def read_cost(self, file):
        values = file[-1].split()
        return int(values[1])

    def print_J(self):
        filename = 'printed/plantedFrustLoops_Nq%s_Nsg%s_s%s.png' % (
            self.nb_qubits,
            self.nb_sg,
            self.id,
        )
        directory = os.path.dirname(os.path.abspath(__file__))
        directory = os.path.join(directory, filename)
        img = self.J
        misc.imsave(directory, img)

    def run_SA(self, T=500, c=0.8, n_iter=100):
        """
            Implements a simulated annealing procedure
            to find the lowest energy for this given instance problem
        """
        val = (-1, 1)
        sol = np.array([choice(val) for i in xrange(self.config.shape[0])])
        old_cost = self.get_cost(sol)
        scores = [old_cost, ]
        temperatures = [-T, ]
        print 'Current best: ', old_cost
        while T > 1:
            for i in xrange(n_iter):
                swap = randint(0, sol.shape[0] - 1)
                new_sol = sol.copy()
                new_sol[swap] = new_sol[swap] * -1
                new_cost = self.get_cost(new_sol)
                if new_cost < old_cost or (old_cost - new_cost) < T * log(random()):
                    sol = new_sol
                    old_cost = new_cost
                    print 'New best: ', new_cost
                T = c * T
                scores.append(old_cost)
                temperatures.append(-T)
                plotLines([[temperatures, scores], ],
                          title='Sim_Anneal_T_E', xlabel='T', ylabel='Energy')
        return sol

    def run_GA(self):
        """
            Implements a genetic algorithm
            to find the lowest energy for this given instance problem.
        """
        pass

if __name__ == '__main__':
    print 'No test implemented'
