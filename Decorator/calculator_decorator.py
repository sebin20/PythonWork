def swap_dec(fn):

    def wrapper(n1,n2):

        if n1<n2:

            (n1,n2)=(n2,n1)

        return fn(n1,n2)

    return wrapper

@swap_dec
def addition(num1,num2):

    return num1+num2

@swap_dec
def substraction(num1,num2):

    return num1-num2

@swap_dec
def division(num1,num2):

    return num1/num2

print(addition(10,23))

print(substraction(10,23))

print(division(10,23))
