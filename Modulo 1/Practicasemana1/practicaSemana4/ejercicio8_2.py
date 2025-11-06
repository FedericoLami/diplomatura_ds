clientes = [
  (1, "Ana", "García", "ana@example.com", "Calle Falsa 123"), 
  (2, "Pedro", "Martínez", "pedro@example.com", "Avenida Siempreviva 742"),
  (3, "Luisa", "Fernández", "luisa@example.com", "Calle Falsa 123"),
  (4, "Juan", "Pérez", "juan@example.com", "Calle Falsa 123"), 
  (5, "Ana", "García", "ana@example.com", "Calle Falsa 123")
]

clientes_unicos = {}

for cliente in clientes:
    # Creamos una clave a partir de la información de contacto
    clave = (cliente[3], cliente[4])
    if clave not in clientes_unicos:
        # Si la clave no existe, agregamos la tupla completa como valor
        clientes_unicos[clave] = cliente

# Convertimos los valores del diccionario a una lista
clientes_unicos_ordenados = sorted(list(clientes_unicos.values()), key=lambda cliente: cliente[1])

print(clientes_unicos_ordenados)