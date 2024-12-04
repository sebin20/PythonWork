cars=[
    {"id":1,
     "name":"fronx",
     "price":1200000,
     "brand":"nexa",
     "colors":["red","blue","white"],
     "transmissions":["manuel","amt","cvt"]},
    
    
    {
     "id":2,
     "name":"baleno",
     "price":1100000,
     "brand":"nexa",
     "colors":["grey","blue","white"],
     "transmissions":["manuel","amt","cvt"]
     },
    
    {"id":3,"name":"3xo",
     "price":900000,
     "brand":"mahindra",
     "colors":["red","white","black"],
     "transmissions":["amt","cvt"]},
    
    
    {"id":4,
     "name":"punch",
     "price":700000,
     "brand":"tata",
     "colors":["red","blue","white","green"],
     "transmissions":["manuel","cvt"]},
    
    {"id":5,
     "name":"nexon",
     "price":1400000,
     "brand":"tata",
     "colors":["red","white"],
     "transmissions":["manuel","amt","cvt"]},
    
    {"id":6,
     "name":"kiger",
     "price":1000000,
     "brand":"renault",
     "colors":["blue","white"],
     "transmissions":["manuel","cvt","dct"]},
    
    {"id":7,
     "name":"taigun",
     "price":2300000,
     "brand":"volkswagon",
     "colors":["red","blue","white"],
     "transmissions":["manuel","cvt","torque"]},
]


#To print count of vehicles

print(f"Total no of cars = {len(cars)}")


#To print available colors of baleno   ----->  use next() to avoid nested list

colors_baleno=[car.get("colors") for car in cars if car.get("name")=="baleno"]  
# colors_baleno=next(car.get("colors") for car in cars if car.get("name")=="baleno")
print(colors_baleno)

# color=[]
# color.extend(*colors_baleno)
# print(color)

#print all brands

brands=[car.get("brand") for car in cars ]
print(set(brands))

#print car names available in amt transmission

amt_car_names=[car.get('name') for car in cars if 'amt' in car.get("transmissions")]
print(amt_car_names)

# To print cars in blue color

cars_in_blue=[car.get("name") for car in cars if "blue" in car["colors"]]
print(cars_in_blue)

# To print all transimission types

transmission=[]
transmission_types=[car.get("transmissions") for car in cars]

# for item in transmission_types:    
#     transmission.extend(item)
# print(set(transmission))

for item in transmission_types:
    
    for trans in item:
        
        transmission.append(trans)
        
print(set(transmission))

# To print all colors in cars

all_colors=[color for car in cars for color in car.get("colors")]
print(set(all_colors))

#most popular color

color_count={col:all_colors.count(col)   for col in all_colors }
print(color_count)

most_popular_color=max(all_colors,key=lambda col: all_colors.count(col))
print(most_popular_color)

#costly car

costly_car_price=max([car.get("price") for car in cars ])

print(costly_car_price)

costly_car=[car.get("name")  for car in cars if car.get("price")==costly_car_price]

print(costly_car)

# Or 

costly_car=max(cars,key=lambda car:car.get('price'))
print(costly_car.get('name'))



#minimum cost

minimum_cost_price=min([car.get("price") for car in cars ])

minimum_cost_car=[car.get("name")  for car in cars if car.get("price")==minimum_cost_price]

print(minimum_cost_car)


#sort car with price

sorts_car=sorted(cars,key=lambda car:car.get('price'))

sort_dict={car.get('name'):car.get('price')  for car in sorts_car }
print(sort_dict)