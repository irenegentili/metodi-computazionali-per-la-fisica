import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pianeti = pd.read_csv('ExoplanetsPars_2024.csv',delimiter=',',comment='#', usecols=['pl_orbper', 'pl_bmassj', 'pl_orbsmax','st_mass','discoverymethod' ])
print(pianeti)
print(pianeti.columns)

print(pianeti.iloc[5:8])

plt.scatter(pianeti['pl_orbper'] , pianeti['pl_bmassj'], color='royalblue', s=32)
plt.xlabel('periodo', fontsize=16)
plt.ylabel('massa', fontsize=16)
plt.xscale('log')
plt.yscale('log')
plt.show()

RqM=pianeti['pl_orbsmax']**2/pianeti['st_mass']

plt.scatter(pianeti['pl_orbper'] , RqM, color='tomato')
plt.xlabel('periodo', fontsize=16)
plt.ylabel('Rmax/m*', fontsize=16)
plt.xscale('log')
plt.yscale('log')
plt.show()

transit=pianeti.loc[( pianeti['discoverymethod'] =='Transit')]
rad_vel=pianeti.loc[( pianeti['discoverymethod'] == 'Radial Velocity')]

plt.scatter(transit['pl_orbper'] , transit['pl_bmassj'], color='royalblue', s=68, label='transit', alpha=0.5)
plt.scatter(rad_vel['pl_orbper'] , rad_vel['pl_bmassj'], color='tomato',   s=68, label='radial velocity', alpha=0.5)
plt.xlabel('periodo', fontsize=16)
plt.ylabel('massa', fontsize=16)
plt.legend(fontsize=14)
plt.xscale('log')
plt.yscale('log')
plt.show()

trm=np.log10(transit['pl_bmassj'])
rvm=np.log10(rad_vel['pl_bmassj'])
n, bis, p = plt.hist(rvm, bins=200, range=(-4, 4), color='gold', label='radial velocity',alpha=0.5 )
n, bis, p = plt.hist(trm, bins=200, range=(-4, 4), color='green',label='transit',alpha=0.5 )
plt.ylabel('massa', fontsize=16)
plt.legend(fontsize=14)
plt.show()



fig = plt.figure(figsize=(12,11))


gr = fig.add_gridspec(2, 2, hspace=0, wspace=0)
ax = gr.subplots( sharex='col', sharey='row')

ax[1,0].scatter(np.log10(transit['pl_orbper']),  trm,  color='limegreen',  alpha=0.3, label='Transit')
ax[1,0].scatter( np.log10(rad_vel['pl_orbper']), rvm, color='darkorange', alpha=0.3, label='Radial Velocity')

ax[1,0].tick_params(axis='both', which='major', labelsize=14)
ax[1,0].set_xlabel('log(Period [days])',         fontsize=16)
ax[1,0].set_ylabel('log(Planet Mass)',  fontsize=16)
ax[1,0].legend(fontsize=16)


ax[0,0].hist( np.log10(transit['pl_orbper']),bins=50, range=(-2, 5), color='limegreen',  alpha=0.5, label='Transit')

ax[0,0].hist(np.log10(rad_vel['pl_orbper']), bins=50, range=(-2, 5), color='darkorange',  alpha=0.5, label='Radial Velocity')
ax[0,0].tick_params(axis='both', which='major', labelsize=14)
ax[0,0].set_ylabel('Numero pianeti',        fontsize=16)
ax[0,0].legend(fontsize=16)



ax[1,1].hist(trm,bins=50, range=(-4, 4), color='limegreen',  alpha=0.5, orientation='horizontal', label='Transit')

ax[1,1].hist(rvm, bins=50, range=(-4, 4), color='darkorange',  alpha=0.5, orientation='horizontal', label='Radial Velocity')
ax[1,1].tick_params(axis='both', which='major', labelsize=14)
ax[1,1].set_xlabel( 'Number of planets',        fontsize=16)
ax[1,1].legend(fontsize=16)

ax[0,1].axis('off')

plt.savefig('/home/irene_gentili/MCF/metodi-computazionali-per-la-fisica/E02/graficoriassuntivo.pdf')
plt.show()