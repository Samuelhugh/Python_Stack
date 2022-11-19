# Defining my Class, The File name and Class name does not have to be the same
class Ninja:
# Initializer Method, Must Provide self for Python
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
# Instance Methods
    def hello(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

    def treat_list(self):
        for treat in range(len(self.treats)):
            print(self.treats[treat])

    def walk(self):
        output_variable = input(f'Would you like to walk {self.pet.name}?')
        if output_variable == 'yes':
            print(f"Walking {self.pet.name}.")
            self.pet.play()
        else:
            print('No walkies today')

    def feed(self):
        print(f"Feeding {self.pet.name} {self.pet_food}!")
        self.pet.eat()

    def bathe(self):
        print(f"{self.first_name} gave {self.pet.name} a bath.")
        self.pet.noise()

if __name__ == "__main__":
    print("The File is being executed directly")
else:
    print("The File is being executed because it is Imported by another File. The File is called: ", __name__)