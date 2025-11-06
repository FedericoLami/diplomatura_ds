activador=True
nombres=[]
edades=[]
materias=[]
while activador:
    nombre=input("Ingrese el nombre de los estudiantes:")
    nombres.append(nombre)
    edad=input("Ingrese la edad:")
    edades.append(edad)
    materia=input("Ingrese las materias que cursa el estudiante separadas por coma:")
    materia=tuple(materia.split(","))
    materias.append((materia))
    while activador:
        pregunta=input("¿Desea ingresar otro estudiante? Responda s para ingresar otro estudiante, n para terminar.")
    
        if pregunta=="n":
            activador=False
            break
        elif pregunta=="s":
            break
        else:
            pregunta=input("ERROR, no se reconoce el comando ingresado. PRESIONE ENTER")
    

diccionario={nombres[i]: (edades[i], materias[i]) for i in range(len(nombres))}
contador_materias={}


for tupla in materias:
    for mat in tupla:
        if mat in contador_materias:
            contador_materias[mat]=contador_materias[mat] + 1
        else:
            contador_materias[mat]=1
            


    
    



print("\n\n\n\n\n\n\n\nEsta es la lista de estudiantes con su edad y materias que cursan:\n")
for key,value in diccionario.items():
    print (f'{key:>15s} {value}')


   
print("\n\n\n\nEsta es la lista de materias y cuantos alumnos hay inscriptos en cada una:\n")
for key, value in contador_materias.items():
    print(f'{key:>12s} {value:5d}')
    