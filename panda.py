
class Panda:
    def __init__(self, name:str, age:int, weight:float, is_wild:bool):
        self.name = name
        self.age = age
        self.weight = weight
        self.is_wild = is_wild

    def identity(self):
        return f"{self.name}"

    def details(self):
        return f"{self.name} is {self.age} years old, weighs {self.weight} kg and is {'wild' if self.is_wild else 'not wild'}."





        