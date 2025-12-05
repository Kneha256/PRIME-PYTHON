#hiding internal features and showing only impotant data to client
from abc import ABC, abstractmethod

class Animal(ABC):
    def make_sound(self):
        pass

class lion(Animal):
    def make_sound(self):
        print("roar")

class cat(Animal):
    def make_sound(self):
        print("Meow")

lion1=lion()
lion1.make_sound()
cat1=cat()
cat1.make_sound()