import pandas as pd
import numpy as np
from  scipy import integrate
import math
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import argparse

def parse_arguments():

    parser = argparse.ArgumentParser(description='Esempio utilizzo argarse.',
                                     usage      ='python3 esercizio2.py --opzione')
    parser.add_argument('--pot', action='store', help='passa il potenziale')
    return parser.parse_args()

args= parse_arguments()

def potenziale1 (x):
    return 0.1*x**4
def potenziale2 (x):
    return 0.1*x**(1/2)
def potenziale3 (x):
    return 0.1*np.abs(x)**(3/2)

if args.pot == 'pot1':
    
    periodo = np.empty(0)
    xinarr=np.arange(0.1, 5.1, 0.1)
    for xin in xinarr:
        xx=np.linspace(0, xin, 1000)
        integranda=1/(np.sqrt(potenziale1(xin)-potenziale1(xx[:-1])))
        periodo=np.append(periodo,integrate.simpson(integranda, xx[:-1], dx=xin/1000)*np.sqrt(16))
    

    

    plt.plot(xinarr, periodo, color='royalblue')
    plt.xlabel('punto di partenza')
    plt.ylabel('periodo')
    plt.show()

elif args.pot == 'pot2':
    periodo = np.empty(0)
    xinarr=np.arange(0.1, 5.1, 0.1)
    for xin in xinarr:
        xx=np.linspace(0, xin, 1000)
        integranda=1/(np.sqrt(potenziale2(xin)-potenziale2(xx[:-1])))
        periodo=np.append(periodo,integrate.simpson(integranda, xx[:-1], dx=xin/1000)*np.sqrt(16))
    

    

    plt.plot(xinarr, periodo, color='royalblue')
    plt.xlabel('punto di partenza')
    plt.ylabel('periodo')
    plt.show()
elif args.pot == 'pot3':
    periodo = np.empty(0)
    xinarr=np.arange(0.1, 5.1, 0.1)
    for xin in xinarr:
        xx=np.linspace(0, xin, 1000)
        integranda=1/(np.sqrt(potenziale3(xin)-potenziale3(xx[:-1])))
        periodo=np.append(periodo,integrate.simpson(integranda, xx[:-1], dx=xin/1000)*np.sqrt(16))
    plt.plot(xinarr, periodo, color='royalblue')
    plt.xlabel('punto di partenza')
    plt.ylabel('periodo')
    plt.show()

    



