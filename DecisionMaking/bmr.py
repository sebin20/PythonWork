import sys

weight=int(input("Enter your weight in kg :"))

height=int(input("Enter your height in cm :"))

age=int(input("Enter your age :"))

gender=int(input("Enter 1 for Male  and  2 for female :"))

if gender==1 :
   bmr=10*weight + 6.25*height - 5*age + 5


elif gender==2 :
   bmr = 10*weight + 6.25*height - 5*age - 161
   
else :
    print("You entered invalid gender")

print("your bmr is",bmr)

print("""press 1 if you are Sedentary: little or no exercise	
         
        press 2 if you Exercise 1-3 times/week
          
        press 3 if you Exercise 3-5 times/week
        
        press 4 if you Intense exercise 6-7 times/week
        
        press 5 if you do Very intense exercise daily or physical job""")

activity_level=int(input())

if activity_level==1:
    calorie=bmr * 1.2

elif activity_level==2:
    calorie=bmr* 1.375
    
    
elif activity_level==3:
    calorie=bmr*1.55
    
    
elif activity_level==4:
    calorie=bmr*1.725
    
elif activity_level==5:
    calorie=bmr*1.9

else :
    print("Invalid input.....")

print("Your eatable calorie :",calorie)

print("\n What do you wish to do....weight gain or loss  ")

user_target=int(input("\n press 1 for weight gain and 2 for loss and 3 to exit : "))

if user_target==3 :
    sys.exit(1)
    

calorie_change=int(input("\t Enter how much weight u wish to change : "))

time_period=int(input(" Enter your time period in days : "))

if user_target==1:
    weight_gain=calorie_change*7700
    weight_gain_perday=weight_gain/time_period
    
    print(f"You need to eat {weight_gain_perday+calorie} calories a day  ...")
    
elif user_target==2:
    weight_loss=calorie_change*7700
    weight_loss_perday=weight_loss/time_period
    
    print(f"You need to reduce your calory intake of {round(weight_loss_perday,2)} calories ....your eatable calory is {calorie-weight_loss_perday}")

# elif user_target==3 :
#     sys.exit("Exiting program")
    
else :    
    print("Invalid..")