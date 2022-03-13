from random import random
from math import sqrt
def numero(n):
    numero=((-1)**n)/((2*n)+1)
    return numero
pi=0
for i in range(100000):
    pi=pi+numero(i)
print(pi*4)
