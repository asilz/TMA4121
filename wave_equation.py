import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator

# Definere initialbetingelse
def f(x, y):
    #return (x*y)**2*0.0002 #Annen initialbetingelse som gir en enkel bølge
    return np.sin(np.pi*x*2) * np.sin(0.5*y*2)*0.01

# Sette opp grenser i tid og rom
r_lim = 1
theta_lim = 2*np.pi
t_lim = 0.1*10


M = (int)(50)  # Antall punkter i r-retning
N = (int)(50)  # Antall punkter i theta-retning
P = (int)(1500*0.4)  # Antall punkter i t-retning

h = r_lim/M
k = theta_lim/N
m = t_lim/P

r = np.linspace(0, r_lim, M+1)
theta = np.linspace(0, theta_lim, N+1)
t = np.linspace(0, t_lim, P+1)

u = np.zeros((M+1, N+1, P+1))
r, theta, t = np.meshgrid(r, theta, t)

#u[(int)(M/2), (int)(N/2), 0] = -0.5

u[:, :, 0] = f(r[:, :, 0], theta[:, :, 0])

# Eksplisitt løsningsmetode for polar bølgelikning i r og theta dimensjoner
for p in range(P):
    for i in range(1, M):
        for j in range(1, N):
            #u[i, j, p+1] = m*m*( ((u[i+1,j,p]-2*u[i,j,p]+u[i-1,j,p])/(h*h)) + ((u[i+1,j,p]-u[i,j,p])/(r[i,j,p]*h)) + ((u[i,j+1,p]-2*u[i,j,p]+u[i,j-1,p])/((r[i,j,p]**2)*k*k)) ) + 2*u[i,j,k]-u[i,j,k-1]2*u[i,j,k]
            u[i, j, p+1] = m*m*((u[i+1,j,p]-2*u[i,j,p]+u[i-1,j,p])/(h*h))
            u[i, j, p+1] += m*m*((u[i+1,j,p]-u[i,j,p])/(r[i,j,p]*h))
            u[i, j, p+1] += m*m*((u[i,j+1,p]-2*u[i,j,p]+u[i,j-1,p])/((r[i,j,p]**2)*k*k))
            u[i, j, p+1] += 2*u[i,j,p]
            u[i, j, p+1] -= u[i,j,p-1]

# Plotting av løsningen over tid
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for p in range(0,P,5):
    ax.clear()
    surf = ax.plot_surface(r[:, :, 0], theta[:, :, 0], u[:, :, p].T, cmap=cm.coolwarm, vmin=-1, vmax=1 , linewidth=0, antialiased=False)

    ax.set_xlabel('R-akse')
    ax.set_ylabel('Theta-akse')
    ax.set_zlabel('Height')
    ax.set_zlim(0, 2)
    ax.zaxis.set_major_locator(LinearLocator(10))

    plt.pause(0.001)  # Legge til en pause for å vise plottet før det oppdateres

plt.show()

#Tror ikke løsningen er helt riktig, men det ser ut som en bølge så jeg tror jeg er inne på noe i hvertfall
