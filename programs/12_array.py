# SH-I

import pandas as pd
import numpy as np

data = pd.read_csv('SS_unfiltered_output.csv')
data.set_index('Tag', inplace = True)
del data['X']

col_list = []

for x in data:

    if 'SS' in x:

        col_list.append(x)

for col_name in col_list:

    data = data.sort_values(col_name, ascending = False)

    seq_dict = dict(data[col_name])
    seq_sum = np.sum(data[col_name])

    out_dict = {}

    for x in seq_dict:

        perc = (seq_dict[x] / seq_sum) * 100

        if perc > 0.1:

            out_dict.update({x : seq_dict[x]})

    output = pd.DataFrame(list(out_dict.items()), columns = ['Tag', 'Reads'])

    print(col_name)
    print(output)
    print('')

    # output.to_csv('output2/' + col_name + '.csv', index = False)
