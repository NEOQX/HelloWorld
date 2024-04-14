class Mammal:
    def __init__(self,name):
        self.name = name

    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def meow(self):
        print("meow")



Dog1 = Dog(input("What is your dog name?"))
Dog1.walk()
Dog1.bark()

cat1 = Cat("LOl")
cat1.meow()