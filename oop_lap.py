class Panda:
    def _init_(self, name, age, weight, favorite_food):
        """Initialize the Panda attributes."""
        self.name = name
        self.age = age
        self.weight = weight
        self.favorite_food = favorite_food

    def eat(self):
        """Method to simulate the panda eating."""
        print(f"{self.name} is eating {self.favorite_food}.")

    def sleep(self):
        """Method to simulate the panda sleeping."""
        print(f"{self.name} is sleeping peacefully.")



        from panda import Panda

# Creating 4 instances of Panda
panda1 = Panda("Po", 5, 100, "Bamboo")
panda2 = Panda("Lulu", 3, 85, "Fruits")
panda3 = Panda("Bao", 7, 120, "Sugarcane")
panda4 = Panda("Ming", 4, 95, "Leaves")

# Printing 1 attribute value
print(f"{panda1.name} is {panda1.age} years old.")

# Calling methods on each instance
for panda in [panda1, panda2, panda3, panda4]:
    panda.eat()
    panda.sleep()