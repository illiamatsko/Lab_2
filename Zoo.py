class Zoo:
    animals_count = 0

    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        Zoo.animals_count += 1

    def show_animals(self):
        for animal in self.animals:
            print(animal)

    @staticmethod
    def total_animals():
        return f"Total number of animals in the zoo: {Zoo.animals_count}"