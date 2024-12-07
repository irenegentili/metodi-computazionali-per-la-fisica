import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import matplotlib.animation as animation

def pendolo(r, t, g, l):
    dtedt=r[1]
    dodt=-(g/l)*np.sin(r[0])
    drdt=[dtedt, dodt]
    return drdt


ini =np.array([[np.radians(45),np.radians(45),np.radians(30)],[0,0,0]])
time= np.linspace(0,10,1000)
g=9.81
l=[0.5,1,0.5]

rsol=[integrate.odeint(pendolo, [ini[0][i], ini[1][i]], time, args=(g,l[i])) for i in range(len(l))]

for i in range(len(l)):
    plt.plot(time, np.degrees(rsol[i][:,0]), color='pink')
    plt.xlabel('time')
    plt.ylabel('theta')
    plt.show()


plt.plot(time, rsol[0][:,0], color='pink', label='l=0.5')
plt.plot(time, rsol[1][:,0], color='blue', label='l=1')
plt.plot(time, rsol[2][:,0], color='red', label='l=0.5')
plt.show()


def animate_pendulum(i, x, y, dt, line, mass, text):
    """
    Funzione pe animazione pendolo

    Assegna la posizione  istante per istante  agli ogetti da animare
    Il fulcro del pendolo è posizionato alle coordinate (0,0)

    Parametri
    ----------

    i    : indice del frame da rappresenare (obbligatorio con FuncAnimatuin)
    x    : array con coordinate x della massa del pendolo in funzione del tempo
    y    : array con coordinate y della massa del pendolo in funzione del tempo
    dt   : distanza temporale fra i punti dell'array dei tempi con cui si è risolta l'equazione del moto
    line : oggetto grafico  che rappresenta il filo di sospensione (plt.plot([0,x[i]],[0,yi[i]]))
    mass : oggetto grafico  che rappresenta la massa del pendolo   (plt.plot(   x[i],    yi[i] ))
    text : testo con tempo che scorre

    Output
    -----------
    return line, mass, text
    """
    
    line_x = [0, x[i]]
    line_y = [0, y[i]]
    line.set_data(line_x,line_y)

    mass_x = x[i]
    mass_y = y[i]
    mass.set_data(mass_x,mass_y)

    time_template = 'time = %.1fs'
    text.set_text(time_template % (i*dt))

    return line, mass, text

#------------------- Animazione  ------------------------------------#

# proiezione su asse x e y della soluzione. 
x1 =  1*np.sin(rsol[0][:, 0])
y1 = -1*np.cos(rsol[0][:, 0])

dt=10/1000
    # Figura per animazione 
fig = plt.figure(figsize=(9,8))
ax  = fig.add_subplot(111, autoscale_on=False, xlim=(-1.5, 1.5), ylim=(-1.5, 1.5))
    #ax.grid()


    # Oggetti da animare (linea, massa, testo)
pendulum_line, = ax.plot([], [], 'o-', lw=2, markersize=5,  color='slategray')
pendulum_mass, = ax.plot([], [], 'o',        markersize=15, color='darkred'  )
time_text      = ax.text(0.05, 0.9, '', transform=ax.transAxes, fontsize=16)

    # Animazione 
pendulum_ani = animation.FuncAnimation(
    fig,                                                        # Figura per animazione
    animate_pendulum,                                           # Funzione per animazione con calcolo oggetti ad ogni istante
    np.arange(1, len(y1)),                                      # valori su cui iterare ( corripondnete all'indice i in animate)
    fargs=( x1,y1,dt, pendulum_line, pendulum_mass, time_text), # argomenti aggiuntivi della funzione animate 
    interval=25,                                                # Intervallo fra due frame successivi (ms)
    blit=True)                                                  # Ottimizzazione grafica
plt.show()




