# SH-1

import urllib.request

id_list = list(range(10000))

prefix = 'http://www.functionalglycomics.org/glycomics/HFileServlet?operation=downloadRawFile&fileType=DAT&sideMenu=no&objId=100'

for num in id_list:

    id = str(num).zfill(4)

    url = prefix + id

    try:

        urllib.request.urlretrieve(url, '/Users/derdalab/Desktop/shau/data/extra' + id + '.xls')

        print(id + ' downloaded.')

    except:

        pass
