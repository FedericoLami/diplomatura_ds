lista1=[x**2 for x in range(1,11)]
print(lista1)

lista2=[y for y in range(1,21) if y%2==0]
print(lista2)

ciudades=["Buenos Aires", "Madrid", "Roma", "París"]
emperaturas = [28, 16, 21, 19]

diccionario={i:j for i,j in zip(ciudades,emperaturas)}
print(diccionario)