lista=[1,2,3,4,5,6,7,8,9,10,11,12,13]
lista1=sorted(lista)
lista1.sort(reverse=True)
num=15
print (lista)
print(lista1)

posibles=[]


for j in lista[0:13]:
    for i in lista[1:13]:
        for k in lista[2:13]:
            for l in lista[3:13]:
                for m in lista[4:13]:
                    for z in lista[5:13]:
                        for x in lista[6:13]:
                            for y in lista[7:13]:
                                for p in lista[8:13]:
                                    for c in lista[9:13]:
                                        for v in lista[10:13]:
                                            for b in lista[11:13]:
                                                for n in lista[12:13]:
                                                    if j+i+k+l+m+z+x+y+p+c+v+b+n==num:
                                                        posibles.append([j,i,k,l,m,z,x,y,p,c,v,b,n])


 
print(posibles)
        
 