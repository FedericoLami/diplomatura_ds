normal=["roma","azucar", "sergio", "arroz"]
palindromo=["antonio", "amor", "cultura", "coca", "zorra"]
alreve=[]

len(normal)
len(palindromo)

for i in range(len(palindromo)):   #este for agarra los elementos de la lista palindromo y los escribe al reves.
    alreve.append(palindromo[i][::-1])
    

for j in range(len(normal)):
    for k in range(len(palindromo)):
        if normal[j] == alreve[k]:
            print (f'Las palabras {normal[j]} y {palindromo[k]} son palindromo.')