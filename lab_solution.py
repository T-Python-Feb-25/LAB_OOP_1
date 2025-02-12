"""# LAB_OOP_1
## Using what you learned about classes , create a class to represent a Panda. The class should have the following:
- 4 Attributes
- 2 Methods


### Create 4 instances/objects of the class Panda , print 1 attribute value,  and call the two methods on each instance. 
#### Note:
Arrange your code in seperate files (one for the main file for main logic , and another for the definition of the class). 
"""
from Panda import Panda

panda1=Panda("Lili",6,90,113)
panda2=Panda("Moli",3,60,90)


print(panda1.profile())
print(panda1.health_data())


print(panda2.profile())
print(panda2.health_data())



