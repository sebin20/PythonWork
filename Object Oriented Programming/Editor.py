class Editor:
    
    name:str
    
    vendor:str
    
    def __init__(self,name,vendor):
        
        self.name=name
        
        self.vendor=vendor
        
    def __str__(self):
        
        return self.name
    
    
editor1=Editor("VSCode","Microsoft")

editor2=Editor("pycharm","JetBrains")

editor3=Editor("intellij","Jetbrains")


print(editor1)

print(editor2)

print(editor3)