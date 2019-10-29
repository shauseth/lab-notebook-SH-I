# SH-I

import pandas as pd
import numpy as np

def ham_dist(s1, s2):

    assert len(s1) == len(s2)

    dist = sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

    return dist

data = pd.read_csv('notebook/SS_unfiltered.txt', delim_whitespace = True, skiprows = [1])

print('Before:')
print(data)
print('')

data = data.reset_index()

ss = []

for x in data:

    if 'SS' in x:

        ss.append(x)

for x in ss:

    data = data.sort_values(x, ascending = False)
    data = data.reset_index(drop = 'True')

    seq1 = data.iloc[0, 1]

    count = list(range(len(data['Tag'])))
    count = count[1:]

    for x in count:

        seq2 = data.iloc[x, 1]

        try:

            dist = ham_dist(seq1, seq2)

        except AssertionError:

            pass

        if dist == 1:

            seq_list1 = list(data.loc[0])
            seq_list2 = list(data.loc[x])
            seq_arr1 = np.array(seq_list1[3:])
            seq_arr2 = np.array(seq_list2[3:])
            nam_list = seq_list1[:3]
            seq_list = list(seq_arr1 + seq_arr2)
            fin_list = nam_list + seq_list
            data.loc[0] = fin_list
            data = data.drop([x])
            data = data.reset_index(drop = 'True')

            del count[-1]

            print(data.head())
            print('Fixed row ' + str(x))

data = data.sort_values('index')
data = data.reset_index(drop = 'True')
del data['index']

print('After:')
print(data)
print('')

data.to_csv('SS_unfiltered_output.csv', index = False)
