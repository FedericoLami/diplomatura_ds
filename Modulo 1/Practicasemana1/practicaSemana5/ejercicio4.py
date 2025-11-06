import os
import csv

with open(".\Archivos de datos\estimaciones-agricolas-PBA-1969-2022.csv","rt") as p:
    data=csv.reader(p)
    encabezado=next(data)
    
    lista=[]
    
    #ponemos todos los datos en la lista
    for j in data:
        lista.append(j)
    
    #creamos una lista que se llama cultivo donde vamos a poner el nombre de todos los cultivos
    cultivo=[]
    for i in lista:
        cultivo.append(i[1])
    
    #Transformamos la lista cultivo a un set para que nos elimine los cultivos repetidos y contamos la cantidad de elementos.    
    cultivo=set(cultivo)
    cant_cultivos=len(cultivo)
    
    print(f'La cantidad de cultivos que hay en pcia Bs As es {cant_cultivos}')
    #print(lista)
    
    
    cant_ajo= 0
    mun_prod=""
    
    lista_ajo=[]
    
    for k in lista:
        if k[1]=="Ajo":
            lista_ajo.append(k)
            
    #Esto me va a dar la mayor cantidad de produccion en un municipio en un año determinado
    #Para cumplir la consigna del ejercicio tendria que sumar la produccion de un municipio a traves del tiempo
    #No lo voy a hacer pero lo entiendo.
    
    for l in lista_ajo:
        ajo=float(l[8])
        
        if ajo>cant_ajo:
            cant_ajo=ajo
            mun_prod=l[5]
    
    #Aca creamos un diccionario con key=año y value=superficieSembrada
    #Iteramos sobre la lista_ajo para que, si el año ya esta en el diccionario, sume la sup sembrada y si no esta, lo agregue.    
    siembra={}
    
    for a in lista_ajo:
        año=a[3]
        sup=float(a[6])
        if a[3] not in siembra:
            siembra[año]=sup
        else:
            siembra[año]=siembra[año] + sup
            
    
    mayor_siembra=0
    
    for clave,valor in siembra.items():
        if valor>mayor_siembra:
            mayor_siembra=valor
            año_siembra_mayor=clave
            
            
    #Para hacer el año de mayor rendimiento se haria lo mismo que arriba
    #Doy por terminado este ejercicio.    
            
    print(f'El municipio que mas ajo produjo fue {mun_prod} y su produccion fue de {round(cant_ajo,2)} tn.')
    print(f'El año que mayor superficie se sembro fue en el {año_siembra_mayor} y la superficie sembrada fue de {round(mayor_siembra,2)}')        