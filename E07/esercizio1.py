import pandas as pd
import numpy as np
from  scipy import optimize
import math
import matplotlib.pyplot as plt


decad=pd.read_csv('https://opendata.cern.ch/record/5203/files/Jpsimumu.csv', delimiter=',')

minv=np.empty(0)

for i in range(len(decad['Event'])):
    m=np.sqrt((decad['E1'][i]+decad['E2'][i])**2 - ((decad['px1'][i]+decad['px2'][i])**2 + (decad['py1'][i]+decad['py2'][i])**2 +(decad['pz1'][i]+decad['pz2'][i])**2))
    minv=np.append(minv, m)

for i in range(len(decad['Event'])):
    print('la massa invariante relativa all evento {:d} è {:f}'.format(decad['Event'][i], minv[i]))

n, bin1, p1 = plt.hist(minv, bins=400, color='magenta', alpha=0.7 )
plt.title('istogramma massa invariante')
plt.show()

n1, bin, p = plt.hist(minv, bins=200, range=(2.92, 3.227),color='magenta', alpha=0.7 )
plt.title('istogramma massa invariante nel picco')
plt.show()

def fg1(x, A, p1, po, m, sigma):
    return A*np.exp(-(x-m)**2/(2*sigma**2))+p1*x+po

cent=(bin[1:]+bin[:-1])/2 #il primo elemento di bin è solo l'inizio di un intervallo, l'ultimo è solo la fine, ma gli altri possono essere interpretabili come inizio o fine
#quindi faccio la media tra i primi 200 che sono inizi di intervalli e gli ultimi 200 che posso vedere tutti come fine
pstart=np.array([1,1,1,1,1])
params, params_cov = optimize.curve_fit(fg1, cent, n1, sigma=np.sqrt(n1), absolute_sigma=True, p0=[pstart])

print('params', params)
print('params_cov', params_cov)
print('errori params', np.sqrt(params_cov.diagonal()))

#xtest=np.linspace(2.92, 3.227, 100)

ytest=fg1(cent, params[0],params[1],params[2],params[3], params[4])

chi2 =  np.sum( (ytest - n1)**2/n1)

ndof=len(cent)-len(params) 

fig, ax = plt.subplots(3,1, figsize=(9,6), gridspec_kw={'height_ratios': [3, 1, 1]}, sharex=True) 
fig.subplots_adjust(hspace=0)
ax[0].plot(cent, ytest, color='black', label='fit dati')
ax[0].hist(minv, bins=200, range=(2.92, 3.227),color='magenta', alpha=0.7, label='istogramma massa invariante nel picco' )
ax[0].set_title('massa invariante nel picco')
ax[0].tick_params(axis="y", labelsize=14) 
ax[0].legend()

ax[1].errorbar(cent, n1-ytest, yerr=np.sqrt(n1), fmt='o', color='royalblue' )
ax[1].set_xlabel('bin', fontsize =14)
ax[1].axhline(1, color='darkorange') 
ax[1].set_ylabel('Dati/Fit',  fontsize =14)
ax[1].tick_params(axis="x",   labelsize=10) 
ax[1].tick_params(axis="y",   labelsize=10) 
ax[1].set_yticks(np.linspace(0.1, 3, 6))
ax[1].set_ylim(0.1,2.6)     

ax[2].errorbar(cent, (ytest-n1)/np.sqrt(n1), fmt='o', color='royalblue')
ax[2].set_xlabel('bin', fontsize =14)
ax[2].axhline(1, color='darkorange') 
ax[2].set_ylabel('Dati/Fit',  fontsize =14)
ax[2].tick_params(axis="x",   labelsize=10) 
ax[2].tick_params(axis="y",   labelsize=10) 
ax[2].set_yticks(np.linspace(-4, 4, 8))
ax[2].set_ylim(-4,4)  
plt.show()

print('Chi2 / ndf: {:4.2f} / {:d} = {:2.3f}'.format( chi2, ndof, chi2/ndof ) )


def fg2(x, A1,A2, p1, po, m, sigma1, sigma2 ):
    return A1*np.exp(-(x-m)**2/(2*sigma1**2))+ A2*np.exp(-(x-m)**2/(2*sigma2**2))+p1*x+po


pstart2=np.array([1,1,1,1,1,1,1])
params2, params_cov2 = optimize.curve_fit(fg2, cent, n1, sigma=np.sqrt(n1), absolute_sigma=True, p0=[pstart2])

print('params', params2)
print('params_cov', params_cov2)
print('errori params', np.sqrt(params_cov2.diagonal()))


ytest2=fg2(cent, params2[0],params2[1],params2[2],params2[3], params2[4], params2[5], params2[6])

chi22 =  np.sum( (ytest2 - n1)**2/n1)

ndof2=len(cent)-len(params2) 

fig, ax2 = plt.subplots(3,1, figsize=(9,6), gridspec_kw={'height_ratios': [3, 1, 1]}, sharex=True) 
fig.subplots_adjust(hspace=0)
ax2[0].plot(cent, ytest2, color='black', label='fit dati')
ax2[0].hist(minv, bins=200, range=(2.92, 3.227),color='magenta', alpha=0.7, label='istogramma massa invariante nel picco' )
ax2[0].set_title('massa invariante nel picco')
ax2[0].tick_params(axis="y", labelsize=14) 
ax2[0].legend()

ax2[1].errorbar(cent, n1-ytest2, yerr=np.sqrt(n1), fmt='o', color='royalblue' )
ax2[1].set_xlabel('bin', fontsize =14)
ax2[1].axhline(1, color='darkorange') 
ax2[1].set_ylabel('Dati/Fit',  fontsize =14)
ax2[1].tick_params(axis="x",   labelsize=10) 
ax2[1].tick_params(axis="y",   labelsize=10) 
ax2[1].set_yticks(np.linspace(0.1, 3, 6))
ax2[1].set_ylim(0.1,2.6)     

ax2[2].errorbar(cent, (ytest2-n1)/np.sqrt(n1), fmt='o', color='royalblue')
ax2[2].set_xlabel('bin', fontsize =14)
ax2[2].axhline(1, color='darkorange') 
ax2[2].set_ylabel('Dati/Fit',  fontsize =14)
ax2[2].tick_params(axis="x",   labelsize=10) 
ax2[2].tick_params(axis="y",   labelsize=10) 
ax2[2].set_yticks(np.linspace(-4, 4, 8))
ax2[2].set_ylim(-4,4)  
plt.show()

print('Chi2 / ndf: {:4.2f} / {:d} = {:2.3f}'.format( chi22, ndof2, chi22/ndof2 ) )

#siccome gliscarti nella parte dove domina la gaussiana hanno una certa direzione allora il problema è la distribzuione. nella zona più lontano dal pico domani la polinomiale e qui gli scarti non hanno un andamento definito. 
#quindi dove domina la gaussiana devo associare un errore sistematico perchè ho una sistematica differenza tra i dati.