class Animal:
    count = 0

    def __init__(self, species, name, age):
        self._species = species
        self._name = name
        self._age = age
        Animal.count += 1

    @property
    def species(self):
        return self._species

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def make_sound(self):
        return "Generic animal sound."

    def __str__(self):
        return f"{self.species} named {self.name}, age {self.age}"

    @staticmethod
    def total_count():
        return Animal.count