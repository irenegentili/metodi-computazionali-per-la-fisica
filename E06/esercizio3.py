import pandas as pd
import numpy as np
from  scipy import integrate
import math
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import argparse

os=pd.read_csv('oscilloscope.csv', delimiter=',')

fig,ax = plt.subplots(1,2, figsize=(12,6) )
ax[0].plot(os['time'],os['signal1'], color='red')
ax[1].plot(os['time'], os['signal2'],  color='royalblue'  )

ax[0].set_title('segnale 1', fontsize=15, color='red')
ax[1].set_title('segnale 2', fontsize=15, color='royalblue')

ax[0].set_xlabel('t')
ax[0].set_ylabel('s1')

ax[1].set_xlabel('t')
ax[1].set_ylabel('s2')
plt.show()

sign1=np.array(os['signal1'])
sign2=np.array(os['signal2'])
tt=np.array(os['time'])
print (sign1)

def my_derivative_vh(xx, yy, nh):
    dd = yy[nh:] - yy[:-nh]
    hh = xx[nh:] - xx[:-nh]
    for ih in range(int(nh/2)):
        dd = np.append(yy[nh-ih-1]-yy[0], dd)
        dd = np.append(dd, yy[-1]-yy[-(nh-ih)])
    
        hh = np.append(xx[nh-ih-1]-xx[0], hh)
        hh = np.append(hh, xx[-1]-xx[-(nh-ih)])
    
    return dd/hh


d1=my_derivative_vh(tt, sign1, 30000)
plt.plot(tt, d1,label='der signal 1', color='magenta')
plt.show()
plt.plot(tt, my_derivative_vh(tt, sign2,   30000),label='der signal 2', color='magenta')
plt.show()

maskm=np.abs(d1) < 0.015
val_min=d1[maskm]
pos_min=tt[maskm]

print('le posizioni e i valori dei minimi sono:', pos_min , val_min)

maskcoinc= (sign1 ==sign2)

print ('le coincidenze dei due segnali sono', tt[maskcoinc], sign1[maskcoinc])

