class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(30,40)
point1.x = 10
point1.y = 20
print(point1.y)

point1.draw() #function draw in class

#Person
#       name
#       talk()

class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f"Hi Im {self.name}")


Person1 = Person(input("What is you name? >"))
Person1.talk()