n=input("immettere il numero massimo da sommare: ")
nn=int(n)
somma=0
for i in range(0,nn+1):
    somma=somma+i
print(' la somma dei primi {:d} numeri naturali è: {:d}'.format(nn,somma))
