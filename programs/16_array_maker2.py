# SH-I

import pandas as pd
import numpy as np
import os

from tqdm import tqdm

filename = '20180222-87CLooPA-MR-ppm'

data = pd.read_csv(filename + '.txt', delim_whitespace = True)
data.set_index('Nuc', inplace = True)

try:

    os.mkdir(filename)

except:

    pass

def ham_dist(s1, s2):

    assert len(s1) == len(s2)

    dist = sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

    return dist

def lev_dist(s1, s2):

    if len(s1) > len(s2):

        s1, s2 = s2, s1

    distances = range(len(s1) + 1)

    for i2, c2 in enumerate(s2):

        distances_ = [i2 + 1]

        for i1, c1 in enumerate(s1):

            if c1 == c2:

                distances_.append(distances[i1])

            else:

                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))

        distances = distances_

    return distances[-1]

for col in data:

    col_df = data[col].sort_values(ascending = False)
    col_df = col_df[col_df > 0] # remove less than

    n_list = range(len(col_df) - 2, -1, -1)

    for n in tqdm(n_list):

        seq1 = col_df.index[n]

        count = range(len(col_df) - 1, n, -1)

        for x in count:

            seq2 = col_df.index[x]

            try:

                dist = ham_dist(seq1, seq2)

            except AssertionError:

                dist = None

            if dist == 0 or dist == 1:

                col_df[n] = col_df[n] + col_df[x]
                col_df[x] = 0

    col_df = col_df[col_df > 0]
    col_df = col_df.sort_values(ascending = False)

    n_list = range(len(col_df) - 2, -1, -1)

    for n in tqdm(n_list):

        seq1 = col_df.index[n]

        count = range(len(col_df) - 1, n, -1)

        for x in count:

            seq2 = col_df.index[x]

            dist = lev_dist(seq1, seq2)

            if dist == 1:

                col_df[n] = col_df[n] + col_df[x]
                col_df[x] = 0

    arr_df = pd.Series()
    val_sum = np.sum(col_df)

    for seq, val in col_df.items():

        perc = (val / val_sum) * 100

        if perc > 0.1: # top percentage

            arr_df[seq] = val

    arr_df = arr_df.astype(int)

    arr_df.to_csv(filename + '/' + col + '.txt', sep = '\t', header = False)

    print(arr_df)
    print(col + '.txt created.')
    print('')
