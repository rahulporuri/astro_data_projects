# -*- coding: utf-8 -*-
"""
Created on Sun May 25 10:05:47 2014

@author: rahul.poruri
"""

import numpy as np
import matplotlib.pyplot as plt

data = [line.split() for line in open('Observers Handbook Table.dat')]

len(data)

j = 0
m_v = np.zeros(312)
for i in xrange(4,316):
    tmp = data[i][11]
    m_v[j] = tmp
    j += 1

j = 0
b_v = np.zeros(312)
for i in xrange(4,316):
    tmp = data[i][7]
    b_v[j] = tmp
    j += 1
    
plt.xlim(2,-1)    
plt.scatter(b_v,m_v,s=5)