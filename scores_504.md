
This file summarizes the running time averages to solve the planted problems with Ids <ids> given temperatures <temperatures> and with 504 sub graphs.

## Ids
ids = xrange(0, 500, 50)

## Temperatures and results

# Run on AWS GPU instance
    temps = [
        # The best temperatures are:  [2, 1.5, 1, 0.5]
        [2, 1, .5],  # Entry:  0 , average:  6.08006167412
        [2, 1, .75, .5],  # Entry:  1 , average:  8.63446967602
        [3, 2, 1, .5],  # Entry:  2 , average:  4.28594341278
        [3, 2.5, 2, 1, .5],  # Entry:  3 , average:  11.2874209881
        [2, 1.5, 1, .5],  # Entry:  4 , average:  4.02567346096
        [3, 2, 1.5, 1, .5],  # Entry:  5 , average:  9.17227263451
        [4, 3, 2, 1.5, 1, .5],  # Entry:  6 , average:  12.9710660934
        [5, 4, 3, 2, 1.5, 1, .5],  # Entry:  7 , average:  13.4417264223
        [3.2, 2.7, 2, 1.5, 1, .5],  # Entry:  8 , average:  8.59763152599
        drange(.5, 3, .1)[::-1],  # Entry:  9 , average:  27.6531776667
        drange(.5, 3, .2)[::-1],  # Entry:  10 , average:  13.9443939447
        drange(.5, 3, .25)[::-1],  # Entry:  11 , average:  11.0896609068
        drange(.5, 3, .33)[::-1],  # Entry:  12 , average:  9.04447655678
        drange(.5, 3, .4)[::-1],  # Entry:  13 , average:  6.93130748272
        drange(.5, 3, .5)[::-1],  # Entry:  14 , average:  7.57686486244
        drange(.5, 4, .1)[::-1],  # Entry:  15 , average:  65.001205349
        drange(.5, 4, .2)[::-1],  # Entry:  16 , average:  30.0953076363
        drange(.5, 4, .25)[::-1],  # Entry:  17 , average:  24.6656080961
        drange(.5, 4, .33)[::-1],  # Entry:  18 , average:  15.3797037125
        drange(.5, 4, .4)[::-1],  # Entry:  19 , average:  17.6162266016
        drange(.5, 4, .5)[::-1],  # Entry:  20 , average:  14.4120716572
        drange(.5, 5, .1)[::-1],  # Entry:  21 , average:  123.004396343
        drange(.5, 5, .2)[::-1],  # Entry:  22 , average:  57.3280613661
        drange(.5, 5, .25)[::-1],  # Entry:  23 , average:  31.6118182182
        drange(.5, 5, .33)[::-1],  # Entry:  24 , average:  27.4091967344
        drange(.5, 5, .4)[::-1],  # Entry:  25 , average:  35.4817849874
        drange(.5, 5, .5)[::-1],  # Entry:  26 , average:  15.3356433153
        drange(.5, 6, .1)[::-1],  # Entry:  27 , average:  145.142740059
        drange(.5, 6, .2)[::-1],  # Entry:  28 , average:  71.5834856749
        drange(.5, 6, .25)[::-1],  # Entry:  29 , average:  72.0808825254
        drange(.5, 6, .33)[::-1],  # Entry:  30 , average:  47.0284476519
        drange(.5, 6, .4)[::-1],  # Entry:  31 , average:  25.6613370895
        drange(.5, 6, .5)[::-1],  # Entry:  32 , average:  38.1279673338
        drange(.5, 7, .1)[::-1],  # Entry:  33 , average:  148.960394168
        drange(.5, 7, .2)[::-1],  # Entry:  34 , average:  103.458539939
        drange(.5, 7, .25)[::-1],  # Entry:  35 , average:  44.2248064995
        drange(.5, 7, .33)[::-1],  # Entry:  36 , average:  49.2534312963
        drange(.5, 7, .4)[::-1],  # Entry:  37 , average:  36.1861743927
        drange(.5, 7, .5)[::-1],  # Entry:  38 , average:  36.309117794
    ]

# on laptop:

The best temperatures are:  [0.8300000000000001, 0.5]
        drange(.5, 1, .1)[::-1],  # Entry:  0 , average:  13.6762528896
        drange(.5, 1, .2)[::-1],  # Entry:  1 , average:  7.38200819492
        drange(.5, 1, .25)[::-1],  # Entry:  2 , average:  6.97562570572
        drange(.5, 1, .33)[::-1],  # Entry:  3 , average:  2.65786590576
        drange(.5, 1, .4)[::-1],  # Entry:  4 , average:  3.35053946972
        drange(.5, 1, .5)[::-1],  # Entry:  5 , average:  4.23577251434

The best temperatures are:  [2.0, 1.5, 1.0, 0.5]
        drange(.5, 2.5, .1)[::-1],  # Entry:  0 , average:  19.6650770664
        drange(.5, 2.5, .2)[::-1],  # Entry:  1 , average:  26.4916772127
        drange(.5, 2.5, .25)[::-1],  # Entry:  2 , average:  10.1017335892
        drange(.5, 2.5, .33)[::-1],  # Entry:  3 , average:  9.68981463909
        drange(.5, 2.5, .4)[::-1],  # Entry:  4 , average:  6.91152791977
        drange(.5, 2.5, .5)[::-1],  # Entry:  5 , average:  4.79928133488


The best temperatures are:  [3.0, 2.5, 2.0, 1.5, 1.0, 0.5]

        drange(.5, 3.5, .1)[::-1],  # Entry:  0 , average:  51.7976029158
        drange(.5, 3.5, .2)[::-1],  # Entry:  1 , average:  26.7826597929
        drange(.5, 3.5, .25)[::-1],  # Entry:  2 , average:  18.5598556995
        drange(.5, 3.5, .33)[::-1],  # Entry:  3 , average:  19.8484629154
        drange(.5, 3.5, .4)[::-1],  # Entry:  4 , average:  9.07285785675
        drange(.5, 3.5, .5)[::-1],  # Entry:  5 , average:  7.03486213684

Entry:  [1.4544272552950825, 1.4999468776934912, 0.9468604987640873, 0.5] , average:  6.58254628181
Entry:  [1.3842433825360176, 1.1586458083190747, 1.3199182357287622, 1.3116942580989135, 1.087092750799022, 0.8987606216458575, 1.003575384552797, 0.7377380791777342, 1.0064815346777387, 0.8572236596049281, 0.5] , average:  11.5650449276
Entry:  [1.238402499270101, 1.3338622722189168, 0.6728636189105502, 0.5] , average:  5.30999367237
Entry:  [1.1678895200162993, 0.5] , average:  2.2317538023
Entry:  [1.00088637257158, 0.9374252178992696, 0.5] , average:  7.05354297161
Entry:  [1.0843239755455016, 0.5] , average:  3.45062289238
The best temperatures are:  [1.1678895200162993, 0.5]

















































The best temperatures are:  [2, 1.5, 1, 0.5]

