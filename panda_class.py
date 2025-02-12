# panda_class.py

class Panda:
    # initializer/ constructor
    def __init__(self, name: str, home: str, diet: str, age: int, days: str) -> None:
        # attributes/ properties
        self.name = name
        self.home = home
        self.diet = diet
        self.age = age
        self.days = days

    # methods
    def introduce(self):
        introduction = f"{self.name} live in {self.home}. They eat {self.diet} and they live up to {self.age} years in the wild."
        return introduction

    def book_visit(self):
        visit = f"You can always book a visit to see {self.name} at our zoo. They're available on {self.days}."
        return visit
