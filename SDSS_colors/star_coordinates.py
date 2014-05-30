# -*- coding: utf-8 -*-
"""
Created on Fri May 30 21:46:41 2014

@author: rahul.poruri
"""

import pandas as pd
import matplotlib.pyplot as plt

l_star = np.zeros(len(data))
b_star = np.zeros(len(data))

for j in xrange(len(data)):
    if data['class'][j] == 'STAR':
        l_star[j] = data['l'][j]
        b_star[j] = data['b'][j]



l_star = (l_star-180)*(np.pi/180)
b_star = b_star*(np.pi/180)
subplot(111,projection="aitoff")
plt.scatter(l_star,b_star,c='b')