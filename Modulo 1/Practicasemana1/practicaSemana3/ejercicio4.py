cadena= "Con la banda de Newells Old Boys a tdodos lados siempre voy, de la cabeza"
vocales= ["a", "A" , "e", "E", "i", "I", "o", "O", "u", "U"]

total=0

for i in vocales:
    
    cantidad=cadena.count(i)
    print(f'{i} = {cantidad}')
    total=total + cantidad


print(f'En la cadena hay {total} vocales.')
