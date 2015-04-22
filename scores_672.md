
This file summarizes the running time averages to solve the planted problems with Ids <ids> given temperatures <temperatures> and with 588 sub graphs.

## Ids
ids = xrange(0, 500, 50)

## Temperatures and results

# Run on AWS GPU instance
temps = [
        # The best temperatures are:  [3, 2, 1, 0.5]
        [2, 1, .5],  # Entry:  0 , average:  15.2410852909
        [2, 1, .75, .5],  # Entry:  1 , average:  14.766379714
        [3, 2, 1, .5],  # Entry:  2 , average:  14.6987720966
        [3, 2.5, 2, 1, .5],  # Entry:  3 , average:  17.3893284798
        [2, 1.5, 1, .5],  # Entry:  4 , average:  15.2226057053
        [3, 2, 1.5, 1, .5],  # Entry:  5 , average:  18.397781229
        [4, 3, 2, 1.5, 1, .5],  # Entry:  6 , average:  24.0462519169
        [5, 4, 3, 2, 1.5, 1, .5],  # Entry:  7 , average:  32.3054955244
        [3.2, 2.7, 2, 1.5, 1, .5],  # Entry:  8 , average:  17.140175128
        drange(.5, 3, .1)[::-1],  # Entry:  9 , average:  89.4734609127
        drange(.5, 3, .2)[::-1],  # Entry:  10 , average:  48.3417559624
        drange(.5, 3, .25)[::-1],  # Entry:  11 , average:  34.6096319914
        drange(.5, 3, .33)[::-1],  # Entry:  12 , average:  30.2454355478
        drange(.5, 3, .4)[::-1],  # Entry:  13 , average:  25.0958607912
        drange(.5, 3, .5)[::-1],  # Entry:  14 , average:  20.4520806789
        drange(.5, 4, .1)[::-1],  # Entry:  15 , average:  126.450303721
        drange(.5, 4, .2)[::-1],  # Entry:  16 , average:  67.5963629484
        drange(.5, 4, .25)[::-1],  # Entry:  17 , average:  49.9108476877
        drange(.5, 4, .33)[::-1],  # Entry:  18 , average:  30.6254048109
        drange(.5, 4, .4)[::-1],  # Entry:  19 , average:  29.1750827789
        drange(.5, 4, .5)[::-1],  # Entry:  20 , average:  23.860293746
        drange(.5, 5, .1)[::-1],  # Entry:  21 , average:  179.288570452
        drange(.5, 5, .2)[::-1],  # Entry:  22 , average:  96.5463027
        drange(.5, 5, .25)[::-1],  # Entry:  23 , average:  54.7726613283
        drange(.5, 5, .33)[::-1],  # Entry:  24 , average:  57.4518375158
        drange(.5, 5, .4)[::-1],  # Entry:  25 , average:  48.2985672951
        drange(.5, 5, .5)[::-1],  # Entry:  26 , average:  31.1694227695
        drange(.5, 6, .1)[::-1],  # Entry:  27 , average:  195.949162841
        drange(.5, 6, .2)[::-1],  # Entry:  28 , average:  114.393844271
        drange(.5, 6, .25)[::-1],  # Entry:  29 , average:  68.9995627642
        drange(.5, 6, .33)[::-1],  # Entry:  30 , average:  70.5538904428
        drange(.5, 6, .4)[::-1],  # Entry:  31 , average:  51.8974025011
        drange(.5, 6, .5)[::-1],  # Entry:  32 , average:  38.162510848
        drange(.5, 7, .1)[::-1],  # Entry:  33 , average:  193.638475227
        drange(.5, 7, .2)[::-1],  # Entry:  34 , average:  111.440070057
        drange(.5, 7, .25)[::-1],  # Entry:  35 , average:  91.3522358894
        drange(.5, 7, .33)[::-1],  # Entry:  36 , average:  69.2202715635
        drange(.5, 7, .4)[::-1],  # Entry:  37 , average:  64.0315629005
        drange(.5, 7, .5)[::-1],  # Entry:  38 , average:  38.115746212
    ]







































