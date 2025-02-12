'''
Using what you learned about classes , create a class to represent a Panda. The class should have the following:
4 Attributes
2 Methods
'''
# panda.py

class Panda:
    def __init__(self, name, age, weight, habits):
        self.name = name
        self.age = age
        self.weight = weight
        self.habits = habits

    def weights(self):
        return f"{self.name} weights {self.weight}."

    def add_habits(self):
        return f"{self.name} is a {self.age} years old enjoying his leisure time {self.habits}."


'''
this is the first Python lab in the Course
Feb12, 2025
By Mohammed Albushaier
'''
