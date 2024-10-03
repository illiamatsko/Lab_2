from Zoo import Zoo
from Animal import Animal
from Mammal import Mammal
from WingedAnimal import WingedAnimal
from Bird import Bird
from FlyingFish import FlyingFish


zoo = Zoo()

sparrow = Bird("Sparrow", 2, 0.3)
zoo.add_animal(sparrow)
print(sparrow)
print(sparrow.make_sound())

eagle = Bird("Eagle", 5, 2.5)
zoo.add_animal(eagle)
print(eagle)
print(eagle.make_sound())
print(eagle.fly())

flying_fish = FlyingFish("Swoop", 0.3, "salt", 2)
zoo.add_animal(flying_fish)
print(flying_fish.glide())
print(flying_fish.swim())

dog = Mammal("Dog", 3, "orange", "Golden Retriever")
zoo.add_animal(dog)

print()
print(f"Total Animals: {Animal.total_count()}")
print(f"Total Winged Animals: {WingedAnimal.total_winged_count()}")
print(f"Total Birds: {Bird.total_bird_count()}")
print(f"Total Mammals: {Mammal.get_total_mammals()}")
print(f"Total Flying Fish: {FlyingFish.get_total_flying_fish()}")

print()
zoo.show_animals()