#Jessica Fernada González Rivas
import random
import numpy as np
print("Elegir al azar una ciudad de la Lista despues de hacer una mezcla.")
Lista=['Rome','New York','London','Berlin','Moskov', 'Los Angeles','Paris','Madrid','Tokio','Toronto']
for i in range(1):
    Ciudad=random.shuffle(Lista) #se hace una mezcla de la lista
    Ciudad=random.sample(Lista,1) #se selecciona un elemenot al azar de la lista
print("Mezcla",Lista) #Se imprime lamezclarealizada
print("La ciudad seleccionada luego de una mezcla es",random.sample(Lista,1))#se imprime la cd seleccionada al azar

print("Elegir al azar tres ciudades después de una mezcla.")

for i in range(3): 
    Ciudad=random.shuffle(Lista)#se mezclan de los elementos de la lista.
    Ciudad=random.sample(Lista,3) #se seleccionan 3 ciudades al azar sin repeticion de la lista.
print("Mezcla",Lista)#se imprimen las ciudades mezcladas.
print("las tres ciudades seleccionadas luego de una mezcla son",random.sample(Lista,3))
#se imprimen las tres ciudades seleccionadas al azar y sin repetición.
