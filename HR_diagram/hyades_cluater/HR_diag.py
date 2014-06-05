# -*- coding: utf-8 -*-
"""
Created on Sun May 25 15:48:58 2014

@author: rahul.poruri
"""

import numpy as np
import matplotlib.pyplot as plt

data = [line.split() for line in open('tablea1.dat')]
b_v = np.zeros(len(data))
M_v = np.zeros(len(data))
for j in xrange(1,len(data)):
    b_v[j] = data[j][13]
    M_v[j] = data[j][17]

plt.scatter(b_v,M_v,s=5)
plt.xlim(4,3.5)
plt.show()
