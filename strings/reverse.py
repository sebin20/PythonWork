text="malayalam"
length=len(text)-1

reverse=""
for i in range(length,-1,-1):
    reverse+=text[i]
    
print(reverse)