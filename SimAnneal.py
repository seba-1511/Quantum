#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from math import log
from random import (
    random,
    randint,
)
from graph.plot import (
    plotLines,
    multiPlot,
    plot3D,
)
from utils import hamming_distance


class StandardAnnealer(object):

    def __init__(self, cost, update_cost, solution, values=(-1, 1), plot=False):
        self.cost = cost
        self.update_cost = update_cost
        self.solution = solution
        self.values = values
        self.plot = plot

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

    def run(self, T=10, T_min=0.01, n_sweeps=1000, c=0.9):
        old_cost = self.cost(self.solution)
        if self.plot:
            scores = [old_cost, ]
            temperatures = [T, ]
            hammings = [hamming_distance(self.solution, self.config), ]
        while T > T_min:
            accept_prob = T * log(random())
            for sweep in xrange(n_sweeps):
                for i in xrange(len(self.solution)):
                    swap = randint(0, self.solution.shape[0] - 1)
                    new_sol = self.solution.copy()
                    new_sol[swap] = new_sol[swap] * -1
                    new_cost = self.update_cost(
                        new_sol, self.solution, old_cost, swap)
                    if new_cost < old_cost or (old_cost - new_cost) < accept_prob:
                        self.solution = new_sol
                        old_cost = new_cost
                T = c * T
                if self.plot:
                    scores.append(old_cost)
                    temperatures.append(T)
                    hammings.append(
                        hamming_distance(self.solution, self.config))
        return (self.solution, old_cost)


class LinearAnnealer(StandardAnnealer):

    def run():
        pass
