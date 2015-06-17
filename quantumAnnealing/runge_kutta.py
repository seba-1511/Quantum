#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from graph.plot import plotLines
from annealer import dot_sparse_vec


def add_vector(A, B):
    return [a + b for a, b in zip(A, B)]


def dot_mat_vec(F, y):
    res = []
    for f in F:
        res.append(sum([a * b for a, b in zip(f, y)]))
    return res


def dot_vec_float(vec, fl):
    return [fl * v for v in vec]


def dot_vec_vec(vec, wec):
    return sum([v * w for v, w in zip(vec, wec)])


def complex_conj_vec(vec):
    return [a.conjugate() for a in vec]


# *************************************


def RK4(f):
    return lambda t, y, dt: (
        lambda dy1: (
            lambda dy2: (
                lambda dy3: (
                    lambda dy4: (dy1 + 2 * dy2 + 2 * dy3 + dy4) / 6
                )(dt * f(t + dt, y + dy3))
            )(dt * f(t + dt / 2, y + dy2 / 2))
        )(dt * f(t + dt / 2, y + dy1 / 2))
    )(dt * f(t, y))


def print_RK4(dy, t, y, dt):
    count = 0
    while t <= 1:
        print(str(count) + ": y(%2.3f)\t= %4.6f \t" % (t, y))
        t, y = t + dt, y + dy(t, y, dt)
        count += 1
    return y
# **************************************


class RK(object):

    """
        RK for vector equations.
    """

    def __init__(self, F, y_dot=None):
        """
            F: the matrix of functions
            y_dot: could be an array of the functions for y's (Not used yet)
        """
        self.F = F
        self.dim = len(F(0))

    def __call__(self, y, t=0, dt=0.1):
        f = self.F(t)
        a_n = dot_mat_vec(f, y)

        f = self.F(t + 0.5 * dt)
        b_n = dot_vec_float(a_n, 0.5 * dt)
        b_n = add_vector(y, b_n)
        b_n = dot_mat_vec(f, b_n)

        c_n = dot_vec_float(b_n, 0.5 * dt)
        c_n = add_vector(y, c_n)
        c_n = dot_mat_vec(f, c_n)

        f = self.F(t + dt)
        d_n = dot_vec_float(c_n, dt)
        d_n = add_vector(y, d_n)
        d_n = dot_mat_vec(f, d_n)

        b_n = dot_vec_float(b_n, 2)
        c_n = dot_vec_float(c_n, 2)
        approx = add_vector(a_n, b_n)
        approx = add_vector(approx, c_n)
        approx = add_vector(approx, d_n)
        approx = dot_vec_float(approx, (dt / 6.0))
        return add_vector(y, approx)


class SparseRK(object):

    """
        RK for vector equations.
    """

    def __init__(self, F, y_dot=None):
        """
            F: the matrix of functions
            y_dot: could be an array of the functions for y's (Not used yet)
        """
        self.F = F
        self.dim = len(F(0))

    def __call__(self, y, t=0, dt=0.1):
        f = self.F(t)
        a_n = dot_sparse_vec(f, y)

        f = self.F(t + 0.5 * dt)
        b_n = dot_vec_float(a_n, 0.5 * dt)
        b_n = add_vector(y, b_n)
        b_n = dot_sparse_vec(f, b_n)

        c_n = dot_vec_float(b_n, 0.5 * dt)
        c_n = add_vector(y, c_n)
        c_n = dot_sparse_vec(f, c_n)

        f = self.F(t + dt)
        d_n = dot_vec_float(c_n, dt)
        d_n = add_vector(y, d_n)
        d_n = dot_sparse_vec(f, d_n)

        b_n = dot_vec_float(b_n, 2)
        c_n = dot_vec_float(c_n, 2)
        approx = add_vector(a_n, b_n)
        approx = add_vector(approx, c_n)
        approx = add_vector(approx, d_n)
        approx = dot_vec_float(approx, (dt / 6.0))
        return add_vector(y, approx)


class RK_np(RK):

    """
        Same as RK, but with a numpy implementation.
    """

    def __init__(self, F, y_dot=None):
        self.F = F
        self.dim = len(F(0))

    def __call__(self, y, t=0, dt=0.1):
        y = np.array(y)
        f = self.F(t)
        a_n = np.dot(f, y)

        f = self.F(t + 0.5 * dt)
        b_n = ((0.5 * dt) * a_n) + y
        b_n = np.dot(f, b_n)

        c_n = ((0.5 * dt) * b_n) + y
        c_n = np.dot(f, c_n)

        f = self.F(t + dt)
        d_n = (dt * c_n) + y
        d_n = np.dot(f, d_n)

        return y + (dt / 6.0) * (a_n + 2 * b_n + 2 * c_n + d_n)


if __name__ == '__main__':

    #F_vec = lambda x: [[complex(0, 1), complex(0, 1)],
                       #[complex(0, 1), complex(0, -1)]]

    #y_dot = RK(F_vec)
    #init = [1, 1]
    #dt = 0.001
    #print dot_mat_vec(F_vec(0), init)
    #t = 0
    #vals = [init, ]
    #ts = [t, ]
    #braket = [0, ]
    #while t <= 20:
        #val = y_dot(y=init, t=t, dt=dt)
        ## print 'y=', init, ', t=', t, 'y_dot=', val
        #vals.append(val)
        #t += dt
        #init = val
        #ts.append(t)
        #ket = dot_mat_vec(F_vec(0), init)
        #ket = np.abs(dot_vec_vec(complex_conj_vec(init), ket))
        #braket.append(ket)
    ##: Plotting:
    #vals = np.array(vals)
    #y1_sq = np.abs(vals[:, 0]) ** 2
    #y2_sq = np.abs(vals[:, 1]) ** 2
    #y1_y2_sq_sum = y1_sq + y2_sq
    #plotLines([[ts, y1_sq], [ts, y2_sq], [ts, y1_y2_sq_sum], [ts, braket]],
              #title='Runge-Kutta', xlabel='Time', ylabel='')
