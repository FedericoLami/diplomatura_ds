a=75000
b=230000

años=1

while a<b:
    años+=1
    a=a+a*4/100
    b=b+b*1.2/100
    
print (f'Al año {años} el pais A va a tener {round(a,0)} habitantes y el pais B tendra {round(b,0)} habitantes.')