materia1_str=input("Nota de la primer materia:")
materia1=float(materia1_str)
materia2_str=input("Nota de la segunda materia:")
materia2=float(materia2_str)
materia3_str=input("Nota de la tercer materia:")
materia3=float(materia3_str)
aprueba_con= 7
promedio=(materia1+materia2+materia3)/3

print ("El promedio es ", promedio)
if promedio>=7:
    print("El alumno aprobo el curso.")
else:
    print("El alumno no aprobo.")
