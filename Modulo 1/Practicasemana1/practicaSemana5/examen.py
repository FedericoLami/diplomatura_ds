def ordena(L):
    for i in range(0, len(L)-2):
        encontro=False
        for j in range (1,len(L)-1):
            if L[i] > L[j]:
                L[i], L[j]=L[j], L[i]
                encontro=True
        if encontro:
            break
    return len(L)


x=[4,2,6,5,10]
l=ordena(x)
print(x)
