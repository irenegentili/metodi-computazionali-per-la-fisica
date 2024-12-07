import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import pandas as pd

def V(t):
    if np.isscalar(t):
        if int(t) %2 !=0:
            return -1
        else:
            return 1
    else:
        Vi = np.ones(len(t)) 
        odd_mask = t.astype(int) %2 != 0
        Vi[odd_mask] = -1
        return Vi

def fpb(Vo, t, RC):
    Vi=V(t)
    return (Vi-Vo)/(RC)
    

time=np.linspace(0,10,100)
x0=0
R=[4,1,0.25]
Vin=V(time)

Vout=[integrate.odeint(fpb, y0=x0, t=time, args=(i,)) for i in R]

for i in range(len(Vout)):
    plt.plot(time, Vout[i], color='green', label='Vout')
    plt.plot(time, Vin, color='blue', label='Vin')
    plt.legend()
    plt.xlabel('time')
    plt.show()

print(Vout[0])

Vout_flattened = [vout.flatten() for vout in Vout] 

print(time)
pb=pd.DataFrame({'t':time, 'Vin':Vin, 'Vout RC1': Vout_flattened[0], 'Vout RC2': Vout_flattened[1], 'Vout RC3':Vout_flattened[2]})
pb.to_csv('passabasso.csv', index=False)