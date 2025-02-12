
class Panda:
    
    #constructer
    def __init__(self, name:str ,age:int ,weight:float,hight:float):
        #attrrbutes
        self.name=name
        self.age=age
        self.weight=weight
        self.hight=hight

    
    def profile(self)->str:
        return f"This Panda's Name is {self.name} it is {self.age} years old "
    

    def health_data(self)->str:
        return f"-{self.name} health check :\nweight : {self.weight}\nhight : {self.hight}\n"
    



