# Adding my Imported Module and what I need from it
from ninja import Ninja
# Defining my Class
class Pet:
# Initializer Method
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
# Instance Methods
    def sleep(self):
        sleep_question = input(f'Would you like to rest {self.name}?')
        if sleep_question == 'yes':
            self.energy += 25
            print(f"{self.name} is now resting, increasing his energy by 25%! Energy is now {self.energy}%.")
        else:
            print(f"Rest to gain more energy.")
        return self

    def eat(self):
        self.health += 10
        self.energy += 5
        print(f"{self.name} has now eaten! Energy is now at {self.energy}, Health is now at {self.health}%.")
        return self

    def play(self):
        play_question = input(f"Would you like to play with {self.name}?")
        if play_question == 'yes':
            self.health += 5
            print(f"You have just played with {self.name}! Health is now at {self.health}%.")
        else:
            print(f"Play with {self.name} to increase its health.")
        return self

    def noise(self):
        print("Animal Sound Animal Sound")
        return self

treat_list = ["animal_treats", "biscuits", "animal_candy"]

herxerus = Pet("herxerus", "dog", "backflip", 100, 100)

sammy = Ninja("Samuel", "Hughes", treat_list, "animal_food", herxerus)

sammy.feed()