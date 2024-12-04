arr=[100,200,300,400,500,600,700,800]
    #  0  1   2   3   4   5   6   7   8 
leng=len(arr)

left=1
if leng%2==0:
    right=leng-1
else:
    right=leng-2
    
while(left<=right):
    arr[left],arr[right]=arr[right],arr[left]
    left+=2
    right-=2
print(arr)
    