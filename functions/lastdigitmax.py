def last_digit_max(num1,num2):
    last_digit1=num1%10
    last_digit2=num2%10
    
    print(num1 if last_digit1>last_digit2 else num2)
    
num1=int(input("Enter the number 1: "))
num2=int(input("Enter the number 2: "))
last_digit_max(num1,num2)