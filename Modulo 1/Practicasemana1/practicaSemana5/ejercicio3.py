import os
import csv

with open(".\Archivos de datos\portafolio_juan.csv", "rt") as p:
    data=csv.reader(p)
    encabezado=next(data)
    lista=[]
    for l in data:
        dat=dict(zip(encabezado,l))
        lista.append(dat)
    
    dic_fecha_gasto={}
    valor_portfolio=0    
    dinero_invertido=0
    for d in lista:
        f=d["fecha"]
        valor_compra=float(d["precio_compra"])*int(d["cantidad"])
        dinero_invertido=dinero_invertido+valor_compra
        dic_fecha_gasto[f]=valor_compra
        
        valor_actual=float(d["precio_actual"])*int(d["cantidad"])        
        valor_portfolio=valor_portfolio+valor_actual
    
    ganancia=valor_portfolio-dinero_invertido   
    print(f"La ganancia de Juan es {round(ganancia,2)}. Invirtio {round(dinero_invertido,2)} y su valor actual es de {round(valor_portfolio,2)}")
    #print(dic_fecha_gasto)   
    
with open(".\Archivos de datos\cer-uva-uvi-diarios.csv","rt") as o:
        data1=csv.reader(o)
        encabezado1=next(data1)
        
        
        
        #creo un diccionario con el valor del UVA en su respectiva FECHA
        fecha_uva={}
        
        for j in data1:
            fecha=j[0]
            uva=j[2]
            fecha_uva[fecha]=uva
        
        #creo un diccionario donde estara la fecha donde juan compro las acciones y la cantidad de UVA que podria haber comprado
        #por la misma cantidad de dinero que compro las acciones en esa fecha
        
        fecha_cantidad_uva_comprada={}
        for clave in dic_fecha_gasto:
            for clave1 in fecha_uva:
                if clave==clave1:
                    cant_uva=dic_fecha_gasto[clave]/float(fecha_uva[clave1])
                    fecha_cantidad_uva_comprada[clave]=cant_uva
                    
                    
        valor_actual_uva=208.99
        suma_cantidad_uva=0
        
        for suma in fecha_cantidad_uva_comprada:
            suma_cantidad_uva=suma_cantidad_uva+fecha_cantidad_uva_comprada[suma]
        
        total_valor_uva_actual=valor_actual_uva*suma_cantidad_uva 
        #print(fecha_cantidad_uva_comprada)   
        #print(suma_cantidad_uva)
        print(total_valor_uva_actual)

if valor_portfolio>total_valor_uva_actual:
    print(f'La opcion que mejor rindio fue la compra de las acciones, ya que su valor actual es de {round(valor_portfolio,2)}, mientras que el valor de las UVAs es de {round(total_valor_uva_actual,2)}. ')
else:
    print (f'La opcion que mas rindio fue la de las UVAs ya que su valor actual es de {round(total_valor_uva_actual,2)}, mientras que el de las acciones es de {round(valor_portfolio,2)}')       