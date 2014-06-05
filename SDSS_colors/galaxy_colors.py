# -*- coding: utf-8 -*-
"""
Created on Fri May 30 21:12:00 2014

@author: rahul.poruri
"""

import pandas as pd
import matplotlib.pyplot as plt

u_galaxy = np.zeros(len(data))
g_galaxy = np.zeros(len(data))
r_galaxy = np.zeros(len(data))
i_galaxy = np.zeros(len(data))
z_galaxy = np.zeros(len(data))

for j in xrange(len(data)):
    if data['class'][j] == 'GALAXY':
        u_galaxy[j] = data['u'][j]
        g_galaxy[j] = data['g'][j]
        r_galaxy[j] = data['r'][j]
        i_galaxy[j] = data['i'][j]
        z_galaxy[j] = data['z'][j]



u_g_galaxy = np.zeros(len(data))
g_r_galaxy = np.zeros(len(data))
r_i_galaxy = np.zeros(len(data))
i_z_galaxy = np.zeros(len(data))

u_g_galaxy = u_galaxy - g_galaxy
g_r_galaxy = g_galaxy - r_galaxy
r_i_galaxy = r_galaxy - i_galaxy
i_z_galaxy = i_galaxy - z_galaxy



plt.hold(True)
subplot(221)
plt.scatter(u_g_galaxy,g_r_galaxy,c='g')
plt.xlim(-10,10)
plt.ylim(-10,10)
subplot(222)
plt.scatter(g_r_galaxy,r_i_galaxy,c='g')
plt.xlim(-10,10)
plt.ylim(-10,10)
subplot(223)
plt.scatter(r_i_galaxy,i_z_galaxy,c='g')
plt.xlim(-10,10)
plt.ylim(-10,10)
subplot(224)
plt.scatter(r_i_star,g_star,c='b')
plt.xlim(-10,10)
plt.ylim(-10,10)
