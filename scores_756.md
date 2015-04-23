
This file summarizes the running time averages to solve the planted problems with Ids <ids> given temperatures <temperatures> and with 588 sub graphs.

## Ids
ids = xrange(0, 500, 50)

## Temperatures and results

# Run on AWS GPU instance
temps = [
        # The best temperatures are:  [3, 2, 1, 0.5]
        [2, 1, .5],  # Entry:  0 , average:  17.9192103148
        [2, 1, .75, .5],  # Entry:  1 , average:  27.987347126
        [3, 2, 1, .5],  # Entry:  2 , average:  16.9272893906
        [3, 2.5, 2, 1, .5],  # Entry:  3 , average:  21.7558373213
        [2, 1.5, 1, .5],  # Entry:  4 , average:  21.2971575022
        [3, 2, 1.5, 1, .5],  # Entry:  5 , average:  24.0208431482
        [4, 3, 2, 1.5, 1, .5],  # Entry:  6 , average:  21.6820886135
        [5, 4, 3, 2, 1.5, 1, .5],  # Entry:  7 , average:  24.5345762014
        [3.2, 2.7, 2, 1.5, 1, .5],  # Entry:  8 , average:  27.1268676758
        drange(.5, 3, .1)[::-1],  # Entry:  9 , average:  101.317758703
        drange(.5, 3, .2)[::-1],  # Entry:  10 , average:  50.9078867674
        drange(.5, 3, .25)[::-1],  # Entry:  11 , average:  38.1286491871
        drange(.5, 3, .33)[::-1],  # Entry:  12 , average:  45.8691898346
        drange(.5, 3, .4)[::-1],  # Entry:  13 , average:  25.5480450153
        drange(.5, 3, .5)[::-1],  # Entry:  14 , average:  27.6276902676
        drange(.5, 4, .1)[::-1],  # Entry:  15 , average:  121.879967618
        drange(.5, 4, .2)[::-1],  # Entry:  16 , average:  65.7460227966
        drange(.5, 4, .25)[::-1],  # Entry:  17 , average:  54.7375143051
        drange(.5, 4, .33)[::-1],  # Entry:  18 , average:  54.5334163904
        drange(.5, 4, .4)[::-1],  # Entry:  19 , average:  38.0078181505
        drange(.5, 4, .5)[::-1],  # Entry:  20 , average:  23.1117534637
        drange(.5, 5, .1)[::-1],  # Entry:  21 , average:  156.02460804
        drange(.5, 5, .2)[::-1],  # Entry:  22 , average:  97.3032204151
        drange(.5, 5, .25)[::-1],  # Entry:  23 , average:  59.2537629604
        drange(.5, 5, .33)[::-1],  # Entry:  24 , average:  62.7818203211
        drange(.5, 5, .4)[::-1],  # Entry:  25 , average:  62.7669960022
        drange(.5, 5, .5)[::-1],  # Entry:  26 , average:  36.1748129129
        drange(.5, 6, .1)[::-1],  # Entry:  27 , average:  164.399077511
        drange(.5, 6, .2)[::-1],  # Entry:  28 , average:  119.188174939
        drange(.5, 6, .25)[::-1],  # Entry:  29 , average:  74.6345351219
        drange(.5, 6, .33)[::-1],  # Entry:  30 , average:  64.8591336012
        drange(.5, 6, .4)[::-1],  # Entry:  31 , average:  70.5316184044
        drange(.5, 6, .5)[::-1],  # Entry:  32 , average:  55.2777708769
        drange(.5, 7, .1)[::-1],  # Entry:  33 , average:  218.946008921
        drange(.5, 7, .2)[::-1],  # Entry:  34 , average:  169.821253872
        drange(.5, 7, .25)[::-1],  # Entry:  35 , average:  95.2680874586
        drange(.5, 7, .33)[::-1],  # Entry:  36 , average:  98.0495764732
        drange(.5, 7, .4)[::-1],  # Entry:  37 , average:  107.482244349
        drange(.5, 7, .5)[::-1],  # Entry:  38 , average:  68.9593253374
    ]

