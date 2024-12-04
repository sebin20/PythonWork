f=open("C:\\Users\\sebin\\OneDrive\\Desktop\\Python\\Datasets\\year.txt","r")

lp=open("C:\\Users\\sebin\\OneDrive\\Desktop\\Python\\Datasets\\leap_funct.txt","w")

cn=open("C:\\Users\\sebin\\OneDrive\\Desktop\\Python\\Datasets\\centuary_funct.txt","w")


def is_centuary(year):
    return True if year%100==0 else False

def is_leap(year):
    if (yr %4==0 and yr %100!=0) or (yr %100==0 and yr%400==0):
        return True
    else:
        return False


for yr in f:
    yr=int(yr)
    
    if is_leap(yr):
        lp.write(str(yr)+ "\n")
    
    if is_centuary(yr):
        cn.write(str(yr) + "\n")
    
f.close()  
lp.close()
cn.close()