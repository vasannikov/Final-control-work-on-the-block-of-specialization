import datetime
from models import Dog, Cat, Hamster, Horse, Donkey

class Registry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def list_animals(self):
        for animal in self.animals:
            print(f"{animal.get_name()} (Born: {animal.get_birth_date()}) - Type: {type(animal).__name__}")

    def find_animal(self, name):
        for animal in self.animals:
            if animal.get_name() == name:
                return animal
        return None

def add_new_animal(registry):
    name = input("Enter animal name: ")
    birth_date_str = input("Enter birth date (YYYY-MM-DD): ")
    try:
        birth_date = datetime.datetime.strptime(birth_date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    print("Select type of animal:")
    print("1. Dog")
    print("2. Cat")
    print("3. Hamster")
    print("4. Horse")
    print("5. Donkey")
    animal_type = input("Enter your choice: ")

    if animal_type == '1':
        animal = Dog(name, birth_date)
    elif animal_type == '2':
        animal = Cat(name, birth_date)
    elif animal_type == '3':
        animal = Hamster(name, birth_date)
    elif animal_type == '4':
        animal = Horse(name, birth_date)
    elif animal_type == '5':
        animal = Donkey(name, birth_date)
    else:
        print("Invalid choice. Animal not added.")
        return

    registry.add_animal(animal)
    print(f"{animal.get_name()} has been added to the registry.")


def view_animal_commands(registry):
    name = input("Enter animal name: ")
    animal = registry.find_animal(name)
    if animal:
        commands = animal.get_commands()
        if commands:
            print(f"{animal.get_name()} knows the following commands: {', '.join(commands)}")
        else:
            print(f"{animal.get_name()} does not know any commands yet.")
    else:
        print("Animal not found.")


def teach_animal_command(registry):
    name = input("Enter animal name: ")
    animal = registry.find_animal(name)
    if animal:
        command = input("Enter the new command: ")
        animal.learn_command(command)
        print(f"{animal.get_name()} has learned the command: {command}")
    else:
        print("Animal not found.")


def main_menu(registry):
    while True:
        print("nRegistry Menu:")
        print("1. Add New Animal")
        print("2. List Animals")
        print("3. View Animal Commands")
        print("4. Teach Animal New Command")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_new_animal(registry)
        elif choice == '2':
            registry.list_animals()
        elif choice == '3':
            view_animal_commands(registry)
        elif choice == '4':
            teach_animal_command(registry)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
