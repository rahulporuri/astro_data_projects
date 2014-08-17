# -*- coding: utf-8 -*-
"""
Created on Sun May 25 15:20:07 2014

@author: rahul.poruri
"""

import numpy as np
import matplotlib.pyplot as plt

data = [line.split() for line in open('hipparcos_stars_abridged.dat')]
b_v = np.zeros(len(data)-1)
M_v = np.zeros(len(data)-1)
for j in xrange(1,len(data)):
    b_v[j-1] = data[j][5]
    M_v[j-1] = data[j][6]

plt.scatter(b_v,M_v,s=5)
plt.ylim(20,-5)
plt.ylabel('V absolute magnitude')
plt.xlabel('B-V color')
plt.title('HR diagram for 5000 stars')
plt.show()
