import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import fft, optimize

def funz(f,k, beta):
    return k/f**beta

ds1=pd.read_csv('data_sample1.csv', delimiter=',')
ds2=pd.read_csv('data_sample2.csv', delimiter=',')
ds3=pd.read_csv('data_sample3.csv', delimiter=',')

plt.plot(ds1['time'], ds1['meas'], color='pink')
plt.xlabel('time')
plt.ylabel('ampiezza segnale')
plt.show()

plt.plot(ds2['time'], ds2['meas'], color='royalblue')
plt.xlabel('time')
plt.ylabel('ampiezza segnale')
plt.show()

plt.plot(ds3['time'], ds3['meas'], color='red')
plt.xlabel('time')
plt.ylabel('ampiezza segnale')
plt.show()

ts1=fft.rfft(np.asarray(ds1['meas']))
ts2=fft.rfft(np.asarray(ds2['meas']))
ts3=fft.rfft(np.asarray(ds3['meas']))




plt.plot(np.absolute(ts1[:len(ts1)//2])**2, 'o', color='purple') 
#prendo solo metà perchè sono speculari i coefficienti (soprattutto se reali e sono complessi sono compl coniugati quindi il modulo è lo stesso)
plt.xscale('log')
plt.yscale('log')
plt.show()
plt.plot(np.absolute(ts2[:len(ts2)//2])**2, 'o', color='purple')
plt.xscale('log')
plt.yscale('log')
plt.show()
plt.plot(np.absolute(ts3[:len(ts3)//2])**2,'o', color='purple')
plt.xscale('log')
plt.yscale('log')
plt.show()


d1t=np.asarray(ds1['time'])
f1= fft.fftfreq(len(ts1), d=d1t[1]-d1t[0])
params1, params_covariance1=optimize.curve_fit(funz, f1[1:len(ts1)//2], np.absolute(ts1[1:int(ts1.size)//2])**2, p0=[1,0] )
y1test=funz(f1[1:len(ts1)//2], params1[0], params1[1])
print('fit 1 - k=', params1[0], 'beta=', params1[1])

d2t=np.asarray(ds2['time'])
f2= fft.fftfreq(len(ts2), d=d2t[1]-d2t[0])
params2, params_covariance2=optimize.curve_fit(funz, f2[1:len(ts2)//2], np.absolute(ts2[1:int(ts2.size)//2])**2, p0=[1,0] )
y2test=funz(f2[1:len(ts2)//2], params2[0], params2[1])
print('fit 2 - k=', params2[0], 'beta=', params2[1])

d3t=np.asarray(ds3['time'])
f3= fft.fftfreq(len(ts3), d=d3t[1]-d3t[0])
params3, params_covariance3=optimize.curve_fit(funz, f3[10:len(ts3)//2], np.absolute(ts3[10:int(ts3.size)//2])**2, p0=[1,0.7])
y3test=funz(f3[10:len(ts3)//2], params3[0], params3[1])
print('fit 3 - k=', params3[0], 'beta=', params3[1])

plt.plot(f1[1:int(ts1.size)//2], np.absolute(ts1[1:int(ts1.size)//2])**2, 'o', markersize=4)
plt.plot(f1[1:len(ts1)//2], y1test, color='red')
plt.xlabel('Frequenza')
plt.ylabel(r'$|c_k|^2$')
plt.xscale('log')
plt.yscale('log')
plt.show()

plt.plot(f2[1:int(ts1.size)//2], np.absolute(ts2[1:int(ts2.size)//2])**2, 'o', markersize=4)
plt.plot(f2[1:len(ts2)//2], y2test, color='red')
plt.xlabel('Frequenza')
plt.ylabel(r'$|c_k|^2$')
plt.xscale('log')
plt.yscale('log')
plt.show()

plt.plot(f3[10:int(ts3.size)//2], np.absolute(ts3[10:int(ts3.size)//2])**2, 'o', markersize=4)
plt.plot(f3[10:len(ts3)//2], y3test, color='red')
plt.xlabel('Frequenza')
plt.ylabel(r'$|c_k|^2$')
plt.xscale('log')
plt.yscale('log')
plt.show()



