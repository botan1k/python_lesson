class Animal:
    def voice(self):
        pass

class Cat(Animal):
    def voice(self):
        Animal.voice(self)

class Cow(Animal):
    def voice(self):
        Animal.voice(self)

class Dog(Animal):
    def voice(self):
        Animal.voice(self)


cat = Cat
cow = Cow
dog = Dog

cat.voice('Nya')
cow.voice('Moo')
dog.voice('Woof')
