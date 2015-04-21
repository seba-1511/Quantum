
This file summarizes the running time averages to solve the planted problems with Ids <ids> given temperatures <temperatures> and with 588 sub graphs.

## Ids
ids = xrange(0, 500, 50)

## Temperatures and results

# Run on AWS GPU instance
temps = [
        # The best temperatures are:  [2, 1, 0.5]
        [2, 1, .5],  # Entry:  0 , average:  15.3685964346
        [2, 1, .75, .5],  # Entry:  1 , average:  19.8669018507
        [3, 2, 1, .5],  # Entry:  2 , average:  17.6105135918
        [3, 2.5, 2, 1, .5],  # Entry:  3 , average:  21.4417240143
        [2, 1.5, 1, .5],  # Entry:  4 , average:  19.4092168331
        [3, 2, 1.5, 1, .5],  # Entry:  5 , average:  24.1840399981
        [4, 3, 2, 1.5, 1, .5],  # Entry:  6 , average:  30.3767854691
        [5, 4, 3, 2, 1.5, 1, .5],  # Entry:  7 , average:  35.944064784
        [3.2, 2.7, 2, 1.5, 1, .5],  # Entry:  8 , average:  25.4134469032
        drange(.5, 3, .1)[::-1],  # Entry:  9 , average:  111.737824059
        drange(.5, 3, .2)[::-1],  # Entry:  10 , average:  59.3564682722
        drange(.5, 3, .25)[::-1],  # Entry:  11 , average:  45.235802865
        drange(.5, 3, .33)[::-1],  # Entry:  12 , average:  30.1120203733
        drange(.5, 3, .4)[::-1],  # Entry:  13 , average:  29.6640365601
        drange(.5, 3, .5)[::-1],  # Entry:  14 , average:  23.3694049358
        drange(.5, 4, .1)[::-1],  # Entry:  15 , average:  144.529934049
        drange(.5, 4, .2)[::-1],  # Entry:  16 , average:  78.0310699463
        drange(.5, 4, .25)[::-1],  # Entry:  17 , average:  60.9302085161
        drange(.5, 4, .33)[::-1],  # Entry:  18 , average:  46.2621415377
        drange(.5, 4, .4)[::-1],  # Entry:  19 , average:  44.5459289789
        drange(.5, 4, .5)[::-1],  # Entry:  20 , average:  30.9322038889
        drange(.5, 5, .1)[::-1],  # Entry:  21 , average:  208.89668119
        drange(.5, 5, .2)[::-1],  # Entry:  22 , average:  104.638516068
        drange(.5, 5, .25)[::-1],  # Entry:  23 , average:  87.8461539745
        drange(.5, 5, .33)[::-1],  # Entry:  24 , average:  64.1122633696
        drange(.5, 5, .4)[::-1],  # Entry:  25 , average:  58.0607526064
        drange(.5, 5, .5)[::-1],  # Entry:  26 , average:  41.0190564156
        drange(.5, 6, .1)[::-1],  # Entry:  27 , average:  247.497789979
        drange(.5, 6, .2)[::-1],  # Entry:  28 , average:  152.874437404
        drange(.5, 6, .25)[::-1],  # Entry:  29 , average:  100.213347173
        drange(.5, 6, .33)[::-1],  # Entry:  30 , average:  77.9461653233
        drange(.5, 6, .4)[::-1],  # Entry:  31 , average:  71.7391978979
        drange(.5, 6, .5)[::-1],  # Entry:  32 , average:  50.5663568735
        drange(.5, 7, .1)[::-1],  # Entry:  33 , average:  240.125065494
        drange(.5, 7, .2)[::-1],  # Entry:  34 , average:  168.154844546
        drange(.5, 7, .25)[::-1],  # Entry:  35 , average:  80.3812600851
        drange(.5, 7, .33)[::-1],  # Entry:  36 , average:  89.6496969938
        drange(.5, 7, .4)[::-1],  # Entry:  37 , average:  61.1941177845
        drange(.5, 7, .5)[::-1],  # Entry:  38 , average:  67.0168669939
    ]








































