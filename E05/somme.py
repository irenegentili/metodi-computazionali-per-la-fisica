import math 
import sys
def somma (n):
    s=0
    for i in range (0,n+1):
        s=i+s
    return s

def sommarad (n):
    s=0
    for i in range (0,n+1):
        s=s+math.sqrt(n)
    return s

def sp (n):
    s=0
    p=1
    for i in range (0,n+1):
        p=p*i
        s=s+i
    return s,p

def smpot(n, a=1):
    s=0
    for i in range (0,n+1):
        s=s+math.pow(i,a)
    return s

sys.path.append('../../MCF/E05')
sys.path