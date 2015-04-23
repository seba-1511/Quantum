
This file summarizes the running time averages to solve the planted problems with Ids <ids> given temperatures <temperatures> and with 588 sub graphs.

## Ids
ids = xrange(0, 500, 50)

## Temperatures and results

# Run on AWS GPU instance
temps = [
        # The best temperatures are:  [2, 1, 0.5]
        [2, 1, .5],  # Entry:  0 , average:  13.3117861748
        [2, 1, .75, .5],  # Entry:  1 , average:  20.2947582483
        [3, 2, 1, .5],  # Entry:  2 , average:  17.4434875727
        [3, 2.5, 2, 1, .5],  # Entry:  3 , average:  19.547585392
        [2, 1.5, 1, .5],  # Entry:  4 , average:  20.8302713871
        [3, 2, 1.5, 1, .5],  # Entry:  5 , average:  19.3308734655
        [4, 3, 2, 1.5, 1, .5],  # Entry:  6 , average:  14.8875025034
        [5, 4, 3, 2, 1.5, 1, .5],  # Entry:  7 , average:  27.8071509838
        [3.2, 2.7, 2, 1.5, 1, .5],  # Entry:  8 , average:  20.2458056211
        drange(.5, 3, .1)[::-1],  # Entry:  9 , average:  60.7998099327
        drange(.5, 3, .2)[::-1],  # Entry:  10 , average:  38.2872646093
        drange(.5, 3, .25)[::-1],  # Entry:  11 , average:  38.3439232111
        drange(.5, 3, .33)[::-1],  # Entry:  12 , average:  44.2030246019
        drange(.5, 3, .4)[::-1],  # Entry:  13 , average:  17.6037395954
        drange(.5, 3, .5)[::-1],  # Entry:  14 , average:  30.0171941996
        drange(.5, 4, .1)[::-1],  # Entry:  15 , average:  114.104996014
        drange(.5, 4, .2)[::-1],  # Entry:  16 , average:  41.3118901491
        drange(.5, 4, .25)[::-1],  # Entry:  17 , average:  32.4862995148
        drange(.5, 4, .33)[::-1],  # Entry:  18 , average:  33.488809824
        drange(.5, 4, .4)[::-1],  # Entry:  19 , average:  27.7889359951
        drange(.5, 4, .5)[::-1],  # Entry:  20 , average:  25.9325739861
        drange(.5, 5, .1)[::-1],  # Entry:  21 , average:  141.376545811
        drange(.5, 5, .2)[::-1],  # Entry:  22 , average:  55.319022584
        drange(.5, 5, .25)[::-1],  # Entry:  23 , average:  52.4933824778
        drange(.5, 5, .33)[::-1],  # Entry:  24 , average:  52.3246892691
        drange(.5, 5, .4)[::-1],  # Entry:  25 , average:  38.026649189
        drange(.5, 5, .5)[::-1],  # Entry:  26 , average:  31.1827017784
        drange(.5, 6, .1)[::-1],  # Entry:  27 , average:  103.698758221
        drange(.5, 6, .2)[::-1],  # Entry:  28 , average:  106.287009883
        drange(.5, 6, .25)[::-1],  # Entry:  29 , average:  48.9025055885
        drange(.5, 6, .33)[::-1],  # Entry:  30 , average:  47.3761648655
        drange(.5, 6, .4)[::-1],  # Entry:  31 , average:  40.2947982788
        drange(.5, 6, .5)[::-1],  # Entry:  32 , average:  29.0548914194
        drange(.5, 7, .1)[::-1],  # Entry:  33 , average:  110.649698639
        drange(.5, 7, .2)[::-1],  # Entry:  34 , average:  78.7636207342
        drange(.5, 7, .25)[::-1],  # Entry:  35 , average:  45.1702190161
        drange(.5, 7, .33)[::-1],  # Entry:  36 , average:  65.0479057312
        drange(.5, 7, .4)[::-1],  # Entry:  37 , average:  28.2847656965
        drange(.5, 7, .5)[::-1],  # Entry:  38 , average:  26.6654751301
    ]

