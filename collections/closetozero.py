nums=[2,4,-3,-4,-7,5,1]

dict_num={}

dict_num={i:abs(i)  for i in nums}

min_value=min([v  for v in dict_num.values()])

dist_st=set([k for k,v in dict_num.items() if v==min_value])

 
if len(dist_st)==1:
    
    num=list(dist_st)
    print(num[0])
    
elif len(dist_st)==2:
    
     num=list(dist_st)
     num.sort()
     print(num[1])