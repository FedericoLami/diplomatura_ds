def separar(lista): # la función separar espera un valor y lo guarda en la variable "lista"
    global pares
    pares = []
    global impares
    impares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    pares.sort()
    impares.sort()
    return pares, impares
    
    
    
# ejemplo
separar([4, 7, 2, 9, 10, 8, 3, 6, 1, 5])

print (pares)

