import sys
import numpy as np
import scipy 
import matplotlib.pyplot as plt
from matplotlib import  transforms
import randomwalk2 as rm

def cum(phi): 
    return 0.5*(1-np.cos(phi/2))
   
def invcum(y):
    return  2*np.arccos(1-2*y)

ycum=np.random.random(10000)
xcum=invcum(ycum)

plt.hist(xcum, bins=100, range=(0, 2*np.pi), color='pink')
plt.title(r'grafico valori di $\phi$')
plt.show()

color=['blue', 'magenta', 'red', 'green', 'black']
for i in range(5):
    plt.plot(rm.random_walkphi(8, 1000)[0], rm.random_walkphi(8, 1000)[1], color=color[i])
    plt.xlabel(r'$\Delta x$')
    plt.ylabel(r'$\Delta y$')
plt.show()


for i in range(5):
    x, y=rm.random_walkas(1,0.1)
    plt.plot(x, y, color=color[i])
    plt.xlabel(r'$\Delta x$')
    plt.ylabel(r'$\Delta y$')
plt.show()
