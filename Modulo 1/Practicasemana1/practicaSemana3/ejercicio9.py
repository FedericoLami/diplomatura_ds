nombres = ['Laura', 'Juan', 'Tomás', 'Ana', 'Diego', 'Carla', 'Kim', 'Sofía']
apellidos = ['Pérez', 'Isla', 'Gómez', 'Castro', 'Roca', 'Romero', 'Díaz', 'López']
notas = [7, 4, 9, 5, 7, 8, 6, 10]

nombreapellido=[]

for i in range(len(nombres)):                               #llenamos la lista nombreapellido con los nombres y los apellidos en un mismo elemento
    nombreapellido.append(nombres[i])                                   
    nombreapellido[i]=(nombreapellido[i],apellidos[i], notas[i])
    
orden=sorted(nombreapellido,key=lambda x: x[1])        #ordenamos alfabeticamente segun el segundo parametro , es decir, los apellidos.

for j in range(len(nombreapellido)):
    print(orden[j])
    
    

promedio= sum(notas)/len(notas)
alta=max(notas)
baja=min(notas)

print(f'La nota mas alta es {alta} y la mas baja es {baja}. El promedio es {promedio}')


aprobados=[]
aprobados_bool=[]
for k in range(len(notas)):
    if 7<=notas[k]:
        aprobados.append(nombreapellido[k])
        aprobados_bool.append(True)
    else:
        aprobados_bool.append(False)
        
        
print (aprobados)
print (aprobados_bool)

