import numpy as np


puntos = np.random.rand(10000, 2)
# La manera más básica:
cantidad = 0

for punto in puntos:
  if punto[0]**2 + punto[1]**2 < 1:
    cantidad += 1

# O simplemente (y más eficiente computacionalmente):
cantidad = np.count_nonzero(puntos[:,0]**2+puntos[:,1]**2 < 1) # esta función (como dice su nombre en ingles) cuenta la cantidad de elementos distintos de cero

print('La estimación de Pi dio:', cantidad*4/10000)


def estimar_pi(n):
  puntos = np.random.rand(n, 2)
  cantidad = np.count_nonzero(puntos[:,0]**2+puntos[:,1]**2 < 1)
  
  return cantidad*4/n

print(estimar_pi(1000000))