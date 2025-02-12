class Panda:
  def __init__(self, name, age, weight, favorite_food):
    self.name = name
    self.age = age
    self.weight = weight
    self.favorite_food = favorite_food

  def eat(self):
    print(f"{self.name} is eting {self.favorite_food}")

  def sleep(self):
    print(f"{self.name} is sleeping")
