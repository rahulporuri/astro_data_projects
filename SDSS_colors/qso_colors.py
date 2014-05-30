# -*- coding: utf-8 -*-
"""
Created on Fri May 30 21:16:55 2014

@author: rahul.poruri
"""
import pandas as pd
import matplotlib.pyplot as plt

u_qso = np.zeros(len(data))
g_qso = np.zeros(len(data))
r_qso = np.zeros(len(data))
i_qso = np.zeros(len(data))
z_qso = np.zeros(len(data))

for j in xrange(len(data)):
    if data['class'][j] == 'QSO':
        u_qso[j] = data['u'][j]
        g_qso[j] = data['g'][j]
        r_qso[j] = data['r'][j]
        i_qso[j] = data['i'][j]
        z_qso[j] = data['z'][j]



u_g_qso = np.zeros(len(data))
g_r_qso = np.zeros(len(data))
r_i_qso = np.zeros(len(data))
i_z_qso = np.zeros(len(data))

u_g_qso = u_qso - g_qso
g_r_qso = g_qso - r_qso
r_i_qso = r_qso - i_qso
i_z_qso = i_qso - z_qso

plt.hold(True)
subplot(221)
plt.scatter(u_g_qso,g_r_qso,c='r')
plt.xlim(-10,10)
plt.ylim(-10,10)
subplot(222)
plt.scatter(g_r_qso,r_i_qso,c='r')
plt.xlim(-10,10)
plt.ylim(-10,10)
subplot(223)
plt.scatter(r_i_qso,i_z_qso,c='r')
plt.xlim(-10,10)
plt.ylim(-10,10)
subplot(224)
plt.scatter(r_i_qso,g_qso,c='r')
plt.xlim(-10,10)
plt.ylim(-10,10)