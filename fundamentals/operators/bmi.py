weight_in_kg=int(input("Enter the weight in kg: "))

height_in_cm=int(input("Enter the height in cm: "))

height_in_m= height_in_cm/100

bmi=round(weight_in_kg/height_in_m**2,1)

print(bmi)