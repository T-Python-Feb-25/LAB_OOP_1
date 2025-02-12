class Panda:

    species = "Giant Panda"

    def __init__(self, name, age, color, favorite_food):
        # Instance Attributes
        self.name = name
        self.age = age
        self.color = color
        self.favorite_food = favorite_food

    # Method1 Describe eating behavior
    def eat(self):
        print(f"{self.name} is munching on {self.favorite_food}!")

    # Method2 Describe playing behavior
    def play(self):
        print(f"{self.name} is rolling around in the bamboo forest!")
        
        
# Create4 Panda instances
panda1 = Panda("Bao Bao", 5, "Black and White", "Bamboo")
panda2 = Panda("Mei Mei", 3, "White", "Apples")
panda3 = Panda("Xing Xing", 7, "Black", "Sweet Potatoes")
panda4 = Panda("Ling Ling", 2, "Brown", "Carrots")

# List of pandas
pandas = [panda1, panda2, panda3, panda4]

# Interact with each panda
for panda in pandas:
    print(f"\n{panda.name}'s favorite food: {panda.favorite_food}")
    panda.eat()
    panda.play()