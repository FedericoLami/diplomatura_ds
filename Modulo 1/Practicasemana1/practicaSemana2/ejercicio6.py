numeros=[1,2,3,4,5,6,7,8,9,10]

print(numeros[3:6]) #imprimo lista desde el elemento 3 incluido hasta el elemento 6 (no incluido)
print (numeros[2:9:2]) #sintaxis es [principio(incluido): fin(no incluido): step(salto)]

t=sorted(numeros)     # a 't' le asignamos la lista 'numeros' ordenada ascendentemente. En este caso queda igual porque 'numeros' ya esta ordenada.
t.sort(reverse=True)  # ordenamos 't' de manera descendente
print(t)

for index, value in enumerate(numeros):
    if index==2:
        numeros[index]=index*10
    elif index ==3:
        numeros[index]=index*10
    elif index ==4:
        numeros[index]=index*10
        
        
        
print (numeros)
    
    