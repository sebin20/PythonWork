weight_in_kg=int(input("Enter the weight in kg: "))

height_in_cm=int(input("Enter the height in cm: "))

height_in_m= height_in_cm/100

bmi=round(weight_in_kg/height_in_m**2,1)
print(f"Your bmi is {bmi}")

if bmi>=30:
    print("Obese")

elif bmi>=25 :
    print("Over weight")
    
elif bmi >= 18.5:
    print("Normal weight")

else :
    print("Under weight")