class Pet:

    def __init__(self, type, health, energy, tricks):
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        question = input('Would you like to rest? ')
        if question == 'y':
            self.energy += 25
            print(f"Your {self.type} is resting. His energy has increased by 25%! Energy is now {self.energy}%!")
        else:
            print(f"Rest your {self.type} to gain more energy.")
        return self

    def eat(self):
        question1 = input(f"Would you like to feed your {self.type}? ")
        if question1 == 'y':
            self.energy += 5
            self.health += 10
            print(f"Your {self.type} has ate! Energy is now {self.energy}, Health is now {self.health}")
        else:
            print(f"Your {self.type} did not eat today!")
        return self

    def play(self):
        question2 = input(f"Would you like to play with your {self.type}? ")
        if question2 == 'y':
            self.health += 5
            print(f"You have now played with your {self.type}! Health is now {self.health}%")
        else:
            print(f"Play with your {self.type} to increase its health.")
        return self

    def noise(self):
        print("bark bark")
        return self