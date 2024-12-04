nums=[1,2,3,4]

op=[]
n=len(nums)
prefix=[1]*n  

suffix=[1]*n

#loop for prefix
#          [1,2,3,4]
#          [1,1,2,6]

for i in range(1,n):
    prefix[i]=prefix[i-1]*nums[i-1]

#loop for suffix 
#          [1,2,3,4]
#          [1,1,1,1]

for i in range(n-2,-1,-1):
    suffix[i]=suffix[i+1]*nums[i+1]
    
for i in range(n):
    j=prefix[i]*suffix[i]
    op.append(j)
    
print(op)
    
    
    
    

        
    
