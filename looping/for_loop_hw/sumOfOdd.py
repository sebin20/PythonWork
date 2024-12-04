target=int(input("Enter the range :"))

sum=0

for i in range(1,target+1):
   if i%2!=0: 
       sum=sum+i
print(sum)

# for i in range(1,target+1,2):
#     sum=sum+i
# print(sum)