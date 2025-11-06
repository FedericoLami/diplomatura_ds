import numpy as np


matriz=np.linspace(0,9,10)     #primer data desde donde, segundo data hasta donde, tercer dato cuantos cuantos saltos tiene que dar.
matriz2=np.arange(0,10,1)     #primer data desde donde, hasta donde y cuan grande es el salto. (1  es ir de 1 en 1, 2 es ir de 2 en 2)
print(matriz)
print(matriz2)

matrizOne=np.ones((3,3),dtype=bool)
print(matrizOne)


impares=[n for n in matriz if n%2 !=0]      #esto me crea una lista como ya sabiamos.
imparesarray=matriz[1:10:2]                #aca estoy seleccionando los impares y me deja el array
matriz2[matriz2%2!=0]=-1

b=matriz.reshape(2,5)
        
print(imparesarray) 
print(type(impares),type(imparesarray))
print (matriz2)
        
print(b, b.shape)        