#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os
import re
from graph.plot import (
    plot,
    multiPlot,
    plotLines,
)
from data import (
    Instance,
    Solution,
)
from pdb import set_trace as debug


def parse_instance(file):
    """
        Given the a file object of an instance loaded with Python,
        it returns an Instance object of this problem.
    """
    nb_qubits, nb_sg, id = map(int, re.findall(r'\d+', file))
    return Instance(nb_sg=nb_sg, id=id, nb_qubits=nb_qubits)


def get_all_instances(nb_sg=None, nb_qubits=None, id=None):
    """
        Returns all the instances in an array.
        We can specify restrictions to load only a subset of them.
    """
    instances = []
    sg_condition = 'Nsg' + str(nb_sg) if nb_sg is not None else ''
    qb_condition = 'Nq' + str(nb_qubits) if nb_qubits is not None else ''
    id_condition = 's' + str(id) if id is not None else ''
    for (dirpath, dirnames, filenames) in os.walk('plantedInstances/'):
        for file in filenames:
            if (sg_condition in file and qb_condition in file and
                    id_condition in file):
                instances.append(parse_instance(file))
    return instances

if __name__ == '__main__':
    data = Instance(nb_sg=504, id=199)
    print 'Cost of config:', data.get_cost(data.config)
    print 'Timing: ', data.timing
    sa = data.run_SA()
    print 'Simulated Annealing: ', sa[1]
    debug()
