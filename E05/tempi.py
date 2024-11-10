import pandas as pd
import  matplotlib.pyplot as plt
import numpy as np

modulo0 = pd.read_csv('hit_times_M0.csv',delimiter=',', usecols=['mod_id', 'det_id', 'hit_time'])

n, bis, p = plt.hist(modulo0['hit_time'], bins=50, range=( 287824, 999309580), color='pink', alpha=0.7 )
plt.xlabel('hit time (s) ', color= 'magenta', fontsize=16)
plt.title('istogramma tempi primo modulo')
plt.show()


n, bis, p = plt.hist(np.log10(np.diff(modulo0['hit_time'])), bins=200, range=( 0,10), color='pink', alpha=0.7 )
plt.xlabel('hit time (s) ', color= 'magenta', fontsize=16)
plt.title('istogramma $\Delta t$ primo modulo')
plt.show()
