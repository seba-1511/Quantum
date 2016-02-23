#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
from array import array
from random import Random
from math import (
    exp,
)
from data import (
    LookupInstance,
)
from performance import (
    timeit,
    cprofile,
    Profiler,
)

TOTAL_NB_QUBITS = 512
DIFF_RANGE = 65
RND_SEED = 7186
N_SWEEPS = 1000
NB_EXECUTION_SOLVING = 4

print 'Random Seed: ', RND_SEED


# @profile
def run(problem_id, initial_temp, final_n_sweeps):
    time_to_solution = time.time()
    # initialization of loop variables:
    add, sub = 0, 0
    random = Random(RND_SEED).random
    randrange = Random(RND_SEED).randrange
    choice = Random(RND_SEED).choice
    instance = LookupInstance(id=problem_id, nb_sg=420)
    # instance = LookupInstance(id=0, nb_sg=420)
    J = instance.J
    n_sweeps = xrange(1, final_n_sweeps)
    cost = None
    possible_values = (-1, 1)
    # generate_temperatures ******************
    # temperatures = [2, 1, .5]
    beta_f = 10.0
    beta_i = 1.0 / initial_temp
    temp_gen = lambda beta, n: beta_i + \
        (((beta_f - beta_i) / (final_n_sweeps - 1)) * (n - 1))
    temperatures = [beta_i, ]
    for n in n_sweeps:
        temperatures.append(temp_gen(temperatures[-1], n))
    temperatures = [1.0 / t for t in temperatures]

    # ****************************************

    # get_accept_probs() *****************
    accept_probs = tuple(tuple(exp(d / T)
                               for d in xrange(-DIFF_RANGE, 0)) for T in temperatures)
    # ************************************
    # print 'Time to config: ', time.time() - time_to_solution
    # while cost != instance.min_cost:
    for i in xrange(NB_EXECUTION_SOLVING):
        #: Init variables for annealing
        solution = [choice(possible_values) for i in xrange(TOTAL_NB_QUBITS)]
        cost = instance.get_cost

        #: Run the annealing process
        cost = cost(solution)
        for T_i, T in enumerate(temperatures):
            start = time.time()
            for sweep in n_sweeps:
                swaps = [randrange(0, TOTAL_NB_QUBITS)
                         for i in xrange(TOTAL_NB_QUBITS)]
                for swap in swaps:
                    # update_solution ****************************
                    # sub = sum([value * solution[j] for j, value in J[swap]])
                    # sub *= solution[swap]
                    solution[swap] *= -1
                    add = sum([value * solution[j] for j, value in J[swap]])
                    add *= solution[swap]
                    # ********************************************
                    diff = 2 * add
                    if diff >= 0 or random() < accept_probs[T_i][diff]:
                        cost -= diff
                        if cost <= instance.min_cost:
                            break
                    else:
                        solution[swap] *= -1
                if cost <= instance.min_cost:
                    break
            # print T, ': ', 'Current best: ', cost, '/', instance.min_cost
            # print 'timing', time.time() - start
            if cost <= instance.min_cost:
                break
        if cost == instance.min_cost:
            break
    end = (time.time() - time_to_solution) / NB_EXECUTION_SOLVING

    print 'Time to solution: ', end
    return end

from multiprocessing import Pool
from random import random


def drange(start, stop, step):
    res = []
    r = start
    while r < stop:
        res.append(r)
        r += step
    return res


def drandge(start, stop, step):
    res = []
    r = start
    while r < stop:
        res.append(r)
        rnd = (random() - .5)
        r += (step + rnd) if step + rnd >= 0 else step
    return res


def explore(temp):
    ids = xrange(0, 500)
    sweeps = xrange(100, 10000, 100)
    avg = 36000
    opt = -1
    for s in sweeps:
        times = [run(i, temp, s) for i in ids]
        time = sum(times) / len(times)
        avg, opt = (time, s) if avg > time else (avg, opt)
    return (avg, opt)


if __name__ == '__main__':
    temps = drange(1, 20, 0.1)
    pool = Pool(processes=3)
    results = pool.map(explore, temps)
    mini = 3600
    posi = -1
    print '-' * 40
    for i, r in enumerate(results):
        print 'Entry: ', temps[i], ', average: ', r[0], ' and sweeps: ', r[1]
        mini, posi = (r, i) if r[0] < mini else (mini, posi)
        print ' '
    print '-' * 40
    print 'The best temperatures are: ', temps[posi], ' with a time of: ', mini[0], ' and sweeps: ', mini[1]

# To improve:
# - To find diff: if sol[i] == sol[j] -> add J[i, j] else substract.
# - Manually calculate the exp probs
# - clean code (ex: 1/T done several times)
