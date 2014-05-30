# -*- coding: utf-8 -*-
"""
Created on Fri May 30 21:22:15 2014

@author: rahul.poruri
"""
import pandas as pd
import matplotlib.pyplot as plt

u_star = np.zeros(len(data))
g_star = np.zeros(len(data))
r_star = np.zeros(len(data))
i_star = np.zeros(len(data))
z_star = np.zeros(len(data))

for j in xrange(len(data)):
    if data['class'][j] == 'STAR':
        u_star[j] = data['u'][j]
        g_star[j] = data['g'][j]
        r_star[j] = data['r'][j]
        i_star[j] = data['i'][j]
        z_star[j] = data['z'][j]



u_g_star = np.zeros(len(data))
g_r_star = np.zeros(len(data))
r_i_star = np.zeros(len(data))
i_z_star = np.zeros(len(data))

u_g_star = u_star - g_star
g_r_star = g_star - r_star
r_i_star = r_star - i_star
i_z_star = i_star - z_star

plt.hold(True)
subplot(221)
plt.scatter(u_g_star,g_r_star,c='b')
plt.xlim(-10,10)
plt.ylim(-10,10)
subplot(222)
plt.scatter(g_r_star,r_i_star,c='b')
plt.xlim(-10,10)
plt.ylim(-10,10)
subplot(223)
plt.scatter(r_i_star,i_z_star,c='b')
plt.xlim(-10,10)
plt.ylim(-10,10)
subplot(224)
plt.scatter(r_i_star,g_star,c='b')
plt.xlim(-10,10)
plt.ylim(-10,10)