materia1=[]
materia2=[]
materia3=[]
aprueba_con= 7
for x in range(5):
    nota1_str=input("Ingrese las notas de Materia1: ")
    nota1=float(nota1_str)
    materia1.append(nota1)

promedio1= sum(materia1)/len(materia1)
print (materia1)
print (promedio1)

if promedio1>=aprueba_con:
    for y in range(5):
        nota2_str=input("Ingrese las notas de Materia2: ")
        nota2=float(nota2_str)
        materia2.append(nota2)
    promedio2= sum(materia2)/len(materia2)
    print (materia2)
    print (promedio2)
    if promedio2>=aprueba_con:
        for z in range(5):
            nota3_str=input("Ingrese las notas de Materia3: ")
            nota3=float(nota3_str)
            materia3.append(nota3)
        promedio3= sum(materia3)/len(materia3)
        print (materia3)
        print (promedio3)
        if promedio3>=aprueba_con:
            promediototal=(promedio1+promedio2+promedio3)/3
            print ("El alumno aprobo el curso con un promedio de  ", promediototal)
        else:
            print ("El alumno no aprobo la Materia3, por lo tanto no aprobo el curso.")
    else: 
         print("El alumno no aprobo la Materia2, por lo tanto no aprobo el curso.")
else:
    print("El alumno no aprobo la Materia1, por lo tanto no aprobo el curso.")