for year in range(1800,2025,1):
    if (year%4 ==0 and year%100!=0) or (year%100==0 and year%400==0) :
      print(year)