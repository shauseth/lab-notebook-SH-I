# SH-I

import requests

def getname(acc_no):

    url = 'https://glytoucan.org/Structures/Glycans/' + acc_no

    page = requests.get(url).content

    try:
        IUPAC_list = str(page).split('The IUPAC representation is ')
        IUPAC_list = IUPAC_list[1]
        IUPAC_list = IUPAC_list.split('.  The')
        IUPAC = IUPAC_list[0]
    except:
        IUPAC = None

    try:
        WURCS_list = str(page).split('The WURCS representation is ')
        WURCS_list = WURCS_list[1]
        WURCS_list = WURCS_list.split('.  It')
        WURCS = WURCS_list[0]
    except:
        WURCS = None

    return IUPAC, WURCS
