alquiler_por_dia= 3000
precio_kilometro= 220

dias= int(input("Ingrese el total de dias alquilado: "))
kilometros=float(input("Ingrese el total de kilometros recorridos: "))

total_a_pagar= (dias*alquiler_por_dia)+(kilometros*precio_kilometro)


print ("El saldo a pagar es de :", round(total_a_pagar,2))