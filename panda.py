class Panda:
    def __init__(self, name,age,weight,height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def eat(self,foodname,amount):
        eat=f"{self.name} eats {foodname}kg and the amount must be {amount} ."
        return eat

    def sleep(self,hours):
        sleep= f"{self.name} sleeps for {hours} hours"
        return sleep