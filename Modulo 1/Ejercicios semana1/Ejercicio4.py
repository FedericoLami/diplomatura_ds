capital_inicial=100
interes_anual=1.1
for i in range(7):
    capital_inicial=capital_inicial*interes_anual
capital_final=capital_inicial
total= f'El capital total despues de 7 años es U$S {capital_final:5.2f}'
print (total)