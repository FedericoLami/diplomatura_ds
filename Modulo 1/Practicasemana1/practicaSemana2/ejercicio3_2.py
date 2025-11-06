meses=["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
dias=[31,28,31,30,31,30,31,31,30,31,30,31]
mes=[1,2,3,4,5,6,7,8,9,10,11,12]

num_mes=int(input("Ingrese un numero de mes:"))

for c in mes:
    if c==num_mes:
        posicion=mes.index(c)
        print(f'El mes {num_mes} tiene {dias[posicion]} dias y es {meses[posicion]}')
        

