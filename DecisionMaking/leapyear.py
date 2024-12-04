year=int(input("Enter a year to check leap year or not :"))
if (year%4 ==0 and year%100!=0) or (year%100==0 and year%400==0) :
      print("Its a leap year..")
    
else: 
    print("Its not leap year")