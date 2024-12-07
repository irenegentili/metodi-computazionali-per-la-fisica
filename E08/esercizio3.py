import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import pandas as pd

def oscillatore(r,t,omega,):
    dxdt=r[1]
    dydt= -omega**2*r[0]**3
    return (dxdt,dydt)

time=np.linspace(0,10,1000)

rin=(1,0)
omega=2

sol=integrate.odeint(oscillatore, rin, time, args=(omega,))

fig,ax = plt.subplots(figsize=(9,6))
plt.plot(time, sol , label=('x', 'v')) 
plt.legend(fontsize=14)
plt.show()