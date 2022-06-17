#Ejercicio 12
import random
import numpy as np

def JS(n):
    t = 0
    lamb = 1
    JS = []
    for i in range(n):
        u = random.random()
        lamb_t = random.expovariate(lamb)
        if u <= lamb_t/lamb:
            t = t - (1/lamb)*np.log(u)
            JS.append(t)
    return JS

print("Js = ", JS(4))
