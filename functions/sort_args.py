def sort_number(*args,**kwargs):
    reverse_val=kwargs.get('reverse')
    if reverse_val=="True":
        sorted_num=sorted(args,reverse=True)
        print(sorted_num)   
        
    if reverse_val=="False":
        sorted_num=sorted(args)
        print(sorted_num) 
        
        
    
    
sort_number(1,2,6,4,15,11,reverse="True")
sort_number(1,2,6,4,15,11,reverse="False")