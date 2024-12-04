def student_info(*args,**kwargs):
        operator=kwargs.get('operation')
        
        if operator=="avg":
            return((sum(args)/len(args)))
        
        if operator=="total":
            return(sum(args))
    
print(student_info(45,43,44,48,operation="total"))

print(student_info(45,43,44,48,operation="avg"))