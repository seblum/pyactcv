# -*- coding: utf-8 -*-
"""
2021-08-20

@author: seblum
"""

from . import actr
import requests
import re

def getFilename_fromCd(cd):
    
"""
Get filename from content-disposition
"""
if not cd:
return None
fname = re.findall('filename=(.+)', cd)
if len(fname) == 0:
return None
return fname[0]


url = 'http://act-r.psy.cmu.edu/actr7.x/win-standalone.zip'
r = requests.get(url, allow_redirects=True)
filename = getFilename_fromCd(r.headers.get('content-disposition'))
open(filename, 'wb').write(r.content)