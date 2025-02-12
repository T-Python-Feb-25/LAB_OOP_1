class Panda:

    def __init__(self, name:str , age:int , weight:int , color:str ):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color

    def get_weight(self):
        return f"the panda name is {self.name} the weight is {self.weight} KG"
    
    def get_color(self):
        return f"the panda name is {self.name} the color is {self.color}"