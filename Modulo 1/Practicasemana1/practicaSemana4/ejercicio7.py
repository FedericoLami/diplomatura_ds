entrada=input("Ingrese una lista de palabras separadas por espacio:")
entrada_tupla=tuple(entrada.split())

contador_letras={}

for palabra in entrada_tupla:
    for letra in palabra:
        if letra in contador_letras:
            contador_letras[letra]= contador_letras[letra] + 1
        else:
            contador_letras[letra]=1
            

letra_maxima_repetida= max(contador_letras, key=contador_letras.get)
print(entrada_tupla)
print(letra_maxima_repetida, contador_letras[letra_maxima_repetida])


