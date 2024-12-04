prices=[7,1,5,3,4,6,9,0]
# prices=[7,6,4,3,1]
#       0 1 2 3 4 5

max_profit=0


for i in range(len(prices)-1):
    for j in range(i+1,len(prices)):
        if prices[j]-prices[i] >  max_profit:
            max_profit=prices[j]-prices[i]
            
if max_profit==0:
    print(max_profit)
     
else:
    for i in range(len(prices)):
        for j in range(len(prices)):
            if prices[j]-prices[i]==max_profit:
                print(prices[j]-prices[i])
                break
        