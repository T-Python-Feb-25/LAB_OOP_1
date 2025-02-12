'''Using what you learned about classes , create a class to represent a Panda. The class should have the following:
4 Attributes
2 Methods
Create 4 instances/objects of the class Panda , print 1 attribute value, and call the two methods on each instance.
Note:'''

class Panda:
    #initilizer/ constructor
    def __init__(animal, name:str, home:str, diet:str, age:int) -> None:
        #addtributes/ properties
        animal.name = name
        animal.home = home
        animal.diet = diet
        animal.age = age
        
        
    #methods
    def introduce(animal):
        introduction = f"{animal.name} live in {animal.home}, They eat {animal.diet} and they live up to {animal.age} years in the wild."
        return introduction


#creating instances/ objects

red_pandas = Panda("Red Pandas", "the eastern Himalayas & southwestern China", "bamboo, fruits, and small animals", 10)
giant_pandas = Panda("Giant Pandas", "the mountainous regions of central China", "bamboo, and sometimes small animals", 20)

#calling a method
print(red_pandas.introduce())
#print(giant_pandas.introduce())
        