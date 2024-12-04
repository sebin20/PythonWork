class SuperHero:
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit

    def __str__(self):
        return self.name

class SpiderMan(SuperHero):
    
    def __init__(self,name,suit):
        super().__init__(name,suit)
    
    def superpower(self):
        print("super powers are: sticky hands,web shooting")

class MinnalMurali(SuperHero):
    
    def __init__(self,name,suit):
        super().__init__(name,suit)
        
    def superpower(self):
        print("super powers are: strength,flying ")

spiderman = SpiderMan("Spider-Man", "Red and Blue Suit")
minnalmurali = MinnalMurali("Minnal Murali", "Blue Suit with Lightning Bolt")

print(spiderman)
print(spiderman.suit)
spiderman.superpower()