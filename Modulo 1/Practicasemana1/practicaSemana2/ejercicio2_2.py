cadena = "geringoso"
vocales = ["a", "e", "i", "o", "u"]
ger=["pa", "pe", "pi","po", "pu"]
capadepenapa= ""

for c in cadena:
    capadepenapa= capadepenapa+c
    if c in vocales :
        posicion=vocales.index(c)
        capadepenapa=capadepenapa+ger[posicion]

print(capadepenapa)