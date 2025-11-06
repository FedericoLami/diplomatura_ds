a=[8,7,7,6,9,10,8,9]
b=[9,8,8,9,5,8,9,7]

promedioa=sum(a)/len(a)
promediob=sum(b)/len(b)

if promedioa>promediob:
    print(f'El alumno A tiene una nota de {promedioa} y es mayor que la nota {promediob} del alumno B')
elif promediob==promedioa:
    print(f'Los alumnos tienen el mismo promedio: {promedioa}')
else:
    print(f'El alumno B tiene una nota de {promediob} y es mayor que la nota {promedioa} del alumno A')
        
