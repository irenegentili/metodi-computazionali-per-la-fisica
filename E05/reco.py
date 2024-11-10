class Hit():
    def __init__(self, modulo, sensore, time):
         self.modulo    = modulo
         self.sensore   = sensore
         self.time      = time
         
         
    def __str__(self):
         return 'hit: numero del modulo: {:}, sensore: {:}, time stamp rivelazione : {:}'.format(self.modulo, self.sensore, self.time)

    def __lt__ (self, other):
        return self.time < other.time

    def __gt__ (self, other):
        return self.time > other.time 
    
    def __sub__(self, other):
        return self.time - other.time

    def __eq__ (self, other):
        return  self.sensore == other.sensore and self.modulo == other.modulo


class Event():

    def __init__(self, durata, n, timep, timeu, ahit):
        self.n= n
        self.timep=timep
        self.timeu=timeu
        self.durata=durata
        self.ahit=ahit
    

    
    


