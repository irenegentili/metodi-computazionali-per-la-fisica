giorni=["lunedì","martedì","mercoledì","giovedì","venerdì","sabato", "domenica"]
for s in giorni:
    print('{:<10}'.format(s))

october24=giorni[-6:]+giorni*3+giorni[:4]
print("i giorni di ottobre sono:")
for s in october24:
    print('{:<10}'.format(s))

october_days = {}
for i in range(len(october24)):
    october_days.update({ i+1 : october24[i] })
print('ottobre è:')
for k in october_days:
    print( '{:<d} {:<10}'.format(k, october_days[k]))
