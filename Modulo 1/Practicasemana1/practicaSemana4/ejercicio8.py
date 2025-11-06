clientes = [

  (1, "Ana", "García", "ana@example.com", "Calle Falsa 123"), 

  (2, "Pedro", "Martínez", "pedro@example.com", "Avenida Siempreviva 742"),

  (3, "Luisa", "Fernández", "luisa@example.com", "Calle Falsa 123"),

  (4, "Juan", "Pérez", "juan@example.com", "Calle Falsa 123"), 

  (5, "Ana", "García", "ana@example.com", "Calle Falsa 123")
  
  ]


lista_nueva=[]


for x in clientes:
     for y in clientes:
        if x[0]==y[0]:
            continue
        elif x[1:4]==y[1:4]:
            clientes.remove(y)
            

clientes.sort(key=lambda x:x[1])
                     
            

for l in clientes:
    print(l)