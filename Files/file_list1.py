f=open("C:\\Users\\sebin\\OneDrive\\Desktop\\Python\\Datasets\\fruits.txt","r")
fruits=[]

for frt  in f:
    fruits.append(frt.rstrip("\n"))
    
print(fruits)