for row in range(8,1,-1): #1
    for space in range(0,8-row): 
        print(" ",end="")
    for col in range(1,row):
        print("*",end=" ")
    print()
       