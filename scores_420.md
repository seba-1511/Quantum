
This file summarizes the running time averages to solve the planted problems with Ids <ids> given temperatures <temperatures> and with 420 sub graphs.

## Ids
ids = xrange(0, 500, 50)

## Temperatures and results

# Run on AWS GPU instance
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
        drange(.5, 3, .1)[::-1],  # Entry:  9 , average:  83.3435684204
        drange(.5, 3, .2)[::-1],  # Entry:  10 , average:  44.958420825
        drange(.5, 3, .25)[::-1],  # Entry:  11 , average:  34.9596844912
        drange(.5, 3, .33)[::-1],  # Entry:  12 , average:  20.4650949955
        drange(.5, 3, .4)[::-1],  # Entry:  13 , average:  17.7199317932
        drange(.5, 3, .5)[::-1],  # Entry:  14 , average:  14.2617946863
        drange(.5, 4, .1)[::-1],  # Entry:  15 , average:  153.844642377
        drange(.5, 4, .2)[::-1],  # Entry:  16 , average:  65.9701389074
        drange(.5, 4, .25)[::-1],  # Entry:  17 , average:  57.3783693552
        drange(.5, 4, .33)[::-1],  # Entry:  18 , average:  34.0786446571
        drange(.5, 4, .4)[::-1],  # Entry:  19 , average:  27.4933497429
        drange(.5, 4, .5)[::-1],  # Entry:  20 , average:  20.2911326885
        drange(.5, 5, .1)[::-1],  # Entry:  21 , average:  171.301710367
        drange(.5, 5, .2)[::-1],  # Entry:  22 , average:  93.4000267744
        drange(.5, 5, .25)[::-1],  # Entry:  23 , average:  55.5838775635
        drange(.5, 5, .33)[::-1],  # Entry:  24 , average:  62.7699363232
        drange(.5, 5, .4)[::-1],  # Entry:  25 , average:  40.5261266232
        drange(.5, 5, .5)[::-1],  # Entry:  26 , average:  27.9606710911
        drange(.5, 6, .1)[::-1],  # Entry:  27 , average:  179.166746593
        drange(.5, 6, .2)[::-1],  # Entry:  28 , average:  88.2005657196
        drange(.5, 6, .25)[::-1],  # Entry:  29 , average:  89.3465974808
        drange(.5, 6, .33)[::-1],  # Entry:  30 , average:  58.3274750471
        drange(.5, 6, .4)[::-1],  # Entry:  31 , average:  52.3981850624
        drange(.5, 6, .5)[::-1],  # Entry:  32 , average:  46.5125962734
        drange(.5, 7, .1)[::-1],  # Entry:  33 , average:  195.822213292
        drange(.5, 7, .2)[::-1],  # Entry:  34 , average:  99.3887918711
        drange(.5, 7, .25)[::-1],  # Entry:  35 , average:  64.0317424059
        drange(.5, 7, .33)[::-1],  # Entry:  36 , average:  69.1890354395
        drange(.5, 7, .4)[::-1],  # Entry:  37 , average:  41.7157850981
        drange(.5, 7, .5)[::-1],  # Entry:  38 , average:  40.6816365719
    ]



# run on laptop:

The best temperatures are:  [1.5, 1.0, 0.5]
    drange(.5, 2, .1)[::-1], # Entry:  0 , average:  43.119184804
    drange(.5, 2, .2)[::-1], # Entry:  1 , average:  22.1571786642
    drange(.5, 2, .25)[::-1], # Entry:  2 , average:  18.4246081829
    drange(.5, 2, .33)[::-1], # Entry:  3 , average:  15.6575805902
    drange(.5, 2, .4)[::-1], # Entry:  4 , average:  9.17653038502
    drange(.5, 2, .5)[::-1], # Entry:  5 , average:  8.76369099617


The best temperatures are:  [2.5, 2.0, 1.5, 1.0, 0.5]
    drange(.5, 3, .1)[::-1],  # Entry:  0 , average:  78.9687043667
    drange(.5, 3, .2)[::-1],  # Entry:  1 , average:  49.3169859886
    drange(.5, 3, .25)[::-1],  # Entry:  2 , average:  34.7966064692
    drange(.5, 3, .33)[::-1],  # Entry:  3 , average:  19.398724556
    drange(.5, 3, .4)[::-1],  # Entry:  4 , average:  21.3987741232
    drange(.5, 3, .5)[::-1],  # Entry:  5 , average:  11.1934151649


The best temperatures are:  [1.0, 0.5]
    drange(.5, 1.5, .1)[::-1],  # Entry:  0 , average:  30.1065980673
    drange(.5, 1.5, .2)[::-1],  # Entry:  1 , average:  13.2092992067
    drange(.5, 1.5, .25)[::-1],  # Entry:  2 , average:  20.8975524902
    drange(.5, 1.5, .33)[::-1],  # Entry:  3 , average:  8.63462820053
    drange(.5, 1.5, .4)[::-1],  # Entry:  4 , average:  9.2803948164
    drange(.5, 1.5, .5)[::-1],  # Entry:  5 , average:  5.76495139599

The best temperatures are:  [0.5]
    drange(.5, 1, .1)[::-1],  # Entry:  0 , average:  24.4155929804
    drange(.5, 1, .2)[::-1],  # Entry:  1 , average:  13.3331515789
    drange(.5, 1, .25)[::-1],  # Entry:  2 , average:  12.849138236
    drange(.5, 1, .33)[::-1],  # Entry:  3 , average:  10.0620547056
    drange(.5, 1, .4)[::-1],  # Entry:  4 , average:  10.3026433945
    drange(.5, 1, .5)[::-1],  # Entry:  5 , average:  5.12035181522
















