# -*- coding: utf-8 -*-
"""
Created on Tue Jun 03 10:51:06 2014

@author: rahul.poruri
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 09 17:02:45 2014

@author: rahul.poruri
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('first_set.csv')

redshift = []
u, g, r, i, z = [], [], [], [], []
u_g, g_r, r_i, i_z = [], [], [], []

ra, dec = [], []

redshift = data['z']
u, g, r, i, z = data['modelMag_u'], data['modelMag_g'], data['modelMag_r'], data['modelMag_i'], data['modelMag_z']
u_g, g_r, r_i, i_z = data['modelMag_u'] - data['modelMag_g'], data['modelMag_g'] - data['modelMag_r'], data['modelMag_r'] - data['modelMag_i'], data['modelMag_i'] - data['modelMag_z']
ra, dec = data['ra'], data['dec']

'''
plt.hold(True)

plt.subplot(221)
plt.ylim(-4,5)
plt.scatter(redshift, u_g, s=4)
plt.ylabel('u-g')

plt.subplot(222)
plt.ylim(-4,5)
plt.scatter(redshift, g_r, s=4)
plt.ylabel('g-r')

plt.subplot(223)
plt.ylim(-4,5)
plt.scatter(redshift, r_i, s=4)
plt.ylabel('r-i')
plt.xlabel('redshift')

plt.subplot(224)
plt.ylim(-4,5)
plt.scatter(redshift, i_z, s=4)
plt.ylabel('i-z')
plt.xlabel('redshift')

plt.show()

"""
plt.hold(True)

subplot(221)
plt.xlim(-0.5,3)
plt.ylim(-0.5,1.5)
plt.scatter(u_g, g_r, s=4)

subplot(222)
plt.xlim(-1,2)
plt.ylim(-0.5,1.5)
plt.scatter(g_r, r_i, s=4)

subplot(223)
plt.xlim(-0.5,2)
plt.ylim(-0.5,1)
plt.scatter(r_i, i_z, s=4)

subplot(224)

'''

ra = (ra-180)*np.pi/180
dec = dec*np.pi/180

plt.subplot(111,projection='aitoff')
plt.scatter(ra,dec)
plt.grid(True)
plt.show()
