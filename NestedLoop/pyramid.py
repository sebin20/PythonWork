for row in range(1,8):
    for space in range(1,8-row): 
        print(" ",end="")
    for col in range(1,row):
        print("*",end=" ")
    print()
       