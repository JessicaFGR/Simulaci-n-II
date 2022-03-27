import random
import numpy as np

lamb = 0.1
t = 0 
nl = 0 
ns = 0 
n=0 
m = 0
pl = t - (1/lamb)*np.log(random.random())
ts = 1000000 
T = 100
for i in range(T):
    t = t + 1
    if pl <= ts and pl <= T:
        t = pl
        nl += 1
        n += 1
        pl = t - (1/lamb)*np.log(random.random())

print("Tiempo transcurrido = ", t)
print("Número de clientes en el sistema en t = ", n)
print("Primera llegada = ", pl)
