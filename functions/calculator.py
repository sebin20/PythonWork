def calculator(*args,**kwargs):
        operator=kwargs.get('operation')
        prod=1
        if operator=="+":
            return(sum(args))
        
        if operator=="*":
            for i in args:
                prod=prod*i
            return(prod)
    
print(calculator(10,10,2,20,operation="+"))