numero = 10

if (numero % 2) == 1:
  print('El número es impar')
else:
  print('El número es par')
if (numero % 2) == 0 or (numero % 2) == 1:
  print('El número no es ni par ni impar. Hay algo raro...')    #lo que esta mal en este ejercicio es el segundo IF. Esta de mas, ya que en el 
                                                                # primer if-else ya estan todas los resultados que puede dar la operacion
                                                                # numero % 2. 