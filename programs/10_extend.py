# SH-I

import pandas as pd
import os

rfu = pd.read_csv('cfg_data/sorted/glycans.csv')
dev = pd.read_csv('cfg_data/sorted/glycans.csv')

for filename in os.listdir('cfg_data/sorted/avg_rfu/'):

    file = pd.read_csv('cfg_data/sorted/avg_rfu/' + filename)

    try:

        avg_rfu = file['Average RFU']
        st_dev = file['StDev']

        rfu[filename] = avg_rfu
        dev[filename] = st_dev

    except:

        pass

rfu.to_csv('cfg_data/sorted/rfu.csv', index = False)
print('rfu.csv created.')

dev.to_csv('cfg_data/sorted/dev.csv', index = False)
print('dev.csv created.')
