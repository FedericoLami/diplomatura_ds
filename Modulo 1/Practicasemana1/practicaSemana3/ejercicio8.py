lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]



for i in lista:
    
        if i%5==0 and i%3 == 0:
            lista[i-1]="fizzbuzz"
            
        elif i%5==0:
            lista[i-1]="buzz"
        elif i%3 == 0:
            lista[i-1]="fizz"
        
print (lista)