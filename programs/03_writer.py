# SH-I

import pandas as pd
from get import getname

file = open('acc_no2.txt', 'r')

data = file.read()
lines = data.split('\n')

data = pd.DataFrame(columns = ['acc_no', 'IUPAC', 'WURCS'])
data.to_csv('data2.csv', index = False)

for i, acc_no in enumerate(lines):

    IUPAC, WURCS = getname(acc_no)

    row = [acc_no, IUPAC, WURCS]

    line = pd.DataFrame(columns = ['acc_no', 'IUPAC', 'WURCS'])

    line.loc[0] = row

    line.to_csv('data2.csv', index = False, header = False, mode = 'a')

    print(line.loc[0])

file.close()
