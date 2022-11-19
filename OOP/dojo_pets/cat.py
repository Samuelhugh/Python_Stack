# Importing the Superclass, So I can use Python Inheritance Syntax and Pythons' Super() Syntax and Parent Module I used to Derive this Subclass 
from pet import Pet
# Utilizing Python Inheritance Syntax to Define the Subclass
class Cat(Pet):

    def __init__(self, name, type, tricks, health, energy):
        super().__init__(name, type, tricks, health, energy)
        # self.name = name
        # self.type = type
        # self.tricks = tricks
        # self.health = health
        # self.energy = energy

    def hello(self):
        print(f"Hello, {self.name}")

    def printType(self):
        print(f"Animal Type: {self.type}")

    def printTricks(self):
        for trick in range(len(self.tricks)):
            print(f'Trick: {self.tricks[trick]}')

    def sleep(self):
        super().sleep()

    def eat(self):
        super().eat()

    def play(self):
        super().play()

    def noise(self):
        super().noise()

list_of_tricks = ["Roll Over", "Purr", "Open doors"]

squshy = Cat("babba", "Rare Cat", list_of_tricks, 100, 100)

squshy.hello()
squshy.sleep()
squshy.printTricks()
squshy.play()