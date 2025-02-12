class Panda():
    def __init__(self,color:str,name:str,height:float,age:int):
        self.color=color
        self.name=name
        self.height=height
        self.age=age
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    def play(self):
        print(f"{self.name} is playing with his friend")