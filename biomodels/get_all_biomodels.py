# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 10:52:49 2022

@author: Lucian
"""

from bioservices import BioModels
s = BioModels()
#s.settings.TIMEOUT = 90

for i in range(1, 1065):
# for i in [505, 506]:
    if i in [649, 694, 992, 993]: #Don't exist
        continue
    num = f'{i:010d}'
    mod = "BIOMD" + num
    try:
        s.get_model_download(mod)
    except:
        print("Skipped model ", mod)

