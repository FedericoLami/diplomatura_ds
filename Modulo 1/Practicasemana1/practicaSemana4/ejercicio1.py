numeros=input("Ingrese una lista de numeros separados por comas:")
lista_numeros=numeros.split(",")

numeros2=[]
for i in lista_numeros:
    try:
        numero_float=float(i)
        numeros2.append(numero_float)
    except ValueError:
        print ("ERROR: La lista ingresada no cumple los requisitos.")
        break
else:
    numeros2=tuple(numeros2)
        

    print(numeros2)
    print(f'La suma de los numeros es: {sum(numeros2)}')
        





    