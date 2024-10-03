from AquaticAnimal import AquaticAnimal
from WingedAnimal import WingedAnimal

class FlyingFish(AquaticAnimal, WingedAnimal):
    flying_fish_counter = 0

    def __init__(self, name, wingspan, water_type, age):
        super().__init__("Flying Fish", name, age,)
        self._water_type = water_type
        self._wing_span = wingspan
        FlyingFish.flying_fish_counter += 1

    def glide(self):
        return f"{self.name} is gliding above the {self.water_type} water."

    @staticmethod
    def get_total_flying_fish():
        return FlyingFish.flying_fish_counter

    def __str__(self):
        return f"Flying Fish: {super().__str__()}"