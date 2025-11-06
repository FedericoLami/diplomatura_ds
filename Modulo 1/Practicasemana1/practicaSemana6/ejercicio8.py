# Esta función espera dos valores: el monto de dinero disponible y el costo de cada bombón.


def bombones(monto, costo):
  numero = int(monto / costo)
  vuelto = round(monto - (costo * numero),2)
  return vuelto, numero

# La función entrega dos valores, por lo que podemos desacoplar los valores directamente en el llamado de la función
# o podemos asignar una variable a la llamada de la función y guardará en ella una tupla con todos los valores que 
# entregue la función según como esté definida.
# Aqui llamamos la función para un valor total de $1200 y un costo por unidad de $25,99
vuelto, numero = bombones(1200,25.99)
print("Puedo comprar",numero,"bombones y me dan $",vuelto,"de vuelto.")