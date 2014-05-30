# -*- coding: utf-8 -*-
"""
Created on Fri May 30 21:47:04 2014

@author: rahul.poruri
"""

import pandas as pd
import matplotlib.pyplot as plt

l_galaxy = np.zeros(len(data))
b_galaxy = np.zeros(len(data))

for j in xrange(len(data)):
    if data['class'][j] == 'GALAXY':
        l_galaxy[j] = data['l'][j]
        b_galaxy[j] = data['b'][j]



l_galaxy = (l_galaxy-180)*(np.pi/180)
b_galaxy = b_galaxy*(np.pi/180)
subplot(111,projection="aitoff")
plt.scatter(l_galaxy,b_galaxy,c='g')


