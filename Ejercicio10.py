import random 
import matplotlib.pyplot as plt 
num = [] 
m = 10
s = 5 
for i in range(1000): 
  temp = random.betavariate(m,s) 
  num.append(temp) 
plt.hist(num, bins = 100, color= "green") 
plt.show() 

#Para el triangular
import random 
import matplotlib.pyplot as plt 
num = [] 
m = 10
s = 5 
for i in range(10000): 
  temp = random.triangular(m,s) 
  num.append(temp) 
plt.hist(num, bins = 100, color= "purple") 
plt.show() 

#pareto
import random 
import matplotlib.pyplot as plt 
num = [] 
m = 10
s = 5 
for i in range(10000): 
  temp = random.paretovariate(m,s) 
  num.append(temp) 
plt.hist(num, bins = 100, color= "blue") 
plt.show() 
