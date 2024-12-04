import random
random_number=1
# random_number=random.randint(1,10)
# print(random_number)
num=0

while (random_number!=num) : 
    
    random_number=random.randint(1,10)
    # print(random_number)
    num=int(input("Enter the number :"))
    if random_number==num :
        print("YOu guessed right..")
    else :
        print("you guessed wrong..")
    