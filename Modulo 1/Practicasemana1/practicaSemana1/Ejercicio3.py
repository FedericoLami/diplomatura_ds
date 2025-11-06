nombre=input("Ingrese su nombre:")
edad_str=input("Ingrese su edad:")
edad=int(edad_str)
peso_str=input("Ingrese su peso en kilogramos:")
peso=float(peso_str)
altura_str=input("Ingrese su altura en metros:")
altura=float(altura_str)
 
imc= (peso/(altura**2))

print (nombre,"usted tiene", edad,"años y su indice de masa corporal es:", round (imc, 2))
