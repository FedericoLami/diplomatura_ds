fibonacci=0
fibonacci1=1
fibonacci2=0
print (fibonacci1)
for i in range(9):
    fibonacci2=fibonacci1+fibonacci
    print (fibonacci2)
    fibonacci=fibonacci1
    fibonacci1=fibonacci2
    
    
    
    
    
    
    
    
    
    # 0 + 1 = 1
    # 1 + 1 = 2
    # 1 + 2 = 3
    # 2 + 3 = 5
    # 3 + 5 = 8
    # 5 + 8 = 13