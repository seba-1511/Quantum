#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from math import log
from random import (
    random,
    randint,
)


class StandardAnnealer(object):

    def __init__(self, cost, update_cost, solution, values=(-1, 1), plot=True):
        self.cost = cost
        self.update_cost = update_cost
        self.solution = solution

    def run(self, T=10, T_min=0.01, n_sweeps=1000, c=0.9):
        old_cost = self.cost(self.solution)
        while T > T_min:
            accept_prob = T * log(random())
            for sweep in xrange(n_sweeps):
                for i in xrange(len(self.solution)):
                    swap = randint(0, self.solution.shape[0] - 1)
                    new_sol = self.solution.copy()
                    new_sol[swap] = new_sol[swap] * -1
                    new_cost = self.update_cost(new_sol, self.solution, old_cost, swap)
                    if new_cost < old_cost or (old_cost - new_cost) < accept_prob:
                        self.solution = new_sol
                        old_cost = new_cost
                T = c * T
                # scores.append(old_cost)
                # temperatures.append(T)
                # hammings.append(hamming_distance(sol, self.config))
                # Plotting:
                # plotLines([[temperatures, scores], ],
                #           title='Sim_Anneal_T_E', xlabel='T',
                #           ylabel='Energy', xscale='log')
                # plotLines([[temperatures, hammings], ],
                #           title='Sim_Anneal_T_Hamming', xlabel='T',
                #           ylabel='Hamming', xscale='log')
                # multiPlot([[scores, hammings], ],
                #           title='Sim_Anneal_E_Hamming', xlabel='Energy',
                #           ylabel='Hamming')
                # plot3D([temperatures, hammings, scores], title='3D_E_T_Ham',
                #        xlabel='T', ylabel='Hamming', zlabel='E')
        return (self.solution, old_cost)


class LinearAnnealer(StandardAnnealer):

    def run():
        pass
