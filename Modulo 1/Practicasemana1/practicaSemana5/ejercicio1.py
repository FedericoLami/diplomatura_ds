import os
import math as m
os.chdir('.\Practicasemana1\practicaSemana5')
#print(os.getcwd())

with open("raices.csv","w") as r:
    for i in range(1,101):
        numero=i
        raiz=m.sqrt(i)
        r.write(f'{numero}  ,  {round(raiz,3)}\n')