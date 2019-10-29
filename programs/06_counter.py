# SH-I

import pandas as pd
import os

def format(file):

    if 'Structure on Masterlist' and 'AvgMeanS-B w/o MIN/MAX' in file:

        return True

    else:

        return False

count = 0

for filename in os.listdir('data/'):

    try:

        file = pd.read_excel('data/' + filename)

        if format(file):

            count = count + 1

            print(count)

    except:

        pass
