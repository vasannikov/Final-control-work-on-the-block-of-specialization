class Animal:
    def __init__(self, name, birth_date):
        self._name = name
        self._birth_date = birth_date
        self._commands = []

    def get_name(self):
        return self._name

    def get_birth_date(self):
        return self._birth_date

    def get_commands(self):
        return self._commands

    def learn_command(self, command):
        if command not in self._commands:
            self._commands.append(command)

class Pet(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

class WorkingAnimal(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

class Dog(Pet):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

class Cat(Pet):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

class Hamster(Pet):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

class Horse(WorkingAnimal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

class Donkey(WorkingAnimal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

