# Definimos una función recursiva llamada longitud 
def longitud(lista):
  if lista == []:          # me fijo si la lista está vacia
    return 0
  else:
    # si la lista no está vacía, la función devuelve 1 
    # más la longitud de la lista restante (es decir, la lista sin el primer elemento)
    return 1 + longitud(lista[1:])



# defino diferentes listas
a = []    # vacia
b = [1,2,3,5,6,7]   # con 6 elementos
print(longitud(a), len(a))
print(longitud(b), len(b))