from abc import ABC, abstractmethod

class Editor(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def debug(self):
        pass

    @abstractmethod
    def execute(self):
        pass

class Vscode(Editor):

    def open(self):
        print("Vs code opened")

    def write(self):
         print("Vscode writed")

    def debug(self):
          print("Vs code debugged")
    def execute(self):
         print("Vs code executed")

editor = Vscode()
editor.open()
editor.write()
editor.debug()
editor.execute()
