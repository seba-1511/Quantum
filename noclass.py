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

print 'Random Seed: ', RND_SEED


# @profile
def run(problem_id, given_temps, given_sweeps):
    time_to_solution = time.time()
    # initialization of loop variables:
    add, sub = 0, 0
    random = Random(RND_SEED).random
    randrange = Random(RND_SEED).randrange
    choice = Random(1234).choice
    instance = LookupInstance(id=problem_id, nb_sg=420)
    # instance = LookupInstance(id=0, nb_sg=420)
    J = instance.J
    n_sweeps = given_sweeps
    cost = None
    possible_values = (-1, 1)
    # generate_temperatures ******************
    # temperatures = [2, 1, .5]
    temperatures = given_temps
    # ****************************************

    # get_accept_probs() *****************
    accept_probs = tuple(tuple(exp(d / T)
                               for d in xrange(-DIFF_RANGE, 0)) for T in temperatures)
    # ************************************
    # print 'Time to config: ', time.time() - time_to_solution
    # while cost != instance.min_cost:
    for i in xrange(5):
        #: Init variables for annealing
        solution = [choice(possible_values) for i in xrange(TOTAL_NB_QUBITS)]
        cost = instance.get_cost

        #: Run the annealing process
        cost = cost(solution)
        for T_i, T in enumerate(temperatures):
            start = time.time()
            for sweep in xrange(n_sweeps):
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
    end = time.time() - time_to_solution

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
    sweeps = xrange(100, 3000, 100)
    best = 10000 # time reference
    opt = [] # best sweep
    for sweep in sweeps:
        times = [run(i, temp, sweep) for i in ids]
        avg = sum(times) / len(times)
        best, opt = avg, sweep if avg <= best else best, opt
    return best, opt


if __name__ == '__main__':
    temps = [
        # The best temperatures are:  [2, 1.5, 1, 0.5]
        [2, 1, .5],  # Entry:  0 , average:  11.5023886442
        [2, 1, .75, .5],  # Entry:  1 , average:  11.7508713245
        [3, 2, 1, .5],  # Entry:  2 , average:  12.3210867167
        [3, 2.5, 2, 1, .5],  # Entry:  3 , average:  17.2061064005
        [2, 1.5, 1, .5],  # Entry:  4 , average:  11.0133153439
        [3, 2, 1.5, 1, .5],  # Entry:  5 , average:  14.8749244213
        [4, 3, 2, 1.5, 1, .5],  # Entry:  6 , average:  19.2818744421
        [5, 4, 3, 2, 1.5, 1, .5],  # Entry:  7 , average:  21.3565538883
        [3.2, 2.7, 2, 1.5, 1, .5],  # Entry:  8 , average:  16.5079873323
        drandge(.5, 1.5, .1)[::-1],  # Entry:  9 , average:  83.3435684204
        drandge(.5, 1.5, .2)[::-1],  # Entry:  10 , average:  44.958420825
        drandge(.5, 1.5, .25)[::-1],  # Entry:  11 , average:  34.9596844912
        drandge(.5, 1.5, .33)[::-1],  # Entry:  12 , average:  20.4650949955
        drandge(.5, 1.5, .4)[::-1],  # Entry:  13 , average:  17.7199317932
        drandge(.5, 1.5, .5)[::-1],  # Entry:  14 , average:  14.2617946863
        drandge(.5, 2, .1)[::-1],  # Entry:  15 , average:  153.844642377
        drandge(.5, 2, .2)[::-1],  # Entry:  16 , average:  65.9701389074
        drandge(.5, 2, .25)[::-1],  # Entry:  17 , average:  57.3783693552
        drandge(.5, 2, .33)[::-1],  # Entry:  18 , average:  34.0786446571
        drandge(.5, 2, .4)[::-1],  # Entry:  19 , average:  27.4933497429
        drandge(.5, 2, .5)[::-1],  # Entry:  20 , average:  20.2911326885
        drandge(.5, 2.5, .1)[::-1],  # Entry:  21 , average:  171.301710367
        drandge(.5, 2.5, .2)[::-1],  # Entry:  22 , average:  93.4000267744
        drandge(.5, 2.5, .25)[::-1],  # Entry:  23 , average:  55.5838775635
        drandge(.5, 2.5, .33)[::-1],  # Entry:  24 , average:  62.7699363232
        drandge(.5, 2.5, .4)[::-1],  # Entry:  25 , average:  40.5261266232
        drandge(.5, 2.5, .5)[::-1],  # Entry:  26 , average:  27.9606710911
        drandge(.5, 3, .1)[::-1],  # Entry:  27 , average:  179.166746593
        drandge(.5, 3, .2)[::-1],  # Entry:  28 , average:  88.2005657196
        drandge(.5, 3, .25)[::-1],  # Entry:  29 , average:  89.3465974808
        drandge(.5, 3, .33)[::-1],  # Entry:  30 , average:  58.3274750471
        drandge(.5, 3, .4)[::-1],  # Entry:  31 , average:  52.3981850624
        drandge(.5, 3, .5)[::-1],  # Entry:  32 , average:  46.5125962734
        drandge(.5, 3.5, .1)[::-1],  # Entry:  33 , average:  195.822213292
        drandge(.5, 3.5, .2)[::-1],  # Entry:  34 , average:  99.3887918711
        drandge(.5, 3.5, .25)[::-1],  # Entry:  35 , average:  64.0317424059
        drandge(.5, 3.5, .33)[::-1],  # Entry:  36 , average:  69.1890354395
        drandge(.5, 3.5, .4)[::-1],  # Entry:  37 , average:  41.7157850981
        drandge(.5, 3.5, .5)[::-1],  # Entry:  38 , average:  40.6816365719
    ]
    pool = Pool(processes=7)
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
# - change so that diff = new - old
# - Replace sum with for loop -> About the same, slightly slower
# - Find best configurations and temperatures
