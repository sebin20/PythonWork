def two_digit(num):
    
    num_copy=num
    
    if num in tens.keys():
        return(tens[num])
        
        
    else :
        last_digit=num_copy%10
        text1=unit[last_digit]
        num_copy=num_copy//10
        text2=tens[num_copy]
        
        text=text2 +" "+ text1
        return text

num=int(input("ENter the number "))

length=len(str(num))


unit={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}

tens={10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"ninteen",2:"twenty",3:"thirty",4:"fourty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninty"}

if num <10:
    print(unit[num])
   
elif length==2:
    print(two_digit(num))
    
 
elif length==3:
    last_two_digits=num%100
    last_two_digit_text=two_digit(last_two_digits)
    first_digit=num//100
    
    print(unit[first_digit] + " hundred"+" " + last_two_digit_text)
    