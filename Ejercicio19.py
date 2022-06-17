#Calcular el valor de la integral
#I=(1/(1+u1))+(1/(1+u2))+...+(1/(1+un))

import numpy as np
import matplotlib.pyplot as plt

#Definimos la función de prueba.
def funcion(x):
    return 1.0/(1+x)
#Graficamos la función de prueba.
X=np.linspace(0,1,1000)
plt.plot(X,funcion(X), color='green', label="$y=1/(1+x)$")
#plt.fill_between(X,funcion(X))
plt.legend()
plt.xlim(0.0, 1.2)
plt.ylim(0.0, 1.2)
plt.grid(True)
plt.title('Función de prueba', color='b')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

#Ahora por medio de la media muestral

def integral(func=funcion, n=3000):
    muestreo=[]
    suma=[]
    for i in range(n):
        u= np.random.random_sample()
        muestreo.append(u)
        y=funcion(u)
        suma.append(y)

    return np.mean(suma), np.std(suma)

print("El valor de la integral es:", round(integral()[0],5))
print("El error estándar es:", round(integral()[1],5))

def integral(func=funcion, n=3000):
    muestreo=[]
    suma=[]
    for i in range(n):
        u= np.random.random_sample()
        muestreo.append(u)
        y=funcion(1-u)
        suma.append(y)

    return np.mean(suma), np.std(suma), suma

print("El valor de la integral es:", round(integral()[0],5))
print("El error estándar es:", round(integral()[1],5))

def integral(func=funcion, n=3000):
    muestreo=[]
    suma=[]
    for i in range(n):
        u= np.random.random_sample()
        muestreo.append(u)
        y=(funcion(u) + funcion(1-u))/2.0
        suma.append(y)

    return np.mean(suma), np.std(suma)

print("El valor de la integral es:", round(integral()[0],5))
print("El error estándar es:", round(integral()[1],5))

def mc_crudo(funcion, n):
    Integral=[]
    suma=[]
    for i in range(n):
        u= np.random.random_sample()
        y=(funcion(u) + funcion(1-u))/2.0
        suma.append(y)
        Integral.append(np.mean(suma))
        
    print("El valor de la integral es:", round(np.mean(suma),5))
    print("El error estándar es:", round(np.std(suma),5))
    
    return np.mean(suma), np.std(suma), Integral

def mc_crudo1(funcion, n):
    Integral=[]
    suma=[]
    for i in range(n):
        u= np.random.random_sample()
        y=funcion(u)
        suma.append(y)
        Integral.append(np.mean(suma))
        
    print("El valor de la integral es:", round(np.mean(suma),5))
    print("El error estándar es:", round(np.std(suma),5))
    
    return np.mean(suma), np.std(suma), Integral

X1=mc_crudo1(funcion, n=1000)[2]
X=mc_crudo(funcion, n=1000)[2]

plt.plot(X, color='blue', label='antiteticas')
plt.plot(X1, color='green', label='u')
plt.legend()
