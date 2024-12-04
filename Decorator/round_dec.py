def swap_dec(fn):

    def wrapper(n1,n2):

        if n1<n2:

            (n1,n2)=(n2,n1)

        return fn(n1,n2)

    return wrapper

def round_dec(fn):
    def wrapper(num1,num2):
        num1=round(num1)
        num2=round(num2)
        
        return num1,num2
    return wrapper

@swap_dec
@round_dec
def substraction(num1,num2):

    return num1-num2


@swap_dec
@round_dec
def division(num1,num2):

    return num1/num2



print(substraction(10.5,15.5))

print(division(10.9,44.1))
