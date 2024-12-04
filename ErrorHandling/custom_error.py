def voting(age):
    if age < 18:
        raise Exception("Age is low")
    
    elif age >23:
        raise Exception ("Age is high!! ")
    else :
        print("voted")

try :
    voting(30)
except Exception as e:
    print(e)
    
print("Are u voted ?")
print("Okayy")