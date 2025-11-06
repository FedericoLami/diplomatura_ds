lista1=input("Ingrese una lista de numeros enteros separados por coma:")
lista_entero1=lista1.split(",")
lista2=input("Ingrese otra lista de numeros enteros separados por coma:")
lista_enetero2=lista2.split(",")

conjunto1=set(lista_entero1)
conjunto2=set(lista_enetero2)

print(conjunto2 | conjunto1)
print(conjunto1 & conjunto2)
print(conjunto1 - conjunto2)
print(conjunto2 - conjunto1)

