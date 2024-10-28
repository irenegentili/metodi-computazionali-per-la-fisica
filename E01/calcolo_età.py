from datetime import datetime, timedelta
mydate_str=input("inserire la data di nascita:")
mydate= datetime.strptime(mydate_str, "%d-%m-%Y %H:%M:%S")

datenow=datetime.now()

datediff=datenow - mydate
anni=datenow.year - mydate.year
if mydate.month>datenow.month or( mydate.month==datenow.month and mydate.day>datenow.day):
    anni=anni-1

gg=datediff.days
ss=int(datediff.total_seconds())

print("anni", anni)
print("giorni", gg)
print("secondi",ss)
