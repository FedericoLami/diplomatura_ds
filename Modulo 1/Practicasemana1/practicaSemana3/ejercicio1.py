lista=["newells", "eduardo", "ornitorrinco", "cualquier cosa aqui"," java"]
valor=[]

for i in range(0,5):  #recorro la lista
    j=len(lista[i])     #mido la cantidad de caracteres de cada elemento
    valor.append(j)       # agrego a la lista "valor" la cantidad de caracteres de cada elemento


max(valor)       # veo cual es el valor mas alto dentro de la lista "valor"
valor.index(max(valor))   # tomo el indice del valor mas alto en la lista "valor"
print(f'La cadena mas larga es "{lista[valor.index(max(valor))]}"')    
    



