import random
import numpy as np
import matplotlib.pyplot as plt
mu=180
sig=15
n=1000
num=[]
for j in range(n):
  suma=0
  for i in range(15):
    a=random.random()
    suma=suma+a
  x=mu+sig*(suma-6)
  num.append(x)
plt.hist(num, bins = 200)
plt.title("Método de las doce uniformes")
plt.show()
num=[]
print("Gráfica de gauss")
for i in range(n):
    temp = random.gauss(mu, sig)
    num.append(temp)
plt.hist(num, bins = 200)
plt.title("Funcion gauss()")
plt.show()
