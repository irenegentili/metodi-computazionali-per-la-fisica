import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import fft, optimize

cop=pd.read_csv('copernicus_PG_selected.csv', delimiter=',')

plt.plot(cop['date'], cop['mean_co_ug/m3'], color='red', label='concentrazione CO')
plt.plot(cop['date'], cop['mean_nh3_ug/m3'], color='green', label='concentrazione NH_3')
plt.plot(cop['date'], cop['mean_no2_ug/m3'], color='royalblue', label='concentrazione NO_2')
plt.plot(cop['date'], cop['mean_o3_ug/m3'], color='yellow', label='concentrazione O_3')
plt.plot(cop['date'], cop['mean_pm10_ug/m3'], color='magenta', label='concentrazione PM_10')
plt.plot(cop['date'], cop['mean_pm2p5_ug/m3'], color='orange', label='concentrazione PM_2P_5')
plt.plot(cop['date'], cop['mean_so2_ug/m3'], color='purple', label='concentrazione SO_2')
plt.xlabel('time')
plt.ylabel('concentrazione (ug/m3)')
plt.legend()
plt.show()

tf=fft.fft(np.asarray(cop['mean_co_ug/m3']))
fr=fft.fftfreq(len(tf), d=1)

plt.plot(fr[1:len(tf)//2], np.absolute(tf[1:len(tf)//2])**2,'o', color='purple')
plt.xlabel('frequenza')
plt.ylabel('spettro di potenza')
plt.xscale('log')
plt.yscale('log')
plt.show()
#se ho un picco vuol dire che quella frequenza è dominante rispetto alle altre che contribuiscono al rumore
#in questo caso ho quel dato che picca che indica il periodo. se ho una sinusoide quando faccio lo spettro ho tutto zero (ho solo i dati che danno rumore) ed un valore che picca che indica il periodo
#quando ho rumore ho solo un andamento lineare o che va come 1/f come detto all'inzio di E09
plt.plot(cop['date'], cop['mean_co_ug/m3'], color='red', label='concentrazione CO')
plt.show()

plt.plot(1/fr[1:len(tf)//2], np.absolute(tf[1:len(tf)//2])**2, color='purple')
plt.xlabel('tempo')
plt.ylabel('spettro di potenza')
plt.xscale('log')
plt.yscale('log')
plt.show()

fftmask = np.absolute(tf)**2< 4e6
filtered_tf = tf.copy() 
filtered_tf[fftmask] = 0

filtered_itf = fft.irfft(filtered_tf, n=len(cop['mean_co_ug/m3']))

plt.plot(cop['date'], cop['mean_co_ug/m3'], color='gold', label='Dati Originali')
plt.plot(cop['date'], filtered_itf,  color='limegreen', label='dati con filtro')
plt.legend(fontsize=13)
plt.show()

