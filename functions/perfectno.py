num=int(input("Enter the number :"))

def perfectno(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    if sum==num:
            print("Perfect number..")
    
    else :
            print("Not perfcet..")
perfectno(num)
    
