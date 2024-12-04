class Parent:
    def vehicles(self):
        self.bikes=["passion pro","ACtiva"]
        return self.bikes
    
class Child(Parent):
    def vehicles(self):
        self.bikes=super().vehicles()
        self.bikes.append("Hunter")
        
        return self.bikes
    
child=Child()

print(child.vehicles())