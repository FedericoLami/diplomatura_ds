palabra = 'Cocos'



if "a" or "A" in palabra:
  print(f'La palabra \"{palabra}\" contiene una \"a\"')
else:
  print(f'La palabra \"{palabra}\" no contiene una \"a\"')
  
  
  # este ejercicio esta mal porque "a" y "A" al nombrarlas de esa forma, python las toma como cadena de caracteres, y efectivamente hay
  # cadena de caracteres dentro de la variable "palabra". Para que esto no suceda, hay que separa cada expresion, de la siguiente forma
  
  
palabra = 'Cocos'



if "a" in palabra or "A" in palabra:
  print(f'La palabra \"{palabra}\" contiene una \"a\"')
else:
  print(f'La palabra \"{palabra}\" no contiene una \"a\"')
  