class Animal:
    num_of_inst = 0

    def __init__(self, phrase):
        self.phrase = phrase
        Animal.num_of_inst = Animal.num_of_inst + 1

    def say(self, phrase = None):
        print(self.phrase if phrase is None else phrase)

class Cat(Animal):
    def __init__(self, phrase='Nya'):
        super().__init__(phrase)

class Cow(Animal):
    def __init__(self, phrase='Moo'):
        super().__init__(phrase)

class Dog(Animal):
    def __init__(self, phrase='Woof'):
        super().__init__(phrase)

def print_num():
    print(Animal.num_of_inst)

cat = Cat()
cow = Cow()
dog = Dog()

cat.say()
cow.say()
dog.say()

print_num()