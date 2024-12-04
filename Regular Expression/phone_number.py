from re import fullmatch

f=open("C:\\Users\\sebin\\OneDrive\\Desktop\\Python\\Datasets\\phone_numbers.txt","r")

for line in f :
    ph_no=line.rstrip("\n")
    
    pattern="(91)?[0-9]{10}"
    
    matcher=fullmatch(pattern,ph_no)
    
    if matcher!=None:
        print(ph_no)