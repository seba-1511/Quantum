#!/usr/local/bin/python
# -*- coding: utf-8 -*-


def hamming_distance(str1, str2):
    """Implements the Hamming distance between 2 strings."""
    assert(len(str1) == len(str2))
    return sum([1 if x != y else 0 for x, y in zip(str1, str2)])
