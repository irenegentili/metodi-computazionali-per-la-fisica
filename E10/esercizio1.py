import randomwalk2 as rm
import sys
import numpy as np
import scipy 
import matplotlib.pyplot as plt
from matplotlib import  transforms

color=['blue', 'magenta', 'red', 'green', 'black']
for i in range(5):
    plt.plot(rm.random_walk2d(8, 1000)[0], rm.random_walk2d(8, 1000)[1], color=color[i])
    plt.xlabel(r'$\Delta x$')
    plt.ylabel(r'$\Delta y$')
    plt.show()
plt.show()

passi=[10,100,1000]

for i in range(3):
    for j in range(100):
        x, y= rm.random_walk2d(1,passi[i])
        plt.plot(x[-1],y[-1], '-o' , color=color[i])
        plt.xlabel(r'$\Delta x$')
        plt.title('grafico random walker per ' + str(passi[i]) + ' passi')
        plt.ylabel(r'$\Delta y$')
    plt.show()




for i in range(5):
    fig, ax = plt.subplots(1,2, figsize=(11,5))
    dx=rm.random_walk2d(8,1000)[0]
    dy=rm.random_walk2d(8,1000)[1]
    dst=np.empty(0)
    d=0
    for j in range(1, 1000):
        d=d+(dx[j]-dx[j-1])**2+(dy[j]-dy[j-1])**2
        dst=np.append(dst, d)
    ax[0].plot(dx, dy, color=color[i])
    ax[0].set_xlabel(r'$\Delta x$')
    ax[0].set_ylabel(r'$\Delta y$')
    ax[0].set_title('grafico per 5 random walker e 1000 passi')
    ax[1].plot(dst, color=color[i])
    ax[1].set_xlabel('passi')
    ax[1].set_ylabel('$distanza^2$')
    ax[1].set_title('grafico distanza percorsa')
plt.show()