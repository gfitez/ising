#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 16:37:26 2023

@author: julianrubinfien
"""

import sys
import os
import time
import csv
import logging
# import click
import numpy as np
# import logging
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.animation import FuncAnimation
import time


name = 'data/test_'


f = open('data/1.60T3.60_EM_v2.csv_lattice.npy', 'rb')
lattices = np.load(f,allow_pickle=True)


# def latt_video(latt,name):
#     fig, ax = plt.subplots()
#     # xdata, ydata = [], []
#     # ln, = ax.plot([], [], 'ro')
#     sct = ax.imshow(latt[0],cmap=cm.Reds)
    
#     # def init():
#     #     ax.set_xlim(0, 2*np.pi)
#     #     ax.set_ylim(-1, 1)
#     #     return ln,
    
#     def update(frame,sct):
#         # xdata.append(frame)
#         # ydata.append(np.sin(frame))
#         # ln.set_data(xdata, ydata)
#         sct = ax.imshow(latt[frame],cmap=cm.Reds)
        
#         returns = [sct]
#         return tuple(returns)
    
#     ani = FuncAnimation(fig, update, frames=len(latt),interval=180,fargs=([sct]))
        
    
#     ani.save(name+'_lattvideo')

    
    

# if __name__ == "__main__":
#     latt_video(lattices,name)



import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()
a=lattices[0]
im=plt.imshow(a,interpolation='none')
ttl = ax.text(.5, 1.005, 'T=0', transform = ax.transAxes)
plt.axis('off')


def init():
    ttl.set_text('')
    im.set_data(lattices[0])
    return [im],[ttl]


def animate(i):
    ttl.set_text('T = ' +str(i))
    a=im.get_array()
    a=lattices[i]   # exponential decay of the values
    im.set_array(a)
    return [im],[ttl]

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(lattices)-1, interval=100,)

anim.save('lalalalalala.mp4', fps=15, extra_args=['-vcodec', 'libx264'])

# plt.savefig('lattice_animation.mp4')
