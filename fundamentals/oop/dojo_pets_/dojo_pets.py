class Ninja:

    def __init__(self, first_name, last_name, pet, pet_food, treats):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def hello(self):
        print(f"hello my name is {self.first_name} {self.last_name}, {self.pet.name}. Would you like some {self.pet_food}?")

    def listMyTreats(self):
        print(f"what kind of treats would you like, boy? I have {self.treats}.")

    def feed(self):
        food = input(f"What would you like to feed your pet ->>> {self.treats} or {self.pet_food}? ")
        if food == "dog treats":
            print(f"{self.pet.name} loves Treats!")
        elif food == "dog biscuits":
            print(f"{self.pet.name} loves Treats!")
        elif food == "dog bone":
            print(f"{self.pet.name} loves Treats!")
        elif food == self.pet_food:
            print(f"{self.pet.name} just ate some {self.pet_food}")
        else:
            print(f"{self.pet.name} did not eat")

    def walk(self):
        output = input(f'Would you like to walk {self.pet.name}? ')
        if output == 'y':
            print(f"{self.first_name} is walking {self.pet.name}")
        else:
            print('No walkies today')


    def bathe(self):
        bath = input(f"Would you like to clean your {self.pet.name}? ")
        if bath == 'y':
            print(f"{self.first_name} is now bathing {self.pet.name}!")
        else:
            print(f"Your {self.pet.name} is dirty. You should bathe it.")


class Pet:

    def __init__(self, name, type, health, energy, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def yourName(self):
        print(f"Your name is {self.name}")

    def printType(self):
        print(f"This is your animal type: {self.type}")

    def printTricks(self):
        print(f"You can do the following tricks: {self.tricks}")

    def sleep(self):
        question = input('Would you like to rest to increase your energy? ')
        if question == 'y':
            self.energy += 25
            print(f"{self.name} is resting. His energy has increased by 25%! Energy is now {self.energy}%!")
        else:
            print(f"Rest to gain more energy.")

    def eat(self):
        question1 = input(f"Would you like to eat to increase your energy and health? ")
        if question1 == 'y':
            self.energy += 5
            self.health += 10
            print(f"{self.name} has ate! Energy is now {self.energy}%, Health is now {self.health}%")
        else:
            print(f"Your {self.type} did not eat today!")

    def play(self):
        question2 = input(f"Would you like to play to increase your health? ")
        if question2 == 'y':
            self.health += 5
            print(f"You have played for an hour! Health is now {self.health}%")
        else:
            print(f"Play to increase your health.")

    def noise(self):
        print("bark bark")


class Cat(Pet):

    def __init__(self, name, type, health, energy, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def yourName(self): #changed the sentence from Cat class
        print(f"Your name is now {self.name}")

    def printType(self):
        print(f"This is your animal type: {self.type}")

    def printTricks(self):
        print(f"You can do the following tricks: {self.tricks}")

    def sleep(self):
        question = input('Would you like to rest to increase your energy? ')
        if question == 'y':
            self.energy += 25
            print(f"{self.name} is resting. His energy has increased by 25%! Energy is now {self.energy}%!")
        else:
            print(f"Rest to gain more energy.")

    def eat(self):
        question1 = input(f"Would you like to eat to increase your energy and health? ")
        if question1 == 'y':
            self.energy += 5
            self.health += 10
            print(f"{self.name} has ate! Energy is now {self.energy}%, Health is now {self.health}%")
        else:
            print(f"Your {self.type} did not eat today!")

    def play(self):
        question2 = input(f"Would you like to play to increase your health? ")
        if question2 == 'y':
            self.health += 5
            print(f"You have played for an hour! Health is now {self.health}%")
        else:
            print(f"Play to increase your health.")

    def noise(self):
        print("bark bark")

# class Pet attributes and methods /W Encapsulation
tyson = Pet( "cash", "german shepard", 100, 100, "roll, speak, fetch") #Created an instance/object of the class Pet and assigned it to a variable "tyson" with all of the required attributes
tyson.yourName() #created Methods for the class Pet
tyson.printType()
tyson.printTricks()
tyson.sleep()
tyson.eat()
tyson.play()
tyson.noise()

# class Cat(Pet) attributes and methods /W Polymorphism and Encapsulation
simba = Cat("fish", "IDK", 100, 100, "climb stuff") #instance of polymorphosim with the class Pet to the class Cat(Pet) (still using the same attributes as the Pet class)
simba.yourName() # Modifying A method of the class Cat(Pet) using polymorphism to alter a Method

# class Ninja creating an instance of a Ninja and setting attributes and then creating methods /W Encapsulation
sam = Ninja("Sam", "Hughes", tyson, "dog food", "dog treats, dog biscuits, dog bone") #instance/object of a Ninja, With a class Pet assigned to it and one of it attribute
sam.hello() # Method calls for the class Ninja and below
sam.listMyTreats()
sam.feed()
sam.walk()
sam.bathe()