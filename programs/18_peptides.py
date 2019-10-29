# SH-I

import pandas as pd
import numpy as np

from urllib.request import urlopen

def psId(term):

    """Returns primscreen ID given protein name."""

    html = urlopen('http://www.functionalglycomics.org/glycomics/search/jsp/result.jsp?query=' + term + '&cat=all')

    page = str(html.read())
    page_list = page.split('/glycomics/HServlet?operation=view&sideMenu=no&psId=')[1]

    return page_list.split('"')[0]

def cbpId(psid):

    """Returns carbohydrate binding protein ID given primscreen ID."""

    html = urlopen('http://www.functionalglycomics.org/glycomics/HServlet?operation=view&sideMenu=no&psId=' + psid)
    page = str(html.read())

    cbpid = page.split('cbpId=')[1]
    cbpid = cbpid.split('&sideMenu=no')[0]

    return cbpid

def seq(cbpid):

    """Returns peptide sequence given CBD ID."""

    html = urlopen('http://www.functionalglycomics.org/glycomics/GBPServlet?pageType=view&view=view&operationType=view&cbpId=' + cbpid + '&sideMenu=no')
    page = str(html.read())

    seq = page.split('align="left" class="rightSideEqualWidth">')[1]
    seq = seq.split('</td>')[0]
    seq = ' '.join(seq.split('&nbsp;'))
    seq = ' '.join(seq.split('<br>'))

    return seq
