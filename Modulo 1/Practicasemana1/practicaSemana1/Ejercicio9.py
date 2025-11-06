dias=int(input("Ingrese los dias: "))
horas=int(input("Ingrese las horas: "))
minutos=int(input("Ingrese los minutos: "))
segundos=int(input("Ingrese los segundos: "))    


dias_a_segundos=dias*86400
horas_a_segundos=horas*3600
minutos_a_segundos=minutos*60

total_segundos=dias_a_segundos+horas_a_segundos+minutos_a_segundos+segundos

print("El total de segundos es : ", total_segundos)