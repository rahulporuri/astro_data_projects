# -*- coding: utf-8 -*-
"""
Created on Fri May 30 21:46:55 2014

@author: rahul.poruri
"""

import pandas as pd
import matplotlib.pyplot as plt

l_qso = np.zeros(len(data))
b_qso = np.zeros(len(data))

for j in xrange(len(data)):
    if data['class'][j] == 'QSO':
        l_qso[j] = data['l'][j]
        b_qso[j] = data['b'][j]



l_qso = (l_qso-180)*(np.pi/180)
b_qso = b_qso*(np.pi/180)
subplot(111,projection="aitoff")
plt.scatter(l_qso,b_qso,c='r')