for row in range(1,8,):
    for space in range(1,8-row): 
        print(" ",end="")
    for col in range(1,row):
        print("*",end=" ")
    print()
for row in range(7,1,-1): #1
    for space in range(0,7-row): 
        print(" ",end="")
    for col in range(1,row):
        print("*",end=" ")
    print()