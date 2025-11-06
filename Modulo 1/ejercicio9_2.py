# Crear un diccionario para almacenar información de los estudiantes
estudiantes = {}

# Loop para permitir que el usuario registre información de estudiantes
while True:
    # Pedir información del estudiante
    nombre = input("Ingrese el nombre del estudiante (o presione enter para salir): ")
    if nombre == "":
        break
    apellido = input("Ingrese el apellido del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    materias = input("Ingrese una lista de materias en las que está inscrito el estudiante (separadas por comas): ")
    materias = [materia.strip() for materia in materias.split(",")]

    # Guardar la información del estudiante en el diccionario
    estudiantes[nombre + " " + apellido] = {"edad": edad, "materias": materias}

# Mostrar cuántos estudiantes hay inscritos en cada materia
materias_inscritas = {}
for estudiante in estudiantes.values():
    for materia in estudiante["materias"]:
        if materia in materias_inscritas:
            materias_inscritas[materia] += 1
        else:
            materias_inscritas[materia] = 1

# Mostrar información sobre las materias a las que hay estudiantes inscritos
print("Materias con estudiantes inscritos:")
for materia, cantidad in materias_inscritas.items():
    print("- {} ({})".format(materia, cantidad))
    
    
print(estudiantes)
