from WingedAnimal import WingedAnimal

class Bird(WingedAnimal):
    bird_count = 0

    def __init__(self, name, age, wing_span, species="Bird"):
        super().__init__(species, name, age, wing_span)
        Bird.bird_count += 1

    def make_sound(self):
        return f"{self.name} chirps!"

    @staticmethod
    def total_bird_count():
        return Bird.bird_count

    def __str__(self):
        return f"Bird: {super().__str__()}"
