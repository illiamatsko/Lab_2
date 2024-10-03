from Animal import Animal

class Mammal(Animal):
    mammal_counter = 0

    def __init__(self, species, name, fur_color, age):
        super().__init__(species, name, age)
        self.fur_color = fur_color
        Mammal.mammal_counter += 1

    def run(self):
        return f"{self.name} is running with {self.fur_color} fur."

    @staticmethod
    def get_total_mammals():
        return Mammal.mammal_counter

    def __str__(self):
        return f"Mammal: {super().__str__()} with {self.fur_color} fur"