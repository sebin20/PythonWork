def random_numbers(start,stop,end=2):
    while(start<=stop):
        print(start)
        start=start+end
        
start=int(input(" enter start"))
stop=int(input("Enter the stop :"))
# ens=int(input("Enter stepp:"))
random_numbers(start,stop)