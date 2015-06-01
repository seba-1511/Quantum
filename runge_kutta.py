#!/usr/bin/env python
# -*- coding: utf-8 -*-


def RK4_vec():
    """Returns the 4th order Runge-Kutta approximation"""
    pass

f_vec = [[lambda x: x ** 2, lambda x: x ** 3],
         [lambda x: x, lambda x: x ** .5]]


y_dot = RK4_vec()

if __name__ == '__main__':
    pass
