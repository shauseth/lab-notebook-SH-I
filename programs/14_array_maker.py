# SH-I

import pandas as pd
import numpy as np
import os

# enter input file here
input = '20180222-87CLooPA-MR-ppm.txt'
overlap = True

data = pd.read_csv(input, delim_whitespace = True)
data.set_index('Nuc', inplace = True)

try:

    os.mkdir(input[:-4])

except:

    pass

# fixes sequences 1 hamming distance away
def ham_dist(s1, s2):

    assert len(s1) == len(s2)

    dist = sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

    return dist

col_list = []

for x in data:

    col_list.append(x)

for x in col_list:

    data = data.sort_values(x, ascending = False)

    seq1 = data.index[0]

    count = list(range(len(data)))[1:]

    for x in count:

        seq2 = data.index[x]

        try:

            dist = ham_dist(seq1, seq2)

        except AssertionError:

            dist = None

        if dist == 0 or dist == 1:

            data.iloc[0] = np.array(data.iloc[0]) + np.array(data.iloc[x])
            data = data.drop([seq2])

            del count[-1]

            print(data)
            print('')

data.to_csv(input[:-4] + '/' + input[:-4] + '_ham' + '.txt', sep = '\t')

# fixes overlapping
if overlap == True:

    for x in range(len(data.columns)):

        data.iloc[x] = data.iloc[x].where(data.iloc[x] == data.iloc[x].max(), 0)

    print(data)
    print('Removed overlapping.')
    print('')

data.to_csv(input[:-4] + '/' + input[:-4] + '_lap' + '.txt', sep = '\t')

# makes arrays and saves them as files
for col_name in col_list:

    data = data.sort_values(col_name, ascending = False)

    seq_dict = dict(data[col_name])
    seq_sum = np.sum(data[col_name])

    out_dict = {}

    for x in seq_dict:

        perc = (seq_dict[x] / seq_sum) * 100

        if perc > 0.1:

            out_dict.update({x : seq_dict[x]})

    output = pd.DataFrame(list(out_dict.items()), columns = ['DNA', 'Reads'])

    print(col_name)
    print(output)
    print('')

    output.to_csv(input[:-4] + '/' + col_name + '.txt', index = False, sep='\t')

print('Files saved to ' + input[:-4] + '.')
