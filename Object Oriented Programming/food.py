class Cusine:
    cusine_name:str
    
    def __init__(self,cusine_name):
        self.cusine_name=cusine_name
        
    def display_cusine(self):
        print(self.cusine_name)
        
        
class MealType:
    meal_type:str
    
    def __init__(self,meal_type):
        self.meal_type=meal_type
        
        
    def display_meal_type(self):
        print(self.meal_type)
        
class Dish(Cusine,MealType):
    dish:str
    
    def __init__(self,cusine_name,meal_type,dish):
        Cusine.__init__(self,cusine_name)
        MealType.__init__(self,meal_type)
        self.dish=dish
        
    def Display_dish(self):
        self.display_cusine()
        self.display_meal_type()
        print(self.dish)
        
        
dish=Dish("Indian","Lunch","Chicken_fry")
dish.Display_dish()