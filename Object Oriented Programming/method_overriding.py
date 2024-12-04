class Parent:
    def color(self):
        print("Parent class color")
        
    def box(Self):
        print("BOx from parent")
        
class Child(Parent):
    def color(self):
        print("Child class color")
        
child_insta=Child()  # This phenomenon is called method overridding
child_insta.box()