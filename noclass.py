#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import numpy as np

from random import Random
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

choice = Random(1234).choice
TOTAL_NB_QUBITS = 512
DIFF_RANGE = 65
RND_SEED = 1234


@profile
def run():
    print 'Loading all instances...'
    instance = LookupInstance()
    T = 10
    n_sweeps = 1000
    T_min = 1
    start = time.time()
    while True:
        #: Init variables for annealing
        val = (-1, 1)
        solution = [choice(val) for i in xrange(TOTAL_NB_QUBITS)]
        first_cost = instance.get_cost(solution)
        print 'Current best for ', instance.id, ' ', first_cost, ' config: ', instance.min_cost

        #: Init Standard Annealer
        cost = instance.get_cost
        update_cost = instance.get_diff_cost
        random = Random(RND_SEED).random
        shuffle = Random(RND_SEED).shuffle

        #: Run the annealing process
        # generate_temperatures ******************
        temperatures = []
        append = temperatures.append
        while T >= T_min:
            append(T)
            T = T * .927
        # ****************************************

        cost = cost(solution)
        swaps = [i for i, val in enumerate(solution)]
        for T in temperatures:
            start = time.time()

            # get_accept_probs() *****************
            accept_probs = [exp(-d / T)
                            for d in xrange(-DIFF_RANGE, DIFF_RANGE)]
            # ************************************

            for sweep in xrange(n_sweeps):
                shuffle(swaps)
                for swap in swaps:

                    # update_solution ****************************
                    new_sol = solution[:]
                    new_sol[swap] *= -1
                    new_cost = update_cost(new_sol, solution, cost, swap)
                    # ********************************************

                    diff = int(cost - new_cost)
                    if diff >= 0 or random() < accept_probs[diff]:
                        solution = new_sol
                        cost = new_cost
            print T, ': ', 'Current best: ', cost
            print 'timing', time.time() - start
        print 'Found best for ', instance.id, ' ', cost, ' config: ', instance.min_cost
        break
        if cost == instance.min_cost:
            break
    end = time.time() - start

    print 'Time to solution: ', end

if __name__ == '__main__':
    run()
