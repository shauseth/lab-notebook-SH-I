# SH-I

from urllib.request import urlopen
import xmltodict

# returns accession number given api url
def extract(request):

    file = urlopen(request)
    data = file.read()
    file.close()

    data = xmltodict.parse(data)

    acc_no = data['items']['accessionNumber']

    return acc_no

# iterate over offset and write accession numbers to file
file = open('acc_no3.txt', 'w')

list = list(range(111837))
list = list[87950:]

for offset in list:

    url = 'https://api.glytoucan.org/glycans/list?payload=id&limit=1&offset=' + str(offset)
    acc_no = extract(url)

    file.write(acc_no + '\n')

    print(str(offset) + '/111837 ' + acc_no + ' written to file.')

file.close()
