#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import numpy as np

from random import Random, randint
from math import (
    log,
    exp,
)

from SimAnneal import StandardAnnealer
from data import (
    Instance,
    LookupInstance,
)
from performance import (
    timeit,
    profile,
    Profiler,
)
from GA.ga import GeneticAlgorithm


class Predictor(object):

    def __init__(self, instance):
        self.instance = instance

    def predict(self, ind):
        if not ind or not ind.genes or None in ind.genes:
            import pdb; pdb.set_trace()
            return -1.0
        return self.instance.get_cost(ind.genes)


choice = Random(1234).choice
TOTAL_NB_QUBITS = 512
DIFF_RANGE = 65
RND_SEED = 7186
# RND_SEED = randint(0, 10000)
ANNEALING_SCHEDULE = 0.927
MAX_SWEEPS = 1500

print 'Random Seed: ', RND_SEED


def run():
    instance = LookupInstance(id=0, nb_sg=420)
    pred = Predictor(instance)
    ga = GeneticAlgorithm(pred)
    opt = ga.find_optimal()
    print 'Solution: ', instance.get_cost(opt)
    # initialization of loop variables:
    # add, sub = 0, 0
    # random = Random(RND_SEED).random
    # shuffle = Random(RND_SEED).shuffle
    # instance = LookupInstance(id=0, nb_sg=420)
    # instance = LookupInstance(id=5, nb_sg=840)
    # T_start = 10
    # n_sweeps_start = 4
    # T_min = 0.5  # (0.95 - ANNEALING_SCHEDULE) * 3
    # time_to_solution = time.time()
    # sweeps_decay = 1.5
    # cost = None
    # while cost != instance.min_cost:
    # : Init variables for annealing
    #     T = T_start
    #     n_sweeps = n_sweeps_start
    #     val = (-1, 1)
    #     solution = [choice(val) for i in xrange(TOTAL_NB_QUBITS)]

    # : Init Standard Annealer
    #     cost = instance.get_cost
    # update_cost = instance.get_diff_cost
    #     J = instance.J

    # : Run the annealing process
    # generate_temperatures ******************
    #     temperatures = []
    #     append = temperatures.append
    #     while T >= T_min:
    #         append(T)
    #         T = T * ANNEALING_SCHEDULE
    # ****************************************

    #     cost = cost(solution)
    #     swaps = [i for i, val in enumerate(solution)]
    #     for T in temperatures:
    # start = time.time()
    #         n_sweeps = int(
    #             n_sweeps * sweeps_decay) if n_sweeps < MAX_SWEEPS else MAX_SWEEPS
    # get_accept_probs() *****************
    #         accept_probs = [exp(d / T) for d in xrange(-DIFF_RANGE, 0)]
    # ************************************

    #         for sweep in xrange(n_sweeps):
    #             shuffle(swaps)
    #             for swap in swaps:

    # update_solution ****************************
    #                 new_sol = solution[:]
    #                 new_sol[swap] *= -1
    # new_cost = update_cost(new_sol, solution, cost, swap)
    # update_cost *********************************************
    #                 add = 0
    #                 sub = 0
    #                 for j, value in J[swap]:
    #                     add += value * new_sol[j]
    #                     sub += value * solution[j]
    #                 new_cost = cost - \
    #                     (solution[swap] * sub) + (new_sol[swap] * add)
    # ************************************************************
    # ********************************************

    #                 diff = int(cost - new_cost)
    #                 if diff >= 0 or random() < accept_probs[diff]:
    #                     solution = new_sol
    #                     cost = new_cost
    #                     if cost == instance.min_cost:
    #                         break
    #         if cost == instance.min_cost:
    #             break
    #         print T, ': ', 'Current best: ', cost, '/', instance.min_cost
    # print 'timing', time.time() - start
    #     if cost == instance.min_cost:
    #         break
    # end = time.time() - time_to_solution

    # print 'Time to solution: ', end

if __name__ == '__main__':
    run()
