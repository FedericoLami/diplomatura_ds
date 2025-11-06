nombre=["Juan", "Ana", "Marcela", "Claudio", 'Nicolás', 'Cecilia', 'Tomas', 'Pedro']
edades=[25, 15, 13, 21, 45, 32, 17, 33]


pares=list(zip(nombre,edades))
pares_mayor=[par for par in pares if par[1]>18]
#for par in pares:
    
 #   if par[1]>18:
  #      pares_mayor.append(par)
        
pares_mayor.sort()
print(pares_mayor)

