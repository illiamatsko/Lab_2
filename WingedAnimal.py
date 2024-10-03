from Animal import Animal

class WingedAnimal(Animal):
    winged_count = 0

    def __init__(self, species, name, age, wing_span=0):
        super().__init__(species, name, age)
        self._wing_span = wing_span
        WingedAnimal.winged_count += 1

    @property
    def wing_span(self):
        return self._wing_span

    def fly(self):
        return f"{self.name} is flying!"

    @staticmethod
    def total_winged_count():
        return WingedAnimal.winged_count

    def __str__(self):
        return f"{super().__str__()} with a wingspan of {self.wing_span} meters"
