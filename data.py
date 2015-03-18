#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import png
import numpy as np

from scipy import misc
from numpy.random import RandomState
from random import (randint, random, Random)
from math import log
from pdb import set_trace as debug
from graph.plot import (
    plotLines,
    multiPlot,
    plot3D,
    plotLines3D,
    plotSurface3D
)
from performance import timeit
from SimAnneal import StandardAnnealer, LinearAnnealer

TOTAL_NB_QUBITS = 512
INSTANCES_DIR = 'plantedInstances/'
SOLUTIONS_DIR = 'solutionsForInstances/'
VALUES_START = 4

# choice = RandomState(seed=1234).choice
choice = Random(1234).choice


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

    def get_diff_cost(self, sol, prev_sol, cost, col):
        multiplier = self.J[:, col] + self.J[col, :]
        add = np.dot(multiplier, sol) * sol[col]
        sub = np.dot(multiplier, prev_sol) * prev_sol[col]
        return cost - (1 * sub) + (1 * add)

    def load_file(self):
        filename = 'plantedFrustLoops_Nq%s_Nsg%s_s%s.dat' % (
            self.nb_qubits,
            self.nb_sg,
            self.id,
        )
        self.filename = filename
        directory = os.path.dirname(os.path.abspath(__file__))
        directory = os.path.join(directory, INSTANCES_DIR)
        file = open(directory + filename, 'r')
        value = file.readlines()
        file.close()
        return value

    def read_config(self, file):
        # config = np.zeros(TOTAL_NB_QUBITS)
        config = [0 for _ in xrange(TOTAL_NB_QUBITS)]
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
        # return np.zeros(TOTAL_NB_QUBITS)
        return [0 for _ in xrange(TOTAL_NB_QUBITS)]

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

    @timeit
    def run_SA(self, T=10, n_sweeps=10, T_min=1):
        val = (-1, 1)
        # sol = np.array([choice(val) for i in xrange(TOTAL_NB_QUBITS)])
        sol = [choice(val) for i in xrange(TOTAL_NB_QUBITS)]
        old_cost = self.get_cost(sol)
        print 'Current best for ', self.id, ' ', old_cost, ' config: ', self.min_cost
        sol, cost = StandardAnnealer(
            cost=self.get_cost,
            update_cost=self.get_diff_cost,
            solution=sol,
            plot=False,
        ).run(T=T, n_sweeps=n_sweeps, T_min=T_min)
        print 'Found best for ', self.id, ' ', old_cost, ' config: ', self.min_cost
        return sol, cost

    def linear_SA(self, T=10, T_min=1, ):
        pass


class LookupInstance(Instance):

    """An instance, stored with a lookup table. Faster than the normal one."""

    def read_matrix(self, file):
        matrix = [[] for i in xrange(TOTAL_NB_QUBITS)]
        for i in xrange(self.nb_qubits + VALUES_START + 1, len(file) - 1):
            row, col, value = file[i].split()
            matrix[int(row)].append((int(col), int(value)))
            matrix[int(col)].append((int(row), int(value)))
        return matrix

    def get_cost(self, sol):
        H = 0
        max_len = len(self.J)
        first_half = self.J[:max_len]
        for i, row in enumerate(first_half):
            for j, value in row:
                H += (value * sol[i] * sol[j]) + (sol[i] * self.h[i])
        return H / 2

    def get_diff_cost(self, sol, prev_sol, cost, col):
        add = 0
        sub = 0
        for j, value in self.J[col]:
            add += value * sol[j]
            sub += value * prev_sol[j]
        return cost - (prev_sol[col] * sub) + (sol[col] * add)


if __name__ == '__main__':
    import time
    lookup = LookupInstance()
    instance = Instance()
    sol = [choice([-1, 1]) for i in xrange(TOTAL_NB_QUBITS)]
    cost_inst = instance.get_cost(sol)
    cost_look = lookup.get_cost(sol)
    for col in xrange(450, 512):
        print '\nFor col = ', col
        diff = [i for i in sol]
        diff[col] *= -1

        # Lookup benchmark
        diff_look = lookup.get_diff_cost(diff, sol, cost_look, col)
        start = time.time()
        for i in xrange(10):
            # lookup.get_cost(sol)
            diff_look = lookup.get_diff_cost(diff, sol, cost_look, col)
        print 'Lookup: ', time.time() - start

        # Instance benchmark
        diff_inst = instance.get_diff_cost(diff, sol, cost_inst, col)
        start = time.time()
        for i in xrange(10):
            # instance.get_cost(sol)
            diff_inst = instance.get_diff_cost(diff, sol, cost_inst, col)

        print 'Instance: ', time.time() - start
        print cost_inst, cost_look
        print diff_inst, diff_look
        assert(cost_inst == cost_look)
        assert(diff_inst == diff_look)
