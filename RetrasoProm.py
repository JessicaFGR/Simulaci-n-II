from random import expovariate
from matplotlib.pyplot import *
from random import seed
from math import inf as Infinity
from statistics import mean
#Estimacion del promedio de respuesta
# Comenzamos definiendo los Parametros

lamda = 1.3             # Arribos 
mu = 2.0                # salidas

Num_Paquetes = 30       # Numero de paquetes a simular
#T = 100000
count = 0               # Contador de paquetes
t = 0
N = 0                    # Numero de paquetes en el sistema

tll = expovariate(lamda)            # Tiempo de llegada
ts = Infinity                       # Tiempo de salida

# Variables de salida
tll_Data = []                       # tiempos de llegada
ts_Data = []                        # tiempos de salida
r_Data = []                         # retrasos individuales

tiemp=[]
esp=[]

while count < Num_Paquetes:
#while t < T:
    if tll < ts:                    # llegada
        t = tll
        tll_Data.append(t)
        N = N + 1.0
        tll = t + expovariate(lamda)
        tiemp.append(t)
        esp.append(N)
        if N == 1:
            ts = t + expovariate(mu)
    else:                                         # salida
        t = ts 
        ts_Data.append(t)
        N = N - 1.0
        tiemp.append(t)
        esp.append(N)
        count = count + 1                         # Paquetes simulados
        if N > 0:
            ts = t + expovariate(mu)
        else:
            ts = Infinity
            
# Estimación del retraso promedio:

for i in range(Num_Paquetes):
#for i in range(T):
    d = ts_Data[i] - tll_Data[i]
    r_Data.append(d)

print( "Retraso promedio = ", round( mean(r_Data), 4) )

fig = figure(1, figsize=(16, 8))
step(tiemp, esp, Linewidth=1.5, color='green')
xlabel('Tiempo', size=16)
ylabel('N', size=16)
show()
