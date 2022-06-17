#Ejercicio 18.
#Hacer una función que devuelva el intervalo de confianza.
#Calcular los intervalos de confianza a 80, 90, 95, 98 y 99% con la muestra:


import statistics as stat
import math
muestra = [3.2, 3, 2.8, 2.9, 3.1]
n=len(muestra)             
mean=stat.mean(muestra) 
s=stat.stdev(muestra) 
t=2.776   

ic1 = mean - t*(s/math.sqrt(n))     
ic2 = mean + t*(s/math.sqrt(n))

print("Media:",mean)
print("Desviación estandar:",s)
print("Intervalo de confianza:", round(ic1, 2), round(ic2, 2))
S=((3.2-3.0)**2+(3.0-3.0)**2+(2.8-3.0)**2+(2.9-3.0)**2+(3.1-3.0)**2)/(len(muestra)-1) #Varianza muestral 
print(math.sqrt(S))
def desvest(muestra,t):
  n=len(muestra)             # numero de datos
  mean=stat.mean(muestra)    # media muestral
  s=stat.stdev(muestra)      # desviacion estandar muestral

  # empleamos las siguientes formulas
  ic1 = mean - t*(s/math.sqrt(n))     
  ic2 = mean + t*(s/math.sqrt(n))
  intervalo=[round(ic1, 2), round(ic2, 2)]
  return(intervalo)
muestra=[3.33,3.15,2.91,3.05,2.75]

#Intervalo de confianza 80%
desvest(muestra,0.9195)
#Intervalo de confianza 90%
desvest(muestra,1.4759)
#Intervalo de confianza 95%
desvest(muestra,2.0150)
#Intervalo de confianza 98%
desvest(muestra,3.3649)
#Intervalo de confianza 99%
desvest(muestra,4.0321)
