# SH-I

import pandas as pd
import os
from urllib.request import urlopen
import cgi

def format(file):

    if 'Structure on Masterlist' and 'Average RFU' in file:

        return True

    else:

        return False

def getname(file):

    file = file.split('.')
    id = file[0]

    url = 'http://www.functionalglycomics.org/glycomics/HFileServlet?operation=downloadRawFile&fileType=DAT&sideMenu=no&objId=100' + id

    remotefile = urlopen(url)
    blah = remotefile.info()['Content-Disposition']
    value, params = cgi.parse_header(blah)
    name = params['filename']

    return name

for filename in os.listdir('data/'):

    try:

        file = pd.read_excel('data/' + filename)

        if format(file):

            file = file[['Chart Number', 'Structure on Masterlist', 'Average RFU', 'StDev', '% CV']]

            id = filename.split('.')
            id = id[0]

            name = getname(filename)
            name = name.split('.')
            name = name[0] + '_' + id + '.csv'

            file.to_csv('sorted/avg_rfu/' + name, index = False)

            print(name + ' created.')

    except:

        pass
