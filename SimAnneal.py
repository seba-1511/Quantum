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

    def update_temperature(self, c, T):
        return c * T

    def update_solution(self):
        swap = randint(0, self.solution.shape[0] - 1)
        new_sol = self.solution.copy()
        new_sol[swap] = new_sol[swap] * -1
        new_cost = self.update_cost(
            new_sol, self.solution, self.cost, swap)
        return new_sol, new_cost

    def stop_annealing(self, T, T_min):
        return T <= T_min

    def run(self, T=10, T_min=0.01, n_sweeps=1000, c=0.9):
        self.cost = self.cost(self.solution)
        if self.plot:
            scores = [self.cost, ]
            temperatures = [T, ]
            hammings = [hamming_distance(self.solution, self.config), ]
        while not self.stop_annealing(T, T_min):
            accept_prob = T * log(random())
            for sweep in xrange(n_sweeps):
                for i in xrange(len(self.solution)):
                    new_sol, new_cost = self.update_solution()
                    if new_cost < self.cost or (self.cost - new_cost) < accept_prob:
                        self.solution = new_sol
                        self.cost = new_cost
                T = self.update_temperature(c, T)
                if self.plot:
                    scores.append(self.cost)
                    temperatures.append(T)
                    hammings.append(
                        hamming_distance(self.solution, self.config))
        return (self.solution, self.cost)


class LinearAnnealer(StandardAnnealer):

    def __init__(*args, **kwargs):
        StandardAnnealer.__init__(*args, **kwargs)

    def update_temperature(self):
        pass
