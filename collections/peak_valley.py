arr=[3,4,2,1,1,6,4,1,3]
#    0 1 2 3 4 5 6 7 8

#len = 9   9-2=7
for i in range(len(arr)-2):
    if arr[i]<arr[i+1]>arr[i+2]:
        print("Its a peak :",arr[i],arr[i+1],arr[i+2])
        
    elif arr[i]>arr[i+1]< arr[i+2]:
        print("Its a valley :",arr[i],arr[i+1],arr[i+2])
        
