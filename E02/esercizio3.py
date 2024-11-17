import pandas as pd
import  matplotlib.pyplot as plt
import numpy as np

pianeti = pd.read_csv('kplr010666592-2011240104155_slc.csv',delimiter=',', usecols=['TIME', 'SAP_FLUX', 'SAP_FLUX_ERR'])

plt.plot(pianeti['TIME'], pianeti['SAP_FLUX'], color="magenta")
plt.xlabel('time', fontsize=14)
plt.ylabel('flux', fontsize=14)
plt.title('Flusso in funzione del tempo')
plt.show()

tpmin=939.29
tsmin=941.45

T=tsmin-tpmin


folded_time = (((pianeti['TIME'].values - tpmin+T/2)*1e6).astype(int)%int(T*1e6) )/1e6 -T/2


pianeti['FOLDED_TIME'] = folded_time


fig, ax = plt.subplots(figsize=(12,6))
plt.errorbar(pianeti['FOLDED_TIME'], pianeti['SAP_FLUX'], yerr=pianeti['SAP_FLUX_ERR'], fmt='.', color='cornflowerblue' )
plt.xlabel('Time', fontsize=14)
plt.ylabel('Flux',      fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.show()