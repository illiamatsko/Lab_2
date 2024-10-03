from Animal import Animal

class AquaticAnimal(Animal):
    aquatic_counter = 0

    def __init__(self, species, name, age, water_type=""):
        super().__init__(species, name, age)
        self._water_type = water_type
        AquaticAnimal.aquatic_counter += 1

    @property
    def water_type(self):
        return self._water_type

    def swim(self):
        return f"{self.name} is swimming in {self.water_type} water."

    @staticmethod
    def get_total_aquatic_animals():
        return AquaticAnimal.aquatic_counter

    def __str__(self):
        return f"Aquatic Animal: {super().__str__()} in {self.water_type} water"