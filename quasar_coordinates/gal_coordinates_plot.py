# -*- coding: utf-8 -*-
"""
Created on Wed May 28 22:38:35 2014

@author: rahul.poruri
"""

import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv('MyTable_rahul.poruri.csv')

l = np.zeros(len(data1['l']))
b = np.zeros(len(data1['b']))
l = data1['l']
b = data1['b']
# l is the galactic longitude and b is the galactic latitude

l = (l-180)*(np.pi/180)
b = b*(np.pi/180)

# for the matplotlib projection, 
# lat & long need to be (-np.pi/2,np.pi/2) & (-np.pi,np.pi)
# looking at the data, lat is already (-90,90)
# long is (0,360)

subplot(111,projection="aitoff")
plt.scatter(l,b,s=5)
plt.grid(True)
plt.title('Quasars from the SDSS DR10')
plt.xlabel('galactic longitude')
plt.ylabel('galactic latitude')