# SH-I

import pandas as pd
import numpy as np
import os

# enter input file here
input = '20180530-87CLooOO-JM-ppm.txt'

# fixes sequences 1 hamming distance away
def ham_dist(s1, s2):

    assert len(s1) == len(s2)

    dist = sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

    return dist

data = pd.read_csv(input, delim_whitespace = True, skiprows = [1])

print('Before:')
print(data)
print('')

data = data.reset_index()

col_list = []

for x in data:

    if '1-' in x:

        col_list.append(x)

for x in col_list:

    data = data.sort_values(x, ascending = False)
    data = data.reset_index(drop = 'True')

    seq1 = data.iloc[0, 1]

    count = list(range(len(data['Nuc'])))
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

# fixes overlapping
data.set_index('Nuc', inplace = True)
del data['AA']

for x in range(len(data.columns)):

    data.iloc[x] = data.iloc[x].where(data.iloc[x] == data.iloc[x].max(), 0)

    print('Row ' + str(x) + ' fixed.')

# makes arrays and saves them as files
os.mkdir(input[:-4])

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

    output.to_csv(input[:-4] + '/' + col_name + '.csv', index = False)
