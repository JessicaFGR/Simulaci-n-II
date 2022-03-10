import random 
import matplotlib.pyplot as plt 
import numpy as np
a=0
n=150
y = np.linspace(-1, 15, 1000)
for i in range(14):
  x = np.sqrt((y/y))+i
  plt.plot(x, y, color = 'red', markersize = 1)
  i=i+1
for j in range(n):
  x0 = random.uniform(0.5, 14)
  y0 = random.uniform(0.5, 14)
  h=random.randint(0, 1 )
  p=random.random()
  if h==0:
    x1=x0+p  
  else:
    x1=x0-p
  y1 =((((x1-x0)**2)+1)**(1/2))+y0
  xa = np.linspace(x0,x1,100)
  ya = np.sqrt((((y1-y0)/(x1-x0))*(xa-x0))**2)+y0
  plt.plot(xa, ya, color = 'blue', markersize = 1) 
  plt.scatter(x1, y1, s = 20, c = 'blue') 
  if x1 > x0:
    x2 =int(x0)
    x3=x2+1
    x4=x0
    x5=x1
  else:
    x2 =int(x1)
    x3=x2+1
    x4=x1
    x5=x0
  if (x4>x2 and x5<x3):
    a = a+1 
fig = plt.figure(1, figsize = (10, 10)) 
plt.title("Estimación de pi ")
plt.grid()
plt.show()
pi = 2*(n/a) 
print ("pi : ",pi)
print ("")
