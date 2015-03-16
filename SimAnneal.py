#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import numpy as np
from math import log, exp
from numpy.random import RandomState
from graph.plot import (
    plotLines,
    multiPlot,
    plot3D,
)
from utils import hamming_distance
from performance import timeit

"""
    TODO:
    - eliminate dots: use append = mylist.append
    - use map functions and list comprehensions instead of for loops.
    - Generate the lookup tables for the log/exp and Temperatures
    - Shuffle algo for the qubits. Less random gen, ensures they are all flipped
    - instead of lookup tables for probs, memoize them.
"""

DIFF_RANGE = 65
RND_SEED = 1234


class StandardAnnealer(object):

    """
        Implements a simulated annealing procedure
        to find the lowest energy for this given instance problem
    """

    def __init__(self, cost, update_cost, solution, values=(-1, 1), plot=False):
        self.cost = cost
        self.update_cost = update_cost
        self.solution = solution
        self.values = values
        self.plot = plot
        self.random = RandomState(seed=RND_SEED).uniform
        self.shuffle = RandomState(seed=RND_SEED).shuffle

    def save_plot(self, energies, temperatures, hammings):
        if self.plot:
            plotLines([[temperatures, energies], ],
                      title='Sim_Anneal_T_E', xlabel='T',
                      ylabel='Energy', xscale='log')
            plotLines([[temperatures, hammings], ],
                      title='Sim_Anneal_T_Hamming', xlabel='T',
                      ylabel='Hamming', xscale='log')
            multiPlot([[energies, hammings], ],
                      title='Sim_Anneal_E_Hamming', xlabel='Energy',
                      ylabel='Hamming')
            plot3D([temperatures, hammings, energies], title='3D_E_T_Ham',
                   xlabel='T', ylabel='Hamming', zlabel='E')

    def update_temperature(self, T):
        return T.pop(0) if len(T) > 0 else 0

    def update_solution(self, swap):
        new_sol = self.solution.copy()
        new_sol[swap] = new_sol[swap] * -1
        new_cost = self.update_cost(new_sol, self.solution, self.cost, swap)
        return new_sol, new_cost

    def stop_annealing(self, T, T_min):
        return T <= T_min

    def get_accept_probs(self, temp):
        return [exp(-diff / temp) for diff in xrange(-DIFF_RANGE, DIFF_RANGE)]

    def generate_temperatures(self, T, T_min):
        temps = []
        append = temps.append
        while T >= T_min:
            append(T)
            T = T * .927
        return temps

    @timeit
    def run(self, T=10, T_min=0.04, n_sweeps=1000):
        temperatures = self.generate_temperatures(
            T, T_min) if isinstance(T, int) else T
        self.cost = self.cost(self.solution)
        if self.plot:
            energies = [self.cost]
            hammings = [hamming_distance(self.solution, self.config)]
        swaps = np.arange(0, len(self.solution))
        for T in temperatures:
            start = time.time()
            accept_probs = self.get_accept_probs(T)
            for sweep in xrange(n_sweeps):
                self.shuffle(swaps)
                for swap in swaps:
                    new_sol, new_cost = self.update_solution(swap)
                    diff = int(self.cost - new_cost)
                    if diff >= 0 or self.random() < accept_probs[diff]:
                        self.solution = new_sol
                        self.cost = new_cost
                if self.plot:
                    energies.append(self.cost)
                    hammings.append(
                        hamming_distance(self.solution, self.config))
            print T, ': ', 'Current best: ', self.cost
            print 'timing', time.time() - start
        if self.plot:
            self.save_plot(energies, T, hammings)
        return (self.solution, self.cost)


class LinearAnnealer(StandardAnnealer):

    def __init__(*args, **kwargs):
        StandardAnnealer.__init__(*args, **kwargs)
