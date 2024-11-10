import reco as rc 
import pandas as pd
import  matplotlib.pyplot as plt
import numpy as np

modulo0 = pd.read_csv('hit_times_M0.csv',delimiter=',', usecols=['mod_id', 'det_id', 'hit_time'])
modulo1 = pd.read_csv('hit_times_M1.csv',delimiter=',', usecols=['mod_id', 'det_id', 'hit_time'])
modulo2 = pd.read_csv('hit_times_M2.csv',delimiter=',', usecols=['mod_id', 'det_id', 'hit_time'])
modulo3 = pd.read_csv('hit_times_M3.csv',delimiter=',', usecols=['mod_id', 'det_id', 'hit_time'])

dati=[modulo0,modulo1,modulo2,modulo3]

def rc_Hit(a,b,c):
    rh=np.array([rc.Hit(a,b,c)])
    return rh

rhtot=np.empty(0) #array vuoto


for i in dati:
    for ir, rr in i.iterrows(): #perchè i è un dictionary
        rhtot=np.append(rhtot, rc_Hit(rr['mod_id'], rr['det_id'], rr['hit_time']))


rhtotord = np.sort(rhtot)

#nel logaritmo va messo un float
n, bis, p = plt.hist(np.log10(np.diff(rhtotord).astype(float)), bins=50, range=(0,10), color='darkgreen', alpha=0.7 )
plt.xlabel('diff hit time (s) ', color= 'magenta', fontsize=12)
plt.title('istogramma $\Delta t$')
plt.show()

def rc_Event(t):
    
    ev=np.array([rc.Event(t, rhtotord[:n-1])])
    return ev

event=rc_Event(10)
print (event)














