f=open("C:\\Users\\sebin\\OneDrive\\Desktop\\Python\\Datasets\\year.txt","r")

lp=open("C:\\Users\\sebin\\OneDrive\\Desktop\\Python\\Datasets\\leap.txt","w")

cn=open("C:\\Users\\sebin\\OneDrive\\Desktop\\Python\\Datasets\\centuary.txt","w")

for yr in f:
    yr=int(yr)
    if (yr %4==0 and yr %100!=0) or (yr %100==0 and yr%400==0):
        lp.write(str(yr)+ "\n")
    
    if yr %100==0:
        cn.write(str(yr) + "\n")
    
f.close()  
lp.close()
cn.close()