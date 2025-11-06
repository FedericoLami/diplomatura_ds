import os
import csv

with open("./Archivos de datos/arbolado-en-espacios-verdes.csv", "rt", encoding="utf-8") as f:
    filas=csv.reader(f)                             #leemos el archivo abierto y lo guardamos en la variable filas
    encabezados=next(filas)                         #asignamos los encabezados en la variable encabezados
    lineas=[]                                           
    for fila in filas:                              #asignamos a la lista "lineas" todas las filas del archivo "filas"        
        lineas.append(fila)
        
        
#asignamos a la lista "alturas_jacarandas" las alturas de los jacarandas
    alturas_jacarandas=[]
    for sublinea in lineas:                                         
        if sublinea[7]=="Jacarandá":
            alturas_jacarandas.append(sublinea[3])
        
    
    
    
    
    
#creamos un diccionario para asignar como key key el espacio verde y como valor la altura de los arboles    

    arboles__espacioverde_altura={}
    
    for sublinea in lineas:
        if sublinea[10] not in arboles__espacioverde_altura:
            arboles__espacioverde_altura[sublinea[10]]=[int(sublinea[3])]
        else:
            
            arboles__espacioverde_altura[sublinea[10]].append(int(sublinea[3]))
            
# Calculamos el maximo de cada espacio verde y lo imprimimos    
    for clave in arboles__espacioverde_altura:
        max_altura = max(arboles__espacioverde_altura[clave])
        print(f"La altura máxima para la clave '{clave}' es {max_altura}")

# Calculamos el arbol mas alto de todos y donde se encuentra        
    altura_max=0
    lugar=""
    for clave in arboles__espacioverde_altura:
        dd=max(arboles__espacioverde_altura[clave])
        if dd > altura_max:
            altura_max=dd
            lugar=clave
            
            
    print(f'El arbol mas alto mide {altura_max} y se encuentra en {lugar}')
    
    
    #Contamos la cantidad de espacios verdes e imprimimos
    total=len(arboles__espacioverde_altura)
    print(f"En total hay {total} espacios verdes")
    
    
    #creamos un archivo "palmeras.txt" donde vamos a poner todos los datos de este tipo de arbol que hay en el archivo ya abierto
    #pero primero nos paramos en la carpeta donde quiero que se guarde el nuevo archivo.
    os.chdir(".\Practicasemana1\practicaSemana5")
    with open ("palmeras.txt", "w") as p:
        for z in lineas:
            if z[9] =="Palmera":
                p.write(f"{z}\n")