import sys
import numpy as np
import scipy 
import matplotlib.pyplot as plt
from matplotlib import  transforms

def cum(phi): 
    return 0.5*(1-np.cos(phi/2))
   
def invcum(y):
    return  2*np.arccos(1-2*y)

def random_walk2d(step, N):
    deltax=np.array([0])
    deltay=np.array([0])
    tmpx=0
    tmpy=0
    for c in range(0,N+1):
        phi=np.random.uniform(low=0, high=2*np.pi)
        tmpx = tmpx+step*np.cos(phi)
        tmpy = tmpy+step*np.sin(phi)
        deltax=np.append(deltax, tmpx)
        deltay=np.append(deltay, tmpy)
    return deltax, deltay

def random_walkphi(step, N):
    deltax=np.array([0])
    deltay=np.array([0])
    tmpx=0
    tmpy=0
    for c in range(0,N+1):
        phi=invcum(np.random.random())
        tmpx = tmpx+step*np.cos(phi)
        tmpy = tmpy+step*np.sin(phi)

        deltax=np.append(deltax, tmpx)
        deltay=np.append(deltay, tmpy)

    return deltax, deltay

def random_walkas(step,s):
    deltax=np.array([0])
    deltay=np.array([0])
    tmpx=0
    tmpy=0
    while(tmpx<200*s):
        phi=np.random.uniform(low=0, high=2*np.pi)
        tmpx = tmpx+step*np.cos(phi)+s
        tmpy = tmpy+step*np.sin(phi)
        deltay=np.append(deltay, tmpy)
        deltax=np.append(deltax, tmpx)

    return deltax, deltay
