import pandas as pd
import numpy as np
from  scipy import integrate
import math
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import argparse


def parse_arguments():

    parser = argparse.ArgumentParser(description='Esempio utilizzo argarse.',
                                     usage      ='python3 argparse_example.py  --opzione')
    parser.add_argument('--file', action='store', help='passa un file da leggere')
    parser.add_argument('--grafico', action='store', type=str, help='scegliere il grafico')
    return parser.parse_args()

args= parse_arguments()

if args.file !=None:
    
    distanza=pd.read_csv(args.file, delimiter=',', usecols=['t','v'])
    
    if args.grafico != None:
        if args.grafico == 'velocità':
            plt.plot(distanza['t'], distanza['v'], color='royalblue')
            plt.xlabel('tempo')
            plt.ylabel('velocità')
            plt.show()
        elif args.grafico == 'distanza':
            ds= [integrate.simpson(distanza['v'][:i+1], distanza['t'][:i+1]) for i in range(len(distanza['t']))]

            plt.plot (distanza['t'], ds , color='royalblue')
            plt.xlabel('tempo')
            plt.ylabel('distanza')
            plt.show()


