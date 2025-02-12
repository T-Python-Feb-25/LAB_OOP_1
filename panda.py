class Panda:
    def __init__(self, gender: str, age: int, weight: float, color: str):
        self.gender = gender
        self.age = age
        self.weight = weight
        self.color = color

    def getColor(self):
        return f"The Panda Color Is {self.color}"
    def getWeight(self):
        return f"The Panda Weight Is {self.weight}"
