# num1=int(input("Enter the first number :"))
# num2=int(input("Enter the second number :"))
# try:
#     result=num1/num2
#     print(result)
# except:
#     print("Error occured")

# print("File transfer needed after processing")
# print("DataBase commit")

def div(num1,num2):
    return (num1/num2)

num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))
try:
    print(div(num1,num2))
except:
    num2=int(input("ENTER valid second number :"))
    print(div(num1,num2))

print("File transfer needed after processing")
print("DataBase commit")