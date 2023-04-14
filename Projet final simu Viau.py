#%matplotlib ipympl

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.animation as animation

#tiges et masses
l1=1
l2=1
m1=1
m2=1

#condition initiales
y0 = np.array([0, 0.7, 0, 0])

#gravité
g=9.81

def systeme(Y,t,l1,l2,m1,m2):
    o1, op1, o2, op2=Y
    
    do1=op1
    dop1=(m2*g*np.sin(o2)*np.cos(o1-o2)-m2*np.sin(o1-o2)*(l1*op1**2*np.cos(o1-o2)+l2*op2**2)-(m1+m2)*g*np.sin(o1))/l1/(m1+m2*np.sin(o1-o2)**2)
    
    do2=op2
    dop2=((m1+m2)*(l1*op1**2*np.sin(o1-o2)-g*np.sin(o2)+g*np.sin(o1)*np.cos(o1-o2))+m2*l2*op2**2*np.sin(o1-o2)*np.cos(o1-o2))/l2/(m1+m2*np.sin(o1-o2)**2)
    
    return do1, dop1, do2, dop2

#coordonnées cartésiennes des masses
#x1=l1*np.sin(o1)
#y1=-l1*np.cos(o1)
#x2=x1+l2*np.sin(o2)
#y2=y1-l2*np.cos(o2)

#temps max et intervalle
T=100
dt=1000

#résolution
t = np.linspace(0, T, dt)
y=odeint(systeme, y0, t, args=(l1, l2, m1, m2))
o1, o2 = y[:,0], y[:,2]

#graphique    
fig=plt.figure()
    
plt.plot(t,o1)
plt.plot(t,o2)
    
plt.legend(['masse 1','masse 2'])
           
plt.xlabel('temps (s)')
plt.ylabel('position angulaire')

plt.grid()
plt.title('Évolution du double pendule')

#plt.savefig('Pendule 3')

fig.set_size_inches(12.5, 8.5)
plt.show()

                                                                                 .