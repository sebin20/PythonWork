arr1=[10,12,13,14,1,11]
arr2=[11,12,14,16,18]

p1=0
p2=0

arr1.sort()
arr2.sort()

while((p1<len(arr1)) and ( p2<len(arr2))):
    if arr1[p1]==arr2[p2]:
        print(arr1[p1])
        p1+=1
        p2+=1
        
    elif arr1[p1]<arr2[p2]:
       
        p1+=1
        
    elif arr1[p1]>arr2[p2]:
        p2+=1

