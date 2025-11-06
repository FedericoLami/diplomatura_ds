import numpy as np

# a)
pares = np.arange(1000)
pares = pares[pares%2 == 0]
print(pares)

# b)
tablas = np.array([np.arange(1,11)]*10)   # Generamos un array que va del 1 al 10, la transformamos en lista con la operación * concatenamos la misma lista 10 veces
tablas = np.transpose(tablas)*tablas[0,:] # Transponemos dicho array y usando la operación * entre arrays que multiplica cada columna de tablas por tablas[0,:]
                                          # que es un array que va del 1 al 10.
print(tablas)