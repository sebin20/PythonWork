# color=["red","blue","yellow"]
# print(color)
# for col in color:
#     print(col)
    
    
    
expence=[10000,12000,14000,4000]
max_num=expence[0]
min_num=expence[0]
for exp in expence:
    if exp > max_num:
        max_num=exp

    if exp<min_num:
        min_num=exp
print("Max is : ",max_num)
print("Min no is :", min_num)
sum=0
length=len(expence)
for exp in expence:
    sum=sum+exp
    
average=sum/length

print(average)
    