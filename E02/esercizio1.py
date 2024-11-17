import pandas as pd
import  matplotlib.pyplot as plt
import numpy

pianeti = pd.read_csv('kplr010666592-2011240104155_slc.csv',delimiter=',', usecols=['TIME', 'SAP_FLUX', 'SAP_FLUX_ERR'])

print(pianeti)

print('Le colonne sono:', pianeti.columns)

plt.plot(pianeti['TIME'], pianeti['SAP_FLUX'], color="magenta")
plt.xlabel('time', fontsize=14)
plt.ylabel('flux', fontsize=14)
plt.title('Flusso in funzione del tempo')
plt.show()

plt.plot(pianeti['TIME'], pianeti['SAP_FLUX'],'o', color="magenta")
plt.xlabel('time', fontsize=14)
plt.ylabel('flux', fontsize=14)
plt.title('Flusso in funzione del tempo')
plt.show()

plt.errorbar(pianeti['TIME'], pianeti['SAP_FLUX'], yerr=pianeti['SAP_FLUX_ERR'], fmt='o',color="pink")
plt.xlabel('time', fontsize=14)
plt.ylabel('flux', fontsize=14)
plt.title('Flusso in funzione del tempo con bande di errore')
plt.savefig('/home/irene_gentili/MCF/E02/flussoerrori.pdf')
plt.show()

pianetimin=pianeti.loc[( pianeti['TIME'] > 938) & ( pianeti['TIME'] < 940)]

plt.errorbar(pianetimin['TIME'], pianetimin['SAP_FLUX'], yerr=pianetimin['SAP_FLUX_ERR'],color="pink")
plt.xlabel('time', fontsize=14)
plt.ylabel('flux', fontsize=14)
plt.title('Flusso in funzione del tempo nel minimo')
plt.savefig('/home/irene_gentili/MCF/E02/flussomin.pdf')
plt.show()

fig, ax = plt.subplots(figsize=(12,6))
plt.errorbar(pianeti['TIME'], pianeti['SAP_FLUX'], yerr=pianeti['SAP_FLUX_ERR'], fmt='.', color='cornflowerblue' )
plt.xlabel('time', fontsize=14)
plt.ylabel('flux', fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

ins_ax = ax.inset_axes([.65, .62, .32, .32]) 
ins_ax.errorbar(pianetimin['TIME'], pianetimin['SAP_FLUX'], yerr=pianetimin['SAP_FLUX_ERR'], fmt='o',  color='magenta')
plt.savefig('/home/irene_gentili/MCF/E02/flussoconmin.pdf')
plt.show()
