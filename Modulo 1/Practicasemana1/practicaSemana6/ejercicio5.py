# Para poder realizar los cálculos solicitados vamos a escribir 3 funciones: 
# cada una para calcular las 3 métricas solicitadas, pero antes vamos a importar el módulo math para 
# poder tener el valor de pi

import math
pi = math.pi

# Circunferencia:
def circunferencia(r):
  # la funcion espera un input que va a almacenar en la variable r
  return 2 * pi * r

# Superficie:
def superficie(r):
  # la funcion superficie espera un input que va a almacenar en la variable r
  return pi * (r**2)

# Volumen:
def volumen(s, a):
  # la funcion espera dos inputs, el primero lo almacena en s que es la superficie
  # el segundo en a que es la altura
  return s * a

# tanque campo 1
radio = 3    # en metros
altura = 1   # en metros
# llamamos a las funciones y le pasamos a cada una (entre parentesis) 
# el o los valores que esperan
circ = circunferencia(radio) 
sup  = superficie(radio)
vol  = volumen(sup,altura)
print("Tanque 1:", round(circ,2),"m; ", round(sup,2),"m2; ", round(vol,2),"m3.")

# tanque campo 2 
radio = 2.6    # en metros
altura = 1.2   # en metros 
circ = circunferencia(radio)
sup  = superficie(radio)
vol  = volumen(sup,altura)
print("Tanque 2:", round(circ,2),"m; ", round(sup,2),"m2; ", round(vol,2),"m3.")

# tanque campo 3
radio = 4        # en metros 
altura = 1.5     # en metros
circ = circunferencia(radio)
sup  = superficie(radio)
vol  = volumen(sup,altura)
print("Tanque 3:", round(circ,2),"m; ", round(sup,2),"m2; ", round(vol,2),"m3.")