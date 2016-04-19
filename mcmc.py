# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 17:57:47 2016

@author: Andy
"""

import numpy as np
import matplotlib.pylab as plt
import grav
    
def plotmat(mat,title,fignum):
    fig = plt.figure(fignum)
    fig.suptitle(title)
    ax = fig.add_subplot(1,1,1)
    ax.set_aspect('equal')
    #TODO: try using pcolormesh
#    plt.imshow(mat,interpolation='nearest',vmin=-1,vmax=1)#,cmap=plt.cm.Blues)
    plt.imshow(mat,interpolation='nearest',vmin=0,vmax=1)
    plt.colorbar()
    plt.savefig(title+'.png',bbox_inches='tight')

#def main():
#mesh
xnodes=np.arange(0,801,200)
znodes=np.arange(0,801,200)
nxcells=len(xnodes)-1
nzcells=len(znodes)-1
dimsT=(nxcells,nzcells)
dims=(nzcells,nxcells)

#data locations
#xlocs=[290,390,490,590]
n=10
xlocs=np.linspace(50,750,num=n)
zlocs=[-50]
n=len(xlocs)*len(zlocs)

Gorig=grav.sens2d(xnodes,znodes,xlocs,zlocs)

