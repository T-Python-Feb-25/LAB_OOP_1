
class Panda:
    def __init__(self, name, age, weight, color):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color

    def eat(self, food):
        return f"{self.name} is eating {food}"

    def sleep(self):
        return f"{self.name} is sleeping"
