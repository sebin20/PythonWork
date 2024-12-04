#Given a sentence, count the frequency of each word using a dictionary.

str="The cat sat on the mat and the cat looked around on mat"
str_lst=str.split(" ")
dict_demo={}
for wrd in str_lst:
    if wrd in dict_demo:        
        dict_demo[wrd]+=1
        
    else :                           #dict_demo={wrd:str_lst.count(wrd) for wrd in str_lst }
        dict_demo[wrd]=1
        
print(dict_demo)
