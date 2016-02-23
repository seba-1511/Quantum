## Simulated Annealing

Contains different implementation of the algorithm.

### Useful Files

#### solutionsForInstances/
Files containing the configurations for the ground state of problems in plantedInstances/

#### plantedInstances/
Contains the description of planted instances problems. 

#### graph/
Graphing utilities

#### LookupTable/
Lookup table problem instances where the problem matrix is not given but the energy for each configuration is. (no classes, no functions, no Numpy. All procedural)

#### noclass.py
A pretty fast grid-search of best schedule for simulated annealing over planted instances.

#### albash_noclass.py
Same as noclass, but using albash’s schedule.

#### lookupnoclass
Same as noclass, but for LookupTable problems.

#### data.py
Allows to easily load problems, whether they are planted or lookup.

#### performance.py
Utilities to profile python code.

#### scores_*.md
Files containing grid search results for several schedules of simulated annealing on all planted instances.

### Not Very Useful Files

#### printed/
Planted instances as images.

#### GA/
Genetic Algorithm implementation.

#### main.py
A clean but slow simulated annealing example.

#### SimAnneal.py
A class implementation of different kinds of simulated annealing. Clearly slower than noclass standard.

#### ga.py
Solving planted instances with genetic algorithm.

#### plot_neighborhood.py
Plotting the energy neighborhood of a specific configuration, given a problem.

#### plot_time_per__sg.py
Plotting the average time for each kind of planted problem instance, based on the number of subgraphs.

