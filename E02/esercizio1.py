import pandas as pd
import  matplotlib.pyplot as plt
import numpy

pianeti = pd.read_csv('kplr010666592-2011240104155_slc.csv',delimiter=',', usecols=['TIME', 'SAP_FLUX', 'SAP_FLUX_ERR'])

print(pianeti)
print(pianeti.columns)

plt.plot(pianeti['TIME'], pianeti['SAP_FLUX'], color="magenta")
plt.xlabel('time')
plt.ylabel('flux')
plt.show()

plt.plot(pianeti['TIME'], pianeti['SAP_FLUX'],'o', color="magenta")
plt.xlabel('time')
plt.ylabel('flux')
plt.show()

plt.errorbar(pianeti['TIME'], pianeti['SAP_FLUX'], yerr=pianeti['SAP_FLUX_ERR'], fmt='o',color="pink")
plt.title('con errori')
plt.xlabel('time')
plt.ylabel('flux')
plt.savefig('/home/irene_gentili/MCF/E02/flussoerrori.pdf')
plt.show()

pianetimin=pianeti.loc[( pianeti['TIME'] > 938) & ( pianeti['TIME'] < 940)]

plt.errorbar(pianetimin['TIME'], pianetimin['SAP_FLUX'], yerr=pianetimin['SAP_FLUX_ERR'],color="pink")
plt.title('con errori')
plt.xlabel('time')
plt.ylabel('flux')
plt.show()

fig, ax = plt.subplots(figsize=(12,6))
plt.errorbar(kplrdf['TIME'], kplrdf['PDCSAP_FLUX'], yerr=kplrdf['PDCSAP_FLUX_ERR'], fmt='.', color='cornflowerblue' )
plt.xlabel('Time (BJD - 2454833)', fontsize=14)
plt.ylabel(r'Flux ($e^-/s$)',      fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylim(1.012e6, 1.030e6)

# creo inset 
ins_ax = ax.inset_axes([.65, .62, .32, .32])  # [x, y, width, height] w.r.t. ax
ins_ax.errorbar(      kplrdf.loc[ (kplrdf['TIME']> 947.9) & (kplrdf['TIME']< 948.35), 'TIME'],
                      kplrdf.loc[ (kplrdf['TIME']> 947.9) & (kplrdf['TIME']< 948.35), 'PDCSAP_FLUX'],
                 yerr=kplrdf.loc[ (kplrdf['TIME']> 947.9) & (kplrdf['TIME']< 948.35), 'PDCSAP_FLUX_ERR'], fmt='.',  color='royalblue')

plt.show()
