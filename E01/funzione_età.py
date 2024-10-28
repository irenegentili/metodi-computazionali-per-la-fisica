from  datetime import datetime, timedelta

def funzione():
    mydate_str=input("inserire il compleanno")
    now=datetime.now()
    ris=None
    mydate = datetime.strptime(mydate_str, "%d-%m-%Y")
    dec=input("come si vuole l'età?(anni, secoli, giorni, secondi)")
    timediff=now-mydate
    if dec=="anni":
        ris=now.year-mydate.year
    elif dec=="secoli":
        ris=int(timediff.days/36525)
    elif dec=="secondi":
        ris=int(timediff.total_seconds())
    else:
        ris=timediff.days
    return ris, dec

a,b=funzione()
print("L'età è", '{:} {:}'.format(a,b))
        
        
        
        
    
    
