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
    plt.imshow(mat,interpolation='nearest')
    plt.colorbar()
    #plt.savefig(title+'.png',bbox_inches='tight')

#def main():
#mesh
xnodes=np.arange(0,801,200)
znodes=np.arange(0,801,200)
nxcells=len(xnodes)-1
nzcells=len(znodes)-1
ncells=nxcells*nzcells
dimsT=(nxcells,nzcells)
dims=(nzcells,nxcells)

#data locations
#xlocs=[290,390,490,590]
n=20
xlocs=np.linspace(50,750,num=n)
zlocs=[-50]
n=len(xlocs)*len(zlocs)

#sensitivity matrix
Gorig=grav.sens2d(xnodes,znodes,xlocs,zlocs)

#true model
truemodel=np.zeros(dims)
truemodel[1,1]=2
truemodel[2,1]=0.5
truemodel=np.reshape(truemodel.T,[ncells,1])

#true data
truedata=Gorig.dot(truemodel)

#TODO: add noise
sd=0.1

#"true" density distribution
sigma=np.std(truemodel)
mean=np.mean(truemodel)
nmodels=1000000

validmodels=np.array([]).reshape(ncells,0)
#loop so as to discard unused random models
nloop=10
for i in range(0,nloop):
    #generate models
    randmodels=sigma*np.random.randn(ncells,nmodels)+mean
    
    #perform forward models
    randdata=np.dot(Gorig,randmodels)
    
    #calculate data misfits
    phid=np.linalg.norm((randdata-truedata)/sd, axis=0)**2
    isvalidmodel=np.where(phid <= n)
    newvalidmodels=randmodels[:,isvalidmodel]
    newvalidmodels=newvalidmodels.reshape([ncells,newvalidmodels.size//ncells])
    validmodels=np.append(validmodels,newvalidmodels,axis=1)
    print(i)
    #print((phid <= n).sum())
    
#get mean model?
meanmodel=np.mean(validmodels,axis=1).reshape(16,1)
plotmat(meanmodel.reshape(dims).T,'mean model',1)
#plt.imshow(meanmodel.reshape(dims),interpolation='nearest',vmin=-1,vmax=1)
varmodel=np.var(validmodels,axis=1).reshape(16,1)
#plt.imshow(varmodel.reshape(dims),interpolation='nearest')
plotmat(varmodel.reshape(dims).T,'var model',2)