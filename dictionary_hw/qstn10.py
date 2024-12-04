#Given a dictionary of items and their prices, write a program to apply a 10% discount to all the items using dictionary comprehension.

items_fruit = {
    "apple": 100,
    "banana": 60,
    "orange": 150,
    "milk": 30,
    "bread": 40,
    "eggs": 60,
    "cheese": 70,
    "chicken": 140,
    "rice": 45,
    "pasta": 300
}

item_new={frt: pri-(pri*10/100)  for frt,pri  in items_fruit.items() }
print(item_new)



