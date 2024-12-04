class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print( f"The {self.name}-->{self.sound}")


lion = Animal("Lion", "Roar")
cat = Animal("Cat", "Meow")

lion.make_sound()  
cat.make_sound()
