# arr=[0,1,2,3,4,5]
# index=int(input("Enter index :"))
# try :
#     print(arr[index])
    
# except:
#     index=int(input("Enter valid index:"))
#     print(arr[index])
    
# finally:
#     print("code to print elements of arr using index")

arr=[0,1,2,3,4,5]
index=int(input("Enter index :"))
try :
    print(arr[index])
    
except Exception as e:
    # print("Error occured ")
    print("Error occured-->", e)    
    
finally:
    print("code to print elements of arr using index")