import numpy as np 
import math
import random
import matplotlib.pyplot as plt 
x = np.linspace(0,1,100)
y = np.sqrt(np.arctan(x)) 
contador = 0 
n = 100
d = 0 
fig = plt.figure(1, figsize = (10, 10)) 
plt.plot(x, y, color = 'green', markersize = 1) 
for i in range(n):
  x1 = random.random()
  y1 = random.random()
  h = ((math.atan(x1)**(1/2))/y1)
  plt.scatter(x1, y1, s = 20, c = 'purple')  
  if h < 1:
    d = d+1 
  contador = contador+1 
tan = 4*(d/n)
print ("La Raíz del arctan de 0 a 1 es: ",tan)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
